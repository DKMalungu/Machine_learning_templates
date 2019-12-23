#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
#############Recurrent Neural Network with TF 2.0 #############################
#%%
# Importing Core libraries
import tensorflow as tf
from tensorflow.keras.datasets import imdb
#%%
# Data Preprocessing 
#%%
## 1.Setting up the data paramenters
number_of_words = 20000
max_len = 100
#%%
## 2. Loading the dataset from keras
(X_train,y_train),(X_test,y_test) = imdb.load_data(num_words=number_of_words)
#%%
## 3. Padding all sequences to be the same length
X_train = tf.keras.preprocessing.sequence.pad_sequences(X_train,maxlen = max_len)
X_test = tf.keras.preprocessing.sequence.pad_sequences(X_test,maxlen = max_len)
#%%
# Building the Recurrent Neural Network
#%%
## 1. Initializing the model
model = tf.keras.Sequential()
#%%
## 2. Adding the embeddeing layer
embed=128
model.add(tf.keras.layers.Embedding(number_of_words,embed,input_shape = (X_train.shape[1],)))
#%%
## 3 Adding LSTM Layer
model.add(tf.keras.layers.LSTM(units=128,activation = 'tanh'))
#%%
## 4. Adding the output layer
model.add(tf.keras.layers.Dense(units=1,activation='sigmoid'))
#%%
# Compiling the Model
model.compile(optimizer = 'rmsprop',loss = 'binary_crossentropy',metrics = ['accuracy'])
#%%
#Model Summary
model.summary()
#%%
# Training the Model
model.fit(X_train,y_train,epochs = 5,batch_size = 128)
#%%
#Model Evaluation
test_loss,test_accuracy = model.evaluate(X_test,y_test)
print(accuracy)
#%%
