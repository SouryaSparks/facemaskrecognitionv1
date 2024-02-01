import tensorflow as tf
import cv2 
import numpy as np
import os
import time
import sys
import matplotlib.pyplot as plt


# This loads in the model

# os.path.join is useful for using different pathways in a directory
model_dir = os.path.join('models','model.h5')

# The load_model() method takes in a pathway as an argument and loads the model if that path leads to a model 
model = tf.keras.models.load_model(model_dir)

# sys.argv allows arguments to be passed through the command prompt, the variable is a list containing two items, the second item of that list is the file name 
args_passed = sys.argv
image_name = args_passed[1]

try:
    img = cv2.imread(image_name)

    # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # plt.show()

    os.system(image_name)

except:
    Exception('image does not exist!')


