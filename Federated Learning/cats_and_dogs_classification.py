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

# Freeezing the base Model
base_model.trainable = False

# Define the Custome Head
print(base_model.output)
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()(base_model.output)
print(global_average_layer)
output_layer = tf.keras.layers.Dense(units = 1,activation = 'sigmoid')(global_average_layer)

# Creating the Model (Model = base_model + output_layer)
model = tf.keras.Model(inputs=base_model.input, output = output_layer)
model.summary

#Compliling the Model
model.compile(optimizer = tf.keras.optimizer.RMSProp(l_r=0.0001),loss = 'binary_crossentropy',metric = ['accuracy'])

# Image Generation
data_gen_train = ImageDataGenerator(rescale = 1/255.)
train_generator = data_gen_train.flow_from_directory(train_dir,target_size = (128,128),
                                                   batch_size = 128, class_mode = 'binary')
data_gen_test = ImageDataGenerator(rescale = 1/255.)
test_generator = data_gen_test.flow_from_directory(test_dir,target_size = (128,128),
                                                   batch_size = 128, class_mode = 'binary')

# Training the Model
model.fit_generator(train_generator,epoch=5,validation_data = test_generator)