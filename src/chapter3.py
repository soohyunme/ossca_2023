import joblib
import numpy as np
from flask import Flask, jsonify, request
from PIL import Image

app = Flask(__name__)
study_pred_model = joblib.load("./regression_model.pkl")


@app.route("/")
def index():
    return "Index Page"


# http://localhost:5000/hello - 2
@app.route("/hello")
def hello():
    return "Hello World"


# In postman -> [POST] http://localhost:5000/echo
# {body - raw - json} -> {"parameter": "test"}  - 4
@app.route("/echo", methods=["POST"])
def get_echo():
    param = request.get_json()
    return jsonify(param)


# In postman -> [POST] http://localhost:5000/upload_image
# {form-data} -> key=file, value=test.jpg - 5
@app.route("/upload_image", methods=["POST"])
def upload_image():
    img = Image.open(request.files["file"])
    width, height = img.size
    return jsonify({"width": width, "height": height})


# chapter 7 todo 4
@app.route("/predict_score")
def inference_study():
    # Predict sample data - 7
    X_sample = np.array([11]).reshape(-1, 1)
    y_sample_pred = study_pred_model.predict(X_sample)
    return {"score" : int(y_sample_pred)}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
