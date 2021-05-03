from digit_reader.model.helpers import prepare_data
from digit_reader.model.model import MNISTModel

def test_classify_image():
    (x_train, y_train), (x_test, y_test) = prepare_data()
    model = MNISTModel()
    model.train_model(x_train, y_train, epochs=2)
    assert model.classify_image(x_test[0]) == 7
