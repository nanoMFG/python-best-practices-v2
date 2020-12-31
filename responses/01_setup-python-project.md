If you have ever been on GitHub, you must have noticed that a regular project’s structure looks like this:

docs/conf.py
docs/index.rst
module/__init__.py
module/core.py
tests/core.py
LICENSE
README.md
requirements.txt
setup.py

License
This is in the root directory and is where you should add a license for your project. In the repo you will have an option to add an MIT liscense. 

README
This is in the root directory too and is where you describe your project and what it does.

You can write this in Markdown, reStructuredText, or plain text.

Module Code
This holds your actual code that may be inside a subdirectory or inside root.

requirements.txt
This is not mandatory, but if you use this, you put it in the root directory.

Here, you mention the modules and dependencies of the project- the things it will not run without.

In your repository, firstly create a License and a README. Then, create a new module directory and move the existing Python code to the directory. After you are finished, commit your changes to move on to the next step.

***NOTE: IF YOU COMMIT AN INVALID README/LISENCE FILE, WE WILL COMMENT ON THIS ISSUE AND PREVENT YOU FROM MOVING ON.

For testing purposes, write in your README file and actually make a LICENSE file with nanoMFG instead of your github username
