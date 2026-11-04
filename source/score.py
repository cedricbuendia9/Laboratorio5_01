import joblib


def load_model():
    return joblib.load("artifacts/model.pkl")


def predict(features):

    model = load_model()

    prediction = model.predict([features])

    return float(prediction[0])


if __name__ == "__main__":
    sample = [
        0.038,
        0.050,
        0.061,
        0.021,
        -0.044,
        -0.034,
        -0.043,
        -0.002,
        0.019,
        -0.017,
    ]

    result = predict(sample)

    print(result)
