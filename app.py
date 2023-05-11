from flask import Flask, render_template, request
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        # Получение загруженного файла из запроса
        file = request.files['datafile']

        # Сохранение файла с данными
        data_file_path = 'data.csv'  # Путь для сохранения файла
        file.save(data_file_path)

        # Загрузка данных из файла
        data = pd.read_csv(data_file_path)

        # Создание графика
        plt.plot(data['x'], data['y'])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('График данных')

        # Сохранение графика во временный файл
        temp_file = 'static/temp_plot.png'
        plt.savefig(temp_file)

        # Отображение графика на веб-странице
        return render_template('index.html', plot_image=temp_file)

    return render_template('upload.html')

if __name__ == "__main__":
	app.run()