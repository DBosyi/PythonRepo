from flask import Flask, render_template, request
from datetime import datetime
import matplotlib.pyplot as plt
import io
import base64


app = Flask(__name__)

@app.route('/')
def index():

    # Пример данных для графика
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Построение графика
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Пример графика')

    # Преобразование графика в изображение в памяти
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Возвращение HTML-страницы с встроенным графиком
    return render_template('index.html', now=datetime.now(), plot_image=image_base64)	

if __name__ == "__main__":
	app.run()