# :wave: Welcome to "Python Best Practices" 
Hello and welcome to the interactive GitHub Learning Lab course on Python and "best practices".

## About The Project
This project will introduce basic skills for building up a Python project and good habits to follow while developing it.  A commonly used directory structure and its purpose will be presented along with a number of what we consider to be "best practices".

The best practices presented here are intended to be a stepping stone away from monolithic single scripts, or cluttered notebooks and toward code that is more maintainable, easier to read, test and install and ultimately easier for **others** to use and contribute to.

### Project Goals

* Create a working Python machine learning application that lives on GitHub.
* Learn one way to organize application directories to maintain installable, testable code.
* Develop primary functions within Python [module files](https://docs.python.org/3/tutorial/modules.html) within a simple [package](https://docs.python.org/3/tutorial/modules.html#packages).
* Use [docstrings](https://www.python.org/dev/peps/pep-0257/) with a [consistent style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) to document modules, classes and functions.
* Add a basic [`setup.py`](https://docs.python.org/3/distutils/setupscript.html) file to enable local `pip install`.
* Pin requirements and use a virtual environment with [pip tools](https://github.com/jazzband/pip-tools) and Conda.
* Develop code that passes tests using [pytest](https://docs.pytest.org).
* Add GitHub continuous integration features to automate testing and formatting.  

To get started, I'll guide you through some background on what the term "best practices" means and why we need them.
Then I'll show you a particular set of best practices and how they apply to a modest Python-based machine learning
app.

:point_down: _This arrow means you can expand the window! Click on them throughout the course to find more information.
<details><summary>What are Best Practices?</summary>
<hr>
What are best practices...

Of course, no procedure can be considered "best" for every situation.  Many of the particular choices we make for this lab can be done differently just as well or better.  But we hope to present a concrete example that we think is broadly useful for many small to medium sized Python applications....
<hr>
</details>

<details><summary>Directory Layout for a Python Project</summary>
<hr>

## Directory Layout for a Python Project

Many factors can influence the final structure of a Python app including: underlying framework (such as web applications), deployment context (some environments require special files or directories) and conventions of various libraries that may be used in the application.

For our purposes, I'll be presenting a structure that can apply to most small to medium Python applications, that are not subject to special conditions.

### Example Layout
```
myreponame
|---docs/
|   |---mypackage.md      
|---src/
|   |---myapp/
|      |---__init__.py
|      |---app.py  
|      |---myfirstpackage
|      |   |---__init__.py
|      |   |---myfirstpackage.py
|      |   |---helpers.py
|---test/
|   |---myfirstpackage/
|   |   |---test_myfirstpackage.py
|   |   |---test_helpers.py
|---data/
|---LICENSE
|---README.md
|---requirements.txt
|---setup.py
|---.gitignore
```

Here we have proposed and application called "myapp" that contains an internal package called "myfirstpackage".  Around that app we have a number of files and directories that might be familiar and we'll discuss each in turn as we go.
<hr>
</details><br>

## Getting Started
I'll start with the basics and explain the purpose of each element.  At the end you will have created a working python application with an internal package and learned several "best practices" that can benefit you and your collaborators for years to come.

So let's get started!

<hr>
<h3 align="center">Keep reading below to find your first task</h3>
