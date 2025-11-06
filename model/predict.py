import joblib
from utils.constants import MODEL_PATH, VECTORIZER_PATH, LABEL_ENCODER_PATH



classifier = None
vectorizer = None
label_encoder = None


def load_models():
    # Lazy loading of the models: load only when needed
    global classifier, vectorizer, label_encoder
    if classifier is None and vectorizer is None and label_encoder is None:
        classifier = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        label_encoder = joblib.load(LABEL_ENCODER_PATH)


def predict_category(task: str, description: str) -> str:
    load_models()
    if not task and not description:
        return "Uncategorized"
    full_text = [f"{task} {description}"]
    X_new = vectorizer.transform(full_text)
    prediction_numeric = classifier.predict(X_new)[0]  # this is an array with one number in it -> access with [0]
    predicted_label = label_encoder.inverse_transform([prediction_numeric])[0]  # also a 1D array
    return predicted_label


print(predict_category(task="Fix database connection issue",
                 description="Debug the production error caused by the recent migration script and roll back if necessary."))
# result: Development/Tech
