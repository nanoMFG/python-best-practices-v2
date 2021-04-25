## Test-driven development

Now that you know how to run pytest, let's actually write some tests. You might wonder why we start by writing tests instead of implementing the methods first. Technically that's a choice you could make and it could be the case that sometimes it's fine to implement the methods first. However, Test-driven development (TDD) is a software development process that starts with writing the tests based on the software requirements and then tracking software development by testing the software against the tests that are already written.

Although we won't ask you to write any rigorous tests for this course as our focus is more on the process than the outcome, we do want you to get a feel for how we expect your MINIST Model to perform by writing tests!

## Step 12: Write your own tests

As we explained in Step 5 of the course, the project you are working on is a MNIST Model. The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. So after you implement your model and train the model, your model should be able to determine what digit an image represents. If your model can classify images as expected, your model is working but if it isn't it must be failing to do its job.

Although in real projects, we wouldn't want to test few particular cases but instead aim to cover a large range of inputs and outputs, to simplify things, we just want you to write a test that checks whether one of the test images are properly classified.

Let's go through how we can write a rough test to check whether the model is working as expected!

### :keyboard: Activity: Write a test for the MINIST classifier
**:bulb: [Edit `tests/digit_reader/test_mnist.py`]({{quicklink1}})**

1. Read the comments for the ```classify_images``` function in the ```model.py``` file.
1. Go to ```mnist_test.py``` and create a new test case called ```test_classify_images```.
2. In the test case, you need to write a line of code to prepare the data you will used to test whether the function is working as expected. Refer to ```test_x_shape``` for help.
3. Now that you should have test images that you could send in as a parameter to the ```classify_images``` function, we will check whether the first testing image will return label ```9```.

Once you write your test, compare your code with the solution and then commit and push your changes. Next, we will actually write out the implment the ```classify_images``` function.

<details><summary>Solution</summary>
  
```  
    
def test_classify_image():
    (x_train, y_train), (x_test, y_test) = prepare_data()
    model = MNISTModel()
    assert model.classify_image(x_test[0]) == 9
    
```        

</details>
