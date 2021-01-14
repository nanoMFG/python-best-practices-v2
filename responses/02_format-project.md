# Installing and running the Black auto-formatter

## Installing and intro
The black auto-formatter can be installed by running

        pip install black

You can consult [Black's documentation](https://black.readthedocs.io/en/stable/)
for more information on running it, but for most cases it will be sufficient to
simply run:

        black myfile.py

This will auto-format the contents of myfile.py, and insert the result back into
the file, overwriting what was there before.

## Running

The file we want to format in this step is inside a package, but we can still
call black the same way. Go ahead and run this command:

        black mnist_example/mnist_convnet.py

After the formatter has finished, commit the result, and check back here.
