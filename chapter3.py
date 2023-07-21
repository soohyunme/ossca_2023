from flask import Flask, jsonify, request
from PIL import Image

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


# http://localhost:5000/hello - 2
@app.route("/hello")
def hello():
    return "Hello World"


# In postman -> [POST] http://localhost:5000/echo, {body - raw - json} -> {"parameter": "test"}  - 4
@app.route("/echo", methods=["POST"])
def get_echo():
    param = request.get_json()
    return jsonify(param)


# In postman -> [POST] http://localhost:5000/upload_image, {form-data} -> key=file, value=test.jpg - 5
@app.route("/upload_image", methods=["POST"])
def upload_image():
    img = Image.open(request.files["file"])
    width, height = img.size
    return jsonify({"width": width, "height": height})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
