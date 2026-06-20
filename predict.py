import pickle

from feature_extractor import extract_features

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

while True:

    url = input("\nEnter URL (or type exit): ")

    if url.lower() == "exit":
        break

    features = [extract_features(url)]

    prediction = model.predict(features)[0]

    if prediction == 1:
        print("⚠️ Malicious URL")
    else:
        print("✅ Safe URL")