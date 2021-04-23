import pytest

class TestTestMnist():
    def test_test_mnist_content(self):
        with open('src/digit_reader/test/test_mnist.py') as test_file:
            prepare_data_exists = False
            classify_image_exists = False
            mnist_model_exists = False
            for line in model_file:
                if 'prepare_data' in line:
                    prepare_data_exists = True
                elif 'model.classify_image(x_test[0])' in line:
                    classify_image_exists = True
                elif 'MNISTModel()' in line:
                    mnist_model_exists = True
        assert prepare_data_exists and classify_image_exists and mnist_model_exists
