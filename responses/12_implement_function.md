## Step 14: Implement MINIST classifier 
Almost done! Let's now implement the MNIST classifier. Since we don't want to go too much into Tensorflow, just read through the 'Make Predictions' section of the [documentation](https://www.tensorflow.org/tutorials/keras/classification#make_predictions) before starting the activity. We expect you to essentially use the same code with minor adjustments as we want the model to classify a single image and return the label.

### :keyboard: Activity: Implement classify_image

**:bulb: [Go to `src/digit_reader/model/model.py`]({{quicklink1}})**

1. Note that ```probability_model.predict(test_images)``` takes in an numpy array of images as an input. If you don't know about numpy arrays don't worry about it it's basically a Python array that allows for efficient computation. 
2. To create a numpy array from a list, we can do ```np.array(some_list)```. Since we are given a single image, make a list with one element, and send in the numpy array of the image as a parameter for ```probability_model.predict()```.
3. As shown in the documentation, ```np.argmax(predictions[0])``` will return the most likely label which the first image in the list belongs to. Your function should return the value obtained by ```np.argmax(predictions[0])``
4. Once you complete implementing ```classify_image```, run ```pytest -v -k test_classify_image``` and check whether you pass the test.

<details><summary>If you are stuck, here is the solution.</summary>
  
```  
def classify_image(self, image):
  probability_model = keras.Sequential([self.model, keras.layers.Softmax()])
  predictions = probability_model.predict(np.array([image]))
  return np.argmax(predictions[0])
```        

</details>

Now that everything is ready let's wrap everything up in our final step.
