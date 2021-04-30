import os
import pytest

class TestModules():
    def test_initpy(self):
        assert os.path.isfile('src/digit_reader/__init__.py')
        assert os.path.isfile('src/digit_reader/model/__init__.py')

    def test_skeleton_code(self):
        with open('src/digit_reader/model/model.py') as model_file
        assert 'class MNISTModel:' in model_file
        assert 'def train_model(self' in model_file
        assert 'def evaluate_model(self' in model_file

    def test_docstrings(self):
        with open('src/digit_reader/model/model.py') as model_file:
            docstrings = 0
            for line in model_file:
                if '\"\"\"' in line:
                    docstrings += 1
        assert docstrings >= 3
