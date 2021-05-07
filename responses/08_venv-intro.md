### Virtual Environments

Oftentimes, your python application will use packages and modules that are not part of the standard library. In our course, the source code requires installation of numerous packages to run successfully, with the most notable one being TensorFlow and NumPy. Since these packages have to be installed first, at the moment you will not be able to run your code locally.

The next two steps in this course will show you a series of steps you can take to install external packages using virtual environments and the setup script you just wrote. There are a number of ways to do this but we will be presenting you what is considered best practice as that is the purpose of this course.

As mentioned earlier, your python application uses packages and modules that are not part of the Python standard library. As a result, you'll have to find a way to install these packages somewhere. We could technically install these globally (i.e. as part of a system-wide Python), but that is not best practice. 

As exeternal packages and modules are updated constantly, some older applications might fail to run on more recent versions and some older ones might fail on older versions. Imagine that you are working on two seperate python applications and application A only runs only on version 1.8.0 for NumPy, and application B runs only on version 1.17.0. It would be quite a pain to install and reinstall a specific version for NumPy when you have to switch between projects.

In order to avoid this, we encourage that you create virtual environments that essentially contains installations of a particular version of Python or any additional packages and modules for a project you are working on. Going back to our example, you can install NumPy 1.8.0 for one virtual environment and NumPy 1.17.0 for the other virtual environment.

The next few steps will show you how to create virtual environments and install specific versions of a package for that virtual environment.

## Step 9: Activate a Virtual Environment 

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
