"""
Step 1 - Load Data

This next hidden cell will import some libraries and set up our data pipeline. We have a training split called ds_train and a validation split
called ds_valid.
"""
# Importing Libraries
import os, warnings
import matplotlib.pyplot as plt
from matplotlib import gridspec

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory


# Reproducibility
def set_seed(seed=31415):
    np.random.seed(seed)
    tf.random.set_seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    os.environ['TF_DETERMINISTIC_OPS'] = '1'


set_seed(31415)

# Set Matplotlib default
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large', titleweight='bold', titlesize=18, titlepad=10)
plt.rc('image', cmap='magma')
warnings.filterwarnings('ignore')

# Load Training and validation sets
ds_train_ = image_dataset_from_directory('./inputs/train', labels='inferred', label_mode='binary', image_size=[128, 128], interpolation='nearest',
                                         batch_size=64, shuffle=True)
ds_valid_ = image_dataset_from_directory('./inputs/valid', labels='inferred', label_mode='binary', image_size=[128, 128], interpolation='nearest',
                                         batch_size=64, shuffle=False)


# Data Pipeline
def convert_to_float(image, label):
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    return image, label


AUTOTUNE = tf.data.experimental.AUTOTUNE

ds_train = (ds_train_
            .map(convert_to_float)
            .cache()
            .prefetch(buffer_size=AUTOTUNE)
            )

ds_valid = (ds_valid_
            .map(convert_to_float)
            .cache()
            .prefetch(buffer_size=AUTOTUNE)
            )

"""
Step 2 - Define Pre-trained Base

The most commonly used dataset for pre-training is ImageNet, a large dataset of many kind of natural images. 
Keras includes a variety models pre-trained on ImageNet in its applications module. The pre-trained model we'll use is called InceptionV1 .
"""

# Getting the pre-trained base (VGG16)
pretrained_base = tf.keras.models.load_model('./inputs/cv-course-models/inceptionv1')
pretrained_base.trainable = False
"""Reason for False
When doing transfer learning, it's generally not a good idea to retrain the entire base at least not without some care. 
The reason is that the random weights in the head will initially create large gradient updates, which propogate back into the base layers and destroy 
much of the pretraining. Using techniques known as fine tuning it's possible to further train the base on new data, but this requires some care to do well.
"""

"""
Step 3 - Attach Head

Next, we attach the classifier head. For this example, we'll use:
1. a layer of hidden units (the first Dense layer) 
2. a layer to transform the outputs to a probability score for class 1, Truck. 
3. The Flatten layer transforms the two dimensional outputs of the base into the one dimensional inputs needed by the head.
"""
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    pretrained_base,
    layers.Flatten(),
    layers.Dense(6, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

"""
Step 4 - Train

Finally, let's train the model. Since this is a two-class problem, we'll use the binary versions of crossentropy and accuracy. 
The adam optimizer generally performs well, so we'll choose it as well.
"""
optimizer = tf.keras.optimizers.Adam(epsilon=0.01)
model.compile(optimizer=optimizer,
              loss='binary_crossentropy',
              metrics=['binary_accuracy'])

history = model.fit(ds_train,
                    validation_data=ds_valid,
                    epochs=30)
"""
When training a neural network, it's always a good idea to examine the loss and metric plots. 
The history object contains this information in a dictionary history.history. 
We can use Pandas to convert this dictionary to a DataFrame and plot it with a built-in method.
"""
import pandas as pd

history_frame = pd.DataFrame(history.history)
history_frame.loc[:, ['loss', 'val_loss']].plot()
history_frame.loc[:, ['binary_accuracy', 'val_binary_accuracy']].plot();

"""
Conclusion
In this lesson, we learned about the structure of a convnet classifier: 
a head to act as a classifier atop of a base which performs the feature extraction.
The head, essentially, is an ordinary classifier like you learned about in the introductory course.
 For features, it uses those features extracted by the base. 
 This is the basic idea behind convolutional classifiers: that we can attach a unit that performs feature engineering to the classifier itself.

This is one of the big advantages deep neural networks have over traditional machine learning models: given the right network structure, 
the deep neural net can learn how to engineer the features it needs to solve its problem.
"""