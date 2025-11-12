from flask import Flask, request, jsonify, render_template, redirect, session, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS
import numpy as np
from keras.preprocessing import image as keras_image
from keras.models import load_model
import logging
import cv2
import json

app = Flask(__name__)
app.secret_key = 'randombs'

CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_IMAGE_SIZE = 16 * 1024 * 1024  # 16MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_IMAGE_SIZE

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('predictions', exist_ok=True)

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model = None
disease_class = ['Benign', 'Malignant']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS #need to actually check if the file is an image

# Cache model to avoid loading it on every request
def load_saved_model():
    global model
    if model is None:
        model = load_model(os.path.join("models", "vgg19.h5"))
    return model


def image_processor(image_path, target_size):
    """Preprocess images for CNN model"""
    absolute_image_path = os.path.abspath(image_path)
    image = cv2.imread(absolute_image_path)
    if image is None:
        raise ValueError("Could not read the image!")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (target_size[1], target_size[0]))
    image_array = image / 255.0
    return image_array

def predict(image_path):
    target_size = (224, 224, 3)
    processed_img = image_processor(image_path, target_size)
    img_array = np.array([processed_img])

    model = load_saved_model()
    predictions = model.predict(img_array)
    results = {}
    for i, prediction in enumerate(predictions[0]):
        disease = disease_class[i]
        probability = float(prediction * 100)  # Convert probability to percentage
        results[disease] = probability
    return results

def save_prediction_data(prediction_data, filename):
    # Save the prediction data to the file
    with open(filename, 'w') as file:
        json.dump(prediction_data, file)

def load_prediction_data(filename):
    with open(filename, 'r') as file:
        prediction_data = json.load(file)
    return prediction_data



@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        try:
            result = predict(filepath)
            session["prediction_result"] = result
            test_dic = {}
            test_dic[filename] = result
            save_prediction_data(test_dic, os.path.join("predictions", "prediction_data.json"))
            return redirect(url_for('render_predictions'))
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            return jsonify({'error': 'Error occurred during prediction'}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route('/predictions')
def render_predictions():
    result = load_prediction_data(os.path.join("predictions", "prediction_data.json"))
    return render_template('predictions.html', prediction_result = result)

@app.route('/uploads/<path:filename>')
def serve_file(filename):
    print(filename)
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/')
def render_uploads():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
