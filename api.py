from flask import Flask
from src.visualizer import Visualizer
from flask import request
from flask import send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def get_graph():
    fx = request.args.get('fx')
    fy = request.args.get('fy')
    skip = request.args.get('skip')
    v = Visualizer(f_x=str(fx), f_y=str(fy))
    v.plot_color(skip=int(skip))
    return send_file("./vector_field.jpg")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
