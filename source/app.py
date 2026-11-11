from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("artifacts/model.pkl")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json["data"]

    prediction = model.predict([data])

    return jsonify({
        "prediction": float(prediction[0]),
        "version": "2.0"
    })

app.run(host="0.0.0.0", port=5000)
@app.route("/")
def home():
    return "API Diabetes funcionando correctamente"
