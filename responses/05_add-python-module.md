# Creating a python class

Python is an object oriented language, which means it can make use of classes. Don't worry, you won't need to know much about object oriented programming for this course. If you want a quick refresher, check out [this link](https://en.wikipedia.org/wiki/Object-oriented_programming).

### Python Class Structure

Python classes generally look like this: 

    class MyClass:
      def __init__(self):
        """ Initializer Method """
      def foo(self, args):
        """ Some method """
      def bar(self, args):
        """ Some other method """

For a more in depth explanation, see [this link](https://docs.python.org/3/tutorial/classes.html).

## Step 5: Commit python module code

In this step we are going to create a simple python module, with no functionality yet.

### :keyboard: Activity: Create a skeleton model.py

1. Create the file 'src/digit_reader/model/model.py'
2. Create the class 'MNISTModel'
3. Create blank methods named '\_\_init\_\_', 'train_model', and 'evaluate_model'
4. Commit your changes to this pull request's branch

**:bulb: [Add `src/digit_reader/model/model.py`]({{quicklink1}})**

If you get stuck, or don't feel like typing, you can click the dropdown below for the solution code. Feel free to copy and paste it.
<details><summary> A completed MNISTModel class </summary>

    class MNISTModel:
      def __init__(self):
        pass
      def train_model(self):
        pass
      def evaluate_model(self):
        pass

</details>
<hr>
<h3 align="center">Watch below this comment for my response</h3>

> _Sometimes I respond too fast for the page to update! If you perform an expected action and don't see a response from me, wait a few seconds and refresh the page for your next steps._
