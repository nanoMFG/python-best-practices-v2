# First Python files

The first actual python file we are going to add is an \_\_init\_\_.py. This file is what defines a module, and should be placed in the module directory.

### Directory Structure

The \_\_init\_\_.py needs to be placed in the directory that contains the rest of the module code. This will usually be the directory named like the module, i.e. if your module is named 'hello,' you would create the file src/hello/\_\_init\_\_.py.  

We have introduced here the convention of an additional `src` directory.  This separates the top application directory. A best practice is to install the application before running it.  Not running in source directories also helps keep the source tree clean by avoiding creation of extra files and directories like `__pycache__` in the source tree.

## Step 4: Create an \_\_init\_\_.py

To setup the module, we need to create two `__init__.py` files, one for the 'digit_reader' package, and one for its internal 'model' package.

### :keyboard: Activity: Commit your \_\_init\_\_.py's

1. Commit a blank \_\_init\_\_.py for the 'digit_reader' module
2. Commit a blank \_\_init\_\_.py for the 'digit_reader/model' module
3. Open a pull request to main with your changes

**:bulb: [Add `src/digit_reader/__init__.py`]({{quicklink1}})**
**:bulb: [Add `src/digit_reader/model/__init__.py`]({{quicklink2}})**

> _I will respond in the pull request one you open it!_ 
