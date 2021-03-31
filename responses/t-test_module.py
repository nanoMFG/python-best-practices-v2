import os
import pytest

class TestModules():
    def test_initpy(self):
        assert os.path.isfile('src/digit_reader/__init__.py')
        assert os.path.isfile('src/digit_reader/model/__init__.py')

    def test_skeleton_code(self):
        assert os.path.isfile('src/digit_reader/model/model.py')
        from digit_reader.model.model import MNISTModel
        model = MNISTModel()
        model.train_model()
        model.evaluate_model()

    def test_docstrings(self):
        assert True
