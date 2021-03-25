# Virtual Environments and Pip Install
### Virtual Environments

Oftentimes, your python application will use packages and modules that are not part of the standard library. As these packages and modules would be updated constantly, some older applications might fail to run on more recent versions and some older ones might fail on older versions.

In order to resolve this, you can create virtual environments that essentially contains installations of a particular version of Python or any additional packages and modules. If app A uses version 1.0.0 of the 'numpy' package and app B uses version 2.0.0 of the same package, you can create a install v1.0.0 numpy for one virtual environment and v2.0.0 numpy for the other virtual environment.

In our course, the source code requires installation of numerous packages to run successfully, with the most notable one being TensorFlow. The next few steps will show you how to create virtual environments and install specific versions of a package for that virtual environment.
## Step 5: Activate a Virtual Environment 

There are two main ways you can create virtual environments. One is using a Python module called venv and the other is using a package manager called conda. Python virtual environments and Conda environments do have differences but for the purposes of this course, either should work. So if you already have Anaconda, you can use conda.

### :keyboard: Activity: Create and Activate a Virtual Environment

If you are using venv,
1. Run ```python3 -m venv my-env```. This will create the virtual environment.
Now, to activate the virtual environment,
On Windows, run:
2. ```my-env\Scripts\activate.bat```
On Unix or MacOS, run:
2. ```source my-env/bin/activate```

If you are using conda,
1. Run ```conda create --name myenv```. This will create the virtual environment.
2. When conda asks you to proceed, type y: ```proceed ([y]/n)?```
3. Run ```conda activate myenv```

</details>
<hr>
<h3 align="center">Watch below this comment for my response</h3>

> _Sometimes I respond too fast for the page to update! If you perform an expected action and don't see a response from me, wait a few seconds and refresh the page for your next steps._
