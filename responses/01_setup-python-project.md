<!-- ABOUT THE PROJECT -->
## About The Project
This project will introduce basic skills for building up a Python project and good habits to follow while developing it.  A common directory structure and its purpose will be presented along with a number of what we consider to be "best practices".  
Of course, no practice can be considered "best" for every situation.  Many of the particular choices we make for this lab cna be done differently just as well.  But we hope to present a concrete example with particular choices that we think are broadly useful for most small to medium applications.

This is intended to be a stepping stone for modest python applications away from monolithic single scripts, or cluttered notebooks and toward code that is more maintainable, easier to read, easier to test and install and ultimately easier for **others** to use and contribute to.


where the primary functions are collected into a python [module file](https://docs.python.org/3/tutorial/modules.html) within a simple [package]()

<!-- ### Built With Not sure wha to put here yet -DA -->

<!-- GETTING STARTED -->
## Getting Started: Directory Layout

If you have ever been on GitHub, you must have noticed that a regular project’s structure looks like this:

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
<!--
### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python3 
  ```sh
  brew install python
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/python-best-practices-v1.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```

## Modules
This holds your actual code that may be inside a subdirectory or inside root.


## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This is in the root directory and is where you should add a license for your project. In the repo you will have an option to add an MIT liscense. 
Distributed under the MIT License. See `LICENSE` for more information.

## requirements.txt
This is not mandatory, but if you use this, you put it in the root directory.

Here, you mention the modules and dependencies of the project- the things it will not run without.

In your repository, firstly create a License and a README. Then, create a new module directory and move the existing Python code to the directory. After you are finished, commit your changes to move on to the next step.

***NOTE: IF YOU COMMIT AN INVALID README/LISENCE FILE, WE WILL COMMENT ON THIS ISSUE AND PREVENT YOU FROM MOVING ON.

For testing purposes, write in your README file and actually make a LICENSE file with nanoMFG instead of your github username
-->