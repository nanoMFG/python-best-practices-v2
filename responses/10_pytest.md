## Step 10: First test with pytest
Look through some of the tests we wrote to see how your write the tests. Inside tests, you check for whether a function is behaving as expected by asserting that the actual value obtained from the function is equal to the value you expect from the function.

Each test case should be in the form of a function starting with test_ and the test case will fail if any of the assert statements fail. Just like source code, you do need to import the functions or classes you use from the files that you are testing.
### :keyboard: Activity: Install and run pytest
1. Install pytest by running ```pip install -U pytest```
2. Check for the version using ```pytest --version```
3. Now to run pytest just run ```pytest```
Now, you should see a test called ```test_failing()``` that is failing. Figure out how to make the test case pass, then move on to the next step.
4. If your test pass, you are ready for the next step! However, before you go, we would strongly recommend that you take a look at some [flags](https://docs.pytest.org/en/stable/usage.html) you could use when running pytest.


