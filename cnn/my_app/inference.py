import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import mnist

# Load the pre-trained model
model = tf.keras.models.load_model('/app/mnist_cnn_model.h5')

# Load the MNIST dataset for testing
(_, _), (x_test, y_test) = mnist.load_data()

# Preprocess a single image from the test set
x_test = x_test / 255.0  # Normalize pixel values
x_test = x_test[..., tf.newaxis]  # Add channel dimension (28, 28, 1)

# Perform inference on one sample
sample_image = x_test[0:1]  # Take the first image from the test set
prediction = model.predict(sample_image)
predicted_class = np.argmax(prediction, axis=1)

print(f"Predicted class for the test image: {predicted_class[0]}")
