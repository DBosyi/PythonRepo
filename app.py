from flask import Flask, render_template, request
from datetime import datetime
import pygal

app = Flask(__name__)

@app.route('/')
def index():

	# Example data for the plot
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Creating the line chart
    line_chart = pygal.Line()
    line_chart.title = 'Example Chart'
    line_chart.x_labels = x
    line_chart.add('Series', y)

    # Rendering the chart to SVG format
    chart_svg = line_chart.render()

    # Returning the HTML page with the embedded chart SVG
    return render_template('index.html', now=datetime.now(), plot_image=chart_svg)	

if __name__ == "__main__":
	app.run()