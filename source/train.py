from pathlib import Path

import joblib
from model import create_model
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def train():

    data = load_diabetes()

    x = data.data
    y = data.target

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = create_model()

    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    mse = mean_squared_error(y_test, predictions)

    print(f"MSE: {mse}")

    Path("artifacts").mkdir(exist_ok=True)

    joblib.dump(model, "artifacts/model.pkl")

    print("Modelo guardado")


if __name__ == "__main__":
    train()
