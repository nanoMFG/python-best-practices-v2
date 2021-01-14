# Outline for python best practices

Try to follow template from here: https://lab.github.com/docs/sample-outline-table-events  

## Steps Outline
1. Set up your project
    * Create README.md, LICENSE.txt, .gitignore
    * Create new directories and move each file to the appropriate directories (ex: test_function to tests) by showing them the python application layout
    * Every commit the user makes, we comment and let them know whether it was valid (ex: if user commits a new README.md, we check to see if it's correct before providing instructions on LICENSE.txt)
3. Format existing code in mnist_convert.py using black
    * Install black formatter with pip, and run black mnist_convert.py
    * Still provide basics of formatting conventions
4. Add google-style comment blocks in mnist_convert.py
    * Provide example of google-style comments with 2 out of 4 functions in mnist_convert.py as examples
    * Instruct them to add comments in the other 2 with the google-stye comment block guidelines we provide
2. Create a setup file
    * Explain what a setup.py does and provide some instructions on what to include
    * Maybe provide a template for a setup.py in a drop down so they can refer to it if they fail to pass our tests
5. Create dependencies in setup.py and use pip tools to create a requirements.txt
    * The content of the requirements.txt file generated should be checked to see if the user did it correctly    
6. Install/create/activate virtual environment and Pip install packages using requirements.txt
    * mnist_convert.py should not run locally without installing some packages using pip
    * If we choose not to use CI and some function in mnist_convert.py can be run without dataset, we can probably ask the user to comment the output of the function when run locally
    * *TODO:* decide whether we introduce CI in this step, and when to include the step for downloading the dataset
7. Run existing tests in the repository
    * Introduce user to basics of continuous integration, pytest 
    * Enforce branch protection (explain why it's necessary)
    * Ask user to fix the tests that is blocking them from merging to main
    * *TODO:* Need to look into whether CI checks will not run without enforcing branch protection for main 
8. Create a new test
    * Provide instructions for creating a new test
    * Provide end result we expect them to have in a drop down
9. Create main.py
    * Explain its role and try to help user figure out what to write in main.py
    * Provide solution in drop down
    * Should we continue to use pull request from here?
10. Create documentation
    * Ask user to write documentation
    * *TODO:* How do we even test this? Should we just have an example in a dropdown and have them copy paste to move on to next steps?
11. *TODO:* Any more steps?

*Tasks without steps at the moment*
* *~~steps for creating basic python library with a function~~*
* *~~steps for creating an app that imports the function~~*
* *step for downloading dataset*
* *~~step for writing documentation~~*
* *~~maintaining a requirements.txt and/or environment.yml~~*

## Table with events
Step|App Actions| User Actions| Related Event | Status* | Assigned To
-----|-----|-----|-----|-----|-----
0|Create Repo||
1|App creates an issue, asks user to create new misc. files & directories, commit/push changes and close issue | User commits changes then close issue | issues.closed (getFileContents gate checks for each file added) | :white_check_mark: |
2|App creates an issue, asks user commit code formatted using black | User commits changes | push (getFileContents gate) | :ballot_box_with_check:|
3|App comments, ask user to add google-style comment blocks and commit | User commit changes | push (getFileContents gate) | :ballot_box_with_check:|
4|App comments, ask user to create setup.py file | User creates setup and closes issue | push (getFileContents gate)| |
5|App creates an issue, asks user to create dependencies in setup.py and comment the generated requirements.txt content on the issue| User commits changes | push (getFileContents gate)| :heavy_exclamation_mark:|
6|App asks user to create/activate virtual environment, pip install packages, run mnist_convert.py and comment the output on the issue| User comments| issue_comment.created (w/ a gate that checks whether output is as intended)| :ballot_box_with_check:|
7|App creates an issue, asks user to run pytest locally and fix the tests so the tests passes | User creates pull request and merges to main| pull_request.merged (run checks to block merges with invalid pull requests) | |
8|App asks user to commit the new test they create | User creates pull request and add merges to main |  push (getFileContents gate)|
9|App asks user to commit the main.py | User commits changes | push (getFileContents gate) ||
10|App asks user to commit documentation | User commits changes | push (getFileContents gate) ||
11|||

Status Labels*:
:white_check_mark: Complete
:ballot_box_with_check: Template Completed (Content still needs to be filled)
:heavy_exclamation_mark: Boundary cases not working
:x: Not working


*NOTE 1: I personally think pushes and pull requests are interchangable for most tasks. Pull requests are definitely better in terms of habits but I do think they can get a bit tedious with these courses so I used mostly issues for the steps I have included.

*NOTE 2: Continuous Integration could be good if we want user to make specific changes to a file. We need to find ways to run tests on pull requests to check whether the correct files were added.
