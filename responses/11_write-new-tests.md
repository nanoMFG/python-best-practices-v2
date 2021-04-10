## Test-driven development

Now that you know how to run pytest, let's actually write some tests. You might wonder why we start by writing tests instead of implementing the methods first. Technically that's a choice you could make and it could be the case that sometimes it's fine to implement the methods first. However, Test-driven development (TDD) is a software development process that starts with writing the tests based on the software requirements and then tracking software development by testing the software against the tests that are already written.

Although we won't ask you to write any rigorous tests for this course as our focus is more on the process than the outcome, we do want you to get a feel for how we expect your MINIST Model to perform by writing tests!

## Step 12: Write your own tests

As we explained in Step 5 of the course, the project you are working on is an MNIST Model. The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. So after you implement your model and train the model, your model should be able to determine what digit an image represents. If your model can classify images as expected, your model is working but if it isn't it must be failing to do its job.

Let's go through how we can write a rough test to check whether the model is working as expected!


TensorFlow, one of the packages we need to install, actually requires your Python version to be 3.6-3.8. As a result, we have to specify that in our build script. Here's some example values for python_requires and install_requires. The following example project requires a Python version above 3.0 and requires installation of django and pandas. Use the example ```setup.py``` as an example for your project's ```setup.py```.
```python
setuptools.setup(
    name="example_package-username", # Replace with your own username
    ...
    packages=setuptools.find_packages(),
    python_requires='>=3.0',
    install_requires=[
        'django',
        'pandas'
    ]
```

Once your ```setup.py``` is complete, we can run a few commands to install everything you need for your project.
### :keyboard: Activity: Write a test for the MINIST classifier

1. Check the documentation for the ```model.py``` file. For the evaluate_after adding values for the ```python_requires and ```install_requires``` field
2. Run ```pip-compile```
This should create a ```requirements.txt file```. If it's failing, check if there's any problems with your setup.py
3. Run ```pip install -r requirements.txt```

You should now be ready to run some tests for your project. Merge the pull request and we will let you know if you are good to go!
