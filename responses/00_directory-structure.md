<!-- GETTING STARTED -->
## Getting Started: Directory Layout

There are many ways to structure a python application.  Many factors can influence the final structure including: underlying framework (such as web applications), deployment context (some environments require special files or directories) and conventions of various libraries that may be used in the application.

Most applications, that are not subject to special conditions, can benefit from a repository setup similar to the following:

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

We'll start with the basics and explain the purpose of each element as we go.  At the end we'll have a working python application with an internal package.

So let's get started!  

Check the comment below for the first step.