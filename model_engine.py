"""
Model Inference Engine for Plant Disease Detection
Loads plant_disease_model.keras and provides high-performance predictions.
"""

import os
import json
import numpy as np
from PIL import Image

# Suppress verbose TensorFlow warnings
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import keras
from disease_info import format_class_name, get_disease_info

MODEL_PATH = os.path.join(os.path.dirname(__file__), "plant_disease_model.keras")
CLASS_NAMES_PATH = os.path.join(os.path.dirname(__file__), "class_names.json")
IMG_SIZE = 160

_model = None
_class_names = None


def get_class_names():
    """Loads and caches the class names list."""
    global _class_names
    if _class_names is None:
        if os.path.exists(CLASS_NAMES_PATH):
            with open(CLASS_NAMES_PATH, "r", encoding="utf-8") as f:
                _class_names = json.load(f)
        else:
            raise FileNotFoundError(f"Class names file not found at: {CLASS_NAMES_PATH}")
    return _class_names


def get_model():
    """Lazily loads and caches the Keras model."""
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")
        _model = keras.models.load_model(MODEL_PATH)
    return _model


def preprocess_image(image_input):
    """
    Accepts PIL Image, file path, or numpy array,
    converts to RGB and resizes to (160, 160).
    """
    if isinstance(image_input, str):
        img = Image.open(image_input)
    elif isinstance(image_input, np.ndarray):
        img = Image.fromarray(image_input)
    elif isinstance(image_input, Image.Image):
        img = image_input
    else:
        raise ValueError(f"Unsupported image input type: {type(image_input)}")

    img = img.convert("RGB").resize((IMG_SIZE, IMG_SIZE))
    arr = np.array(img, dtype=np.float32)
    # Model expects batch dimension: shape (1, 160, 160, 3)
    arr = np.expand_dims(arr, axis=0)
    return img, arr


def predict_disease(image_input, top_k=5):
    """
    Runs model inference on an image.
    Returns:
        dict containing:
            - top_prediction: dict with class, plant, condition, confidence, is_healthy, info
            - top_k: list of top k predictions with rank, class_name, display_name, confidence, is_healthy
            - all_probabilities: full dictionary of class -> float confidence
    """
    model = get_model()
    class_names = get_class_names()
    
    _, arr = preprocess_image(image_input)
    preds = model.predict(arr, verbose=0)[0]

    # Sort indices by probability descending
    top_indices = np.argsort(preds)[::-1][:top_k]

    top_k_list = []
    for rank, idx in enumerate(top_indices, 1):
        raw_name = class_names[idx]
        conf = float(preds[idx])
        info = get_disease_info(raw_name)
        top_k_list.append({
            "rank": rank,
            "raw_class": raw_name,
            "display_name": format_class_name(raw_name),
            "confidence": conf,
            "confidence_pct": round(conf * 100, 2),
            "is_healthy": info["is_healthy"],
            "plant": info["plant"],
            "condition": info["condition"],
            "info": info
        })

    top_pred = top_k_list[0]
    all_probs = {format_class_name(class_names[i]): float(preds[i]) for i in range(len(class_names))}

    return {
        "top_prediction": top_pred,
        "top_k": top_k_list,
        "all_probabilities": all_probs
    }


if __name__ == "__main__":
    print("Testing model engine...")
    classes = get_class_names()
    print(f"Loaded {len(classes)} classes.")
    m = get_model()
    print("Model summary input shape:", m.input_shape)
    dummy_img = Image.new("RGB", (200, 200), color=(120, 180, 70))
    res = predict_disease(dummy_img, top_k=3)
    print("Top prediction:", res["top_prediction"]["display_name"], f"({res['top_prediction']['confidence_pct']}%)")

