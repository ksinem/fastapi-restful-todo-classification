import os
from pathlib import Path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, r'model_dumps\linear_svc_classifier.joblib')
VECTORIZER_PATH = os.path.join(BASE_DIR, r'model_dumps\category_vectorizer.joblib')
LABEL_ENCODER_PATH = os.path.join(BASE_DIR, r'model_dumps\label_encoder.joblib')

