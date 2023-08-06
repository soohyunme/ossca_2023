import io

import joblib
import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, request
from PIL import Image
from tensorflow import keras

app = Flask(__name__)
study_pred_model = joblib.load("./regression_model.pkl")
cat_dog_model = tf.keras.models.load_model("./cat_dog_model.h5")


@app.route("/")
def index():
    return "Index Page"


# http://localhost:5000/hello - 2
@app.route("/hello")
def hello():
    return "Hi World"


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
    hours = int(request.args.get("hours"))
    X_sample = np.array(hours).reshape(-1, 1)
    y_sample_pred = study_pred_model.predict(X_sample)
    return {"score": int(y_sample_pred)}


# chapter 7 todo 5
@app.route("/predict_catdog", methods=["POST"])
def inference_catdog():
    file = request.files["file"]
    img = keras.utils.load_img(io.BytesIO(file.read()), target_size=(180, 180))
    img_array = keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = cat_dog_model.predict(img_array)
    score = float(predictions[0])
    image_class = "cat" if score < 0.5 else "dog"

    return jsonify({"predict_result": image_class})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
