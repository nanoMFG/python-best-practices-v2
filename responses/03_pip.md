### Pip

Now that you are in a virtual environment, let's talk about pip. Pip or the package installer for Python can be used to install packages from the Python Package Index and other indexes. In essence, you get to install powerful packages created by other people.

In this course, you will be using two widely used packages called numpy and tensorflow among other packages. As a result, you will have to install them in your virtual environment. You can install these packages manually but in this course, we will show you how to do them automatically using 
'''
pip install -r requirements.txt
'''
so that you don't have to manually install all packages.

### Requirements.txt

In order to support the automatic installation of packages, you will first need a requirements.txt file that contains all packages that would have to be installed for the package to run. You could technically manually create a requirments.txt file but that would just be silly.

Luckily, we have a setup build script so we can use that to generate our build script. However, we'll first have to add 2 fields into our setup function to make that possible!

## Step 7: Edit setup.py and install with pip

As mentioned earlier, our project will use numpy and tensorflow and tensorflow actually requires your Python version to be 3.6-3.8. So, we would have to write that in our build script. Here's some example values for python_requires and install_requires. The following example project requires a Python version above 3.0 and requires installation of django and pandas. Use the example setup.py as an example for your project's setup.py.
'''
setuptools.setup(
    name="example_package-username", # Replace with your own username
    ...
    packages=setuptools.find_packages(),
    python_requires='>=3.0',
    install_requires=[
        'django',
        'pandas'
    ]
'''

Once your setup.py is complete, we can run a few commands to install everything you need for your project.
### :keyboard: Activity: From setup.py to pip install 

1. Commit the setup.py file after adding values for the python_requires and install_requires field
2. Run 
'''
pip-compile
'''
This should create a requirements.txt file. If it's failing, check if there's any problems with your setup.py
3. Run pip install -r requirements.txt

You should now be ready to run some tests for your project. Merge the pull request and we will let you know if you are good to go!