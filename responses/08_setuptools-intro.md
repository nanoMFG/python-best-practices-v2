### Setuptools

Now that you have all the files needed to create a Python package and organized your code into modules, it's time to build our package so that so that the various commands that operate on your modules can do the right thing!

The Python distutils package provides support for building and installing additional modules into a Python installation. However, we don't want to use this module directly. Instead we will use setuptools, a collection of enhancements to the Python distutils that allow you to more easily build and distribute Python distributions.

## Step 8: Setup.py

The build script for setuptools is written in the file setup.py. For this step of the course, we will ask you to create a new setup.py file and write the build script.

### :keyboard: Activity: Create setup.py 

**:bulb: [Add `setup.py`]({{quicklink1}})**

1. Create the file ```setup.py```
2. Import setuptools and create an empty call for setup.
```python
import setuptools

setuptools.setup()
```
3. Write the name of the package, version, your name and email, and description like below.
```python
import setuptools

setuptools.setup(
    name="example_package-username", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package"
)
```
4. If you want you could add a field for ```long_description``` and set your ```README.md``` file as your content like this.
```python
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_package-username", # Replace with your own username
    ...
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown"
)
```
5. Later on when you want to import from the modules you create, you will have to access the files in model.py. However, since they are in a `/src` directory, we need to add two lines `package_dir={'': 'src'}` and  `packages=setuptools.find_packages(where='src')` to access files in the package directory.

```python
...
setuptools.setup(
    name="example_package-username", # Replace with your own username
    ...
    long_description_content_type="text/markdown"
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    ...
)
```
7. In later steps of the course, we will ask you to add additional fields to the setup build script. For now, commit the new setup.py file and move on to the next step!

If you get stuck, or don't feel like typing, you can click the dropdown below for the solution code. Feel free to copy and paste it.
<details><summary> A completed setup.py </summary>
    
```python
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="mnist_example-nanoMFG", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)
```
</details>
<hr>
<h3 align="center">Watch below this comment for my response</h3>

> _Sometimes I respond too fast for the page to update! If you perform an expected action and don't see a response from me, wait a few seconds and refresh the page for your next steps._
