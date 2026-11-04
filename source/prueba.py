from model import create_model
from sklearn.datasets import load_diabetes


def test_prediction():

    dataset = load_diabetes()

    x = dataset.data
    y = dataset.target

    model = create_model()

    model.fit(x, y)

    prediction = model.predict([x[0]])

    assert len(prediction) == 1
