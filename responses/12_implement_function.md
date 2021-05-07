## Step 14: Implement MINIST classifier 
Almost done! Let's now implement the MNIST classifier. Since we don't want to go too much into Tensorflow, just read through the 'Make Predictions' section of the [documentation](https://www.tensorflow.org/tutorials/keras/classification#make_predictions) before starting the activity. We expect you to essentially use the same code with minor adjustments as we want the model to classify a single image and return the label.

### :keyboard: Activity: Implement classify_image

**:bulb: [Go to `src/digit_reader/model/model.py`]({{quicklink1}})**

1. Copy paste the following code to `model.py`. You can leave the doc strings but it's okay to replace everything you have with what we provide.

```python
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from digit_reader.model.helpers import num_classes, input_shape

class MNISTModel:
    def __init__(self):
        """Create initial model and print summary"""
        self.model = keras.Sequential(
            [
                keras.Input(shape=input_shape),
                layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
                layers.MaxPooling2D(pool_size=(2, 2)),
                layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
                layers.MaxPooling2D(pool_size=(2, 2)),
                layers.Flatten(),
                layers.Dropout(0.5),
                layers.Dense(num_classes, activation="softmax"),
            ]
        )
        self.model.summary()

    def train_model(self, x_train, y_train, epochs=5):
        """Train the model with specified training data
        Args:
            x_train: MNIST images training set
            y_train: MNIST image labels training set
        """
        batch_size = 128
        self.model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
        self.model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

    def evaluate_model(self, x_test, y_test):
        """Evaluate the model and return the score
        Returns:
            A tuple containing the loss and accuracy
        """
        score = self.model.evaluate(x_test, y_test, verbose=0)
        print("Test loss:", score[0])
        print("Test accuracy:", score[1])
        return score
    
    def classify_image(self, image):
        """Make predictions on what the label is for a given image
        Returns:
            A label integer which the image most likely belongs to
        """
```

2. Create a probability model as shown in the link. Note that instead of doing we are already importing `keras` from `tensorflow`
2. Note in the link that ```probability_model.predict(test_images)``` takes in an numpy array of images as an input. If you don't know about numpy arrays don't worry about it it's basically a Python array that allows for efficient computation. 
3. To create a numpy array from a list, we can do ```np.array(some_list)```. Since we are given a single image, make a list with one element, and send in the numpy array of the image as a parameter for ```probability_model.predict()```.
4. As shown in the documentation, ```np.argmax(predictions[0])``` will return the most likely label which the first image in the list belongs to. Your function should return the value obtained by ```np.argmax(predictions[0])``
5. Once you complete implementing ```classify_image```, run ```pytest -v -k test_classify_image``` and check whether you pass the test.

<details><summary>If you are stuck, here is the solution.</summary>
  
```  
def classify_image(self, image):
  probability_model = keras.Sequential([self.model, keras.layers.Softmax()])
  predictions = probability_model.predict(np.array([image]))
  return np.argmax(predictions[0])
```        

</details>

Now that everything is ready let's wrap everything up in our final step.
