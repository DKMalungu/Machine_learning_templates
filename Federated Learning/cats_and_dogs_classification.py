#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Downloading (Getting the dataset)
import wget
url = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
wget.download(url)

#Importing core libraries
import os
import zipfile
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#Extracting The Zipfile
dataset_path = ('./cats_and_dogs_filtered.zip')
zip_object = zipfile.ZipFile(file = dataset_path,mode='r')
zip_object.extractall()

#Defination of dataset path
dataset_path = ('./cats_and_dogs_filtered/')
train_dir = os.path.join(dataset_path,'train')
test_dir = os.path.join(dataset_path,'validation')

#Loading the MobileNet V2 model
img_shape = [128,128,3]
base_model = tf.keras.applications.MobileNetV2(input_shape = img_shape, include_top = False,
                                               weights = 'imagenet')
base_model.summary()