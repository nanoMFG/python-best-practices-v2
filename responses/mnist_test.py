from digit_reader.model.helpers import prepare_data
from digit_reader.model.model import MNISTModel

def test_failing():
    # this test should initially be failing for some reason, then the user will fix it
    # could be as simple as having it initially be 'assert False' or something more complex
    assert True


def test_x_shape():
    (x_train, y_train), (x_test, y_test) = prepare_data()
    # test if all training images were loaded
    assert x_train.shape[0] == 60000
    # test if all test images were loaded
    assert x_test.shape[0] == 10000
    # test if images are square
    assert x_train.shape[1] == x_train.shape[2]


def test_y_shape():
    (x_train, y_train), (x_test, y_test) = prepare_data()
    # test if all training labels were loaded
    assert y_train.shape[0] == 60000
    # test if all test labels were loaded
    assert y_test.shape[0] == 10000
