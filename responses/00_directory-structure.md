<!-- GETTING STARTED -->
# :wave: Welcome to "Python Project Best Practices 

To get started, I'll guide you through some background on what the term "best practices" means and why we need them.
Then I'll show you a particular set of best practices and how they apply to a modest Python-based machine learning
app.

:point_down: _This arrow means you can expand the window! Click on them throughout the course to find more information.
<details><summary>What are Best Practices?</summary>
<hr>
What are best practices...
<hr>
</details>

<details><summary>Directory Layout for a Python Project</summary>
<hr>

## Directory Layout for a Python Project

There are many ways to structure a python application.  Many factors can influence the final structure including: underlying framework (such as web applications), deployment context (some environments require special files or directories) and conventions of various libraries that may be used in the application.

For our purposes, I'll be presenting a structure that can apply to most small to medium Python applications, that are not subject to special conditions.

### Example Layout
```
myreponame
|---docs/
|   |---mypackage.md      
|---myapp/
|   |---__init__.py
|   |---myfirstpackage
|   |   |---__init__.py
|   |   |---myfirstpackage.py
|   |   |---helpers.py
|---tests/
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

Here we have proposed and application called "myapp" that contains an internal package called "myfirstpackae".  Around that app we have a number of files and directories that might be familiar.
<hr>
</details><br>

## Getting Started
I'll start with the basics and explain the purpose of each element as we go.  At the end you will have created a working python application with an internal package and learned several "best practices" that can benefit you and your collaborators for years to come.

So let's get started!

<hr>
<h3 align="center">Keep reading below to find your first task</h3>