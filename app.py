from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

model = load_model("cifar10_model.keras")

classes = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "CIFAR-10 Deep Learning API is running"
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "Upload an image using the image field"}), 400

    image = Image.open(request.files["image"].stream).convert("RGB")

    input_shape = model.input_shape
    height, width = input_shape[1], input_shape[2]

    image = image.resize((width, height))
    array = np.array(image, dtype=np.float32)

    # Use this normalization only if it matches model training.
    array = array / 255.0
    array = np.expand_dims(array, axis=0)

    predictions = model.predict(array, verbose=0)
    class_id = int(np.argmax(predictions[0]))

    return jsonify({
        "class_id": class_id,
        "prediction": classes[class_id],
        "confidence": float(predictions[0][class_id])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)