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

