#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importing Core Libraries 
#import pandas as pd
#dataset = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv')
#print(dataset)

dataset = [['sunny','hot','high','FALSE','no'],
           ['sunny','hot','high','TRUE','no'],
           ['overcast','hot','high','FALSE','yes'],
           ['rainy','mild','high','FALSE','yes'],
           ['rainy','cool','normal','FALSE','yes'],
           ['rainy','cool','normal','TRUE','no'],
           ['overcast','cool','normal','TRUE','yes'],
           ['sunny','mild','high','FALSE','no'],
           ['sunny','cool','normal','FALSE','yes'],
           ['rainy','mild','normal','FALSE','yes'],
           ['sunny','mild','normal','TRUE','yes'],
           ['overcast','mild','high','TRUE','yes'],
           ['overcast','hot','normal','FALSE','yes'],
           ['rainy','mild','high','TRUE','no']]
# Preprocessing 


# Spliting the dataset into trainingset and testset
# The testset will be made up of 25% of teh rows
split =int(round(14 * .30))

training_dataset =dataset[split:][:]
test_dataset = dataset[:split][:]

# Separating by Class

def separate_by_class(dataset):
    separated = dict()
    for i in range (len(dataset)):
        vector = dataset[i]
        class_value = vector[-1]
        if (class_value not in separated):
            separated[class_value] = list()
        separated[class_value].append(vector)
    return separated


#Displaying the separated classes
separate = separate_by_class(list(training_dataset))
for label in separate:
  print(label)
  for row in separate[label]:
    print(row)
    
# Summarized dataset stat
# Simple stat that will help in the calculation of standard dev
# 1 Calacutation of mean
def mean_value(value):
  mean_value = sum(value)/float(len(value))
  return mean_value

# 2. Calculation of standard dev
from math import sqrt
def standard_dev_value(value):
  stv = sqrt(sum([(mean_value(value)-x) for x in value])/(float(len(value))-1))
  return stv
value = [2,3,4,5]

# statistics for all colunme