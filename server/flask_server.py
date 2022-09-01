import base64
import io
from random import choice

import matplotlib.pyplot as plt
from flask import Flask, render_template, request

from triangle.triangle import perimeters

app = Flask(__name__, template_folder='templates')
host = '127.0.0.1'
port = int('8086')


class FlaskServer:
    @staticmethod
    def matplotlib_visualize(perim, x=None, y=None):
        img = io.BytesIO()
        colors = [choice(["r", "g", "b", "c", "m", "y", "k", "w", "darkblue", "plum", "cyan", "coral", "olive", "grey"])
                  for i in range(0, len(perim['elem']))]
        # plt.figure(figsize=(14, 8))
        fig, ax = plt.subplots(figsize=(14, 8))
        plt.title("Dependence of the perimeter of the element on its number", fontsize=16)
        plt.grid()
        plt.xlabel("Number of element", fontsize=14)
        plt.ylabel("Perimeter of element", fontsize=14)
        ax.bar(perim['elem'], perim['perimeter'], edgecolor="k", linewidth=4, color=colors)
        # ax.text(628.0, -572.0, str(f"{perim['perimeter'][0]}"))
        if request.method == "POST" and x is not None and y is not None:
            elem = FlaskServer.define_bars(x)
            print(elem)
            plt.xticks(perim['elem'][elem], [perim['perimeter'][elem]], rotation="vertical")
        # plt.bar(perim['elem'], perim['perimeter'], edgecolor="k", linewidth=4, color=colors)
        # ax.text(perim['perimeter'], color='black', fontweight='bold')
        plt.savefig(img, format='png')
        plot_url = base64.b64encode(img.getvalue()).decode()
        return plot_url

    @staticmethod
    def define_bars(x):
        # full_coordinates = len(perim['perimeter']) * 30.0
        print(x)
        current_elem = int(round((x - 47) / 30, 0))
        print(current_elem)
        return current_elem

    @staticmethod
    def make_offset(x, y):
        x_correct = float(x - 176)
        y_correct = float(y - 712)
        return x_correct, y_correct

    @staticmethod
    @app.route('/get_visualize', methods=['GET', 'POST'])
    def get_visualize():
        if request.method == "GET":
            plot_url = FlaskServer.matplotlib_visualize(perimeters)
            return render_template('diagram.html', plot_url=plot_url)
        else:
            x = int(request.form['sub.x'])
            y = int(request.form['sub.y'])
            x_corr, y_corr = FlaskServer.make_offset(x, y)
            plot_url = FlaskServer.matplotlib_visualize(perimeters, x_corr, y_corr)

            return render_template('diagram.html', plot_url=plot_url)

    @staticmethod
    @app.route('/', methods=['GET'])
    def main_menu():
        return render_template('main_menu.html')


if __name__ == "__main__":
    app.run(host, port)
