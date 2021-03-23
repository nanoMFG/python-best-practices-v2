### Pip

Now that you are in a virtual environment, let's talk about pip. Pip or the package installer for Python can be used to install packages from the Python Package Index and other indexes. In essence, you get to install powerful packages created by other people.

In this course, you will be using two widely used packages called numpy and tensorflow among other packages. As a result, you will have to install them in your virtual environment. You can install these packages manually but in this course, we will show you how to do them automatically using 
'''
pip install -r requirements.txt
'''
so you don't have to manually install all packages.

### Requirements.txt

In order to support the automatic installation of packages, you will first need a requirements.txt file that contains all packages that would have to be installed for the package to run. You could technically manually create a requirments.txt file but that would just be silly.

Luckily, we have a setup build script so we can use that to generate our build script. However, we'll first have to add 2 fields into our setup function to make that possible!

## Step 7: Pip install and Requirements.txt

There are two main ways you can create virtual environments. One is using a Python module called venv and the other is using a package manager called conda. Python virtual environments and Conda environments do have differences but for the purposes of this course, either should work. So if you already have Anaconda, you can use conda.

### :keyboard: Activity: Create and Activate a Virtual Environment

If you are using venv,
1. Run 'python3 -m venv my-env'. This will create the virtual environment.
Now, to activate the virtual environment,
On Windows, run:
2. 'my-env\Scripts\activate.bat'
On Unix or MacOS, run:
2. 'source my-env/bin/activate'

If you are using conda,
1. Run 'conda create --name myenv'. This will create the virtual environment.
2. When conda asks you to proceed, type y: 'proceed ([y]/n)?'
3. Run 'conda activate myenv'