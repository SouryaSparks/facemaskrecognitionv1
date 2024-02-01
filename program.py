import tensorflow as tf
import cv2 
import numpy as np
import os
import time

# This loads in the model

# os.path.join is useful for using different pathways in a directory
model_dir = os.path.join('models','model.h5')

# The load_model() method takes in a pathway as an argument and loads the model if that path leads to a model 
model = tf.keras.models.load_model(model_dir)



