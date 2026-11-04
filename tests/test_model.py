import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from source.model import create_model


def test_model_creation():
    model = create_model()

    assert model is not None
