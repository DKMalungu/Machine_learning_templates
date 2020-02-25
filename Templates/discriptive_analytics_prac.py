# Importing core libraries
import pandas as pd
import numpy as np

# Importing dataset intp python
file_path='./carpurchase_factors.csv'
dataset=pd.read_csv(file_path)

# Measures of Cetral Tendancy

# 1. Count
column_count=dataset.count()
print('Count of all elements in a columns: ',column_count)

# 2. Sum
column_sum = dataset.sum()
print('Sum of all columns: ',column_sum)

# 3. Mean
column_mean=dataset.mean()
print('Mean of all columns: ',column_mean)

# 4. Mode
column_mode=dataset.mode()
print('Model of all the colunms: ',column_mode)

# 5 Median
column_median=dataset.median()
print('Median off all the columns: ',column_median)

# Measure of Dispersion

# 1. Range
## Min
column_min= dataset.min()
print('The minimum values in the column: ',column_min)

## Max
column_max=dataset.max()
print('This highest value in the column: ',column_max)

#Range
column_range=column_max-column_min
print('The range of each column: ',column_range)

# 2. InterQuartile range
## 1st Quarter
q1 = dataset.quantile(0.25)
print('The 1st Quartile: \n',q1)
## 2nd Quarter
q2 = dataset.quantile(0.5)
print('The 2nd Quartile: \n',q2)
## 3rd Quarter
q3 = dataset.quantile(0.75)
print('The 3rd Quartile: \n',q3)
## IQR
column_iqr=q3-q2
print('The Inter Quartile Range in each columns: \n',column_iqr)

# 3. Variance
column_var=dataset.var()
print('The variance of columns: \n',column_var)

# 4. Standard Deviation
column_std=dataset.std()
print('The Standard Deviation of each columns: \n',column_std)

#5 Describe
column_des=dataset.describe()
print('The basic description: \n',column_des)

# Measure of Relationship
## 1 Covariance Coefficient
cova_coff=dataset.cov()
print('This is the covarance of the dataset: ',cova_coff)

## 2. Correlation Coefficient
corr_coff = dataset.corr()
print('This is the Correlation of the dataset: ',corr_coff)
