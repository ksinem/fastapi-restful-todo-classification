import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import json

with open("config.json", "r") as f:
    config = json.load(f)


vectorizer_params = config["model_config"]["vectorizer"]["params"]
if 'ngram_range' in vectorizer_params:
    vectorizer_params['ngram_range'] = tuple(vectorizer_params['ngram_range'])

vectorizer = TfidfVectorizer(**vectorizer_params)
model = LinearSVC(**config["model_config"]["params"])



def load_training_data() -> list[dict]:
    with open(config["paths"]["train_data"], "r", encoding="utf-8") as f:
        training_data = json.load(f)
    return training_data

def get_features_and_labels():
    training_data = load_training_data()
    tasks = [item['task'] for item in training_data]
    descriptions = [item['description'] for item in training_data]
    labels = [item['label'] for item in training_data]
    X = vectorizer.fit_transform([f"{t} {d}" for t, d in zip(tasks, descriptions)])
    joblib.dump(vectorizer, r'model_dumps\category_vectorizer.joblib')
    le = LabelEncoder()
    y = le.fit_transform(labels)
    joblib.dump(le, r'model_dumps\label_encoder.joblib')
    print(f"Encoded labels: {le.classes_}")
    return X,y

def train_and_test_model():
    X,y = get_features_and_labels()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model.fit(X_train, y_train)
    joblib.dump(model, rf'model_dumps\{config["model_config"]["active_model"]}_classifier.joblib')
    print("\n--- Evaluation ---")
    y_pred = model.predict(X_test)
    performance = classification_report(y_test, y_pred)
    print(f"Classification report on test data: \n {performance}")


if __name__ == "__main__":
    train_and_test_model()

