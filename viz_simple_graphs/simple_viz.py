# Importing Core libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sbn 

#Importing the dataset 
file_path = './cereals.csv'
dataset = pd.read_csv(file_path)

# Visualising the dataset 
print('This is the cereals dataset:\n',dataset)

# Visualising thr diffrent data types for the columns
print('Columns Datatypes: \n',dataset.dtypes)

# Visualizing Histogram of the the Columns (Object Columns)
dataset=dataset.drop(['Cereal'],axis=1)
object_cols = [cols for cols in dataset.columns if dataset[cols].dtypes=='object']
for col in object_cols:
    dataset[col].value_counts().plot.bar(title='A Histogram of '+col)
    plt.show()

# Visualizing Distribution of Numerical colunms
num_cols = dataset.drop(object_cols,axis=1)
for col in num_cols:
    #np.array([col]).astype(np.float)
    sbn.distplot(dataset[col].values,hist=True,rug=True)
    plt.title('Distribution graphs '+col)
    plt.show()

#Visualizing Scatter Plot of the Numerical Colunms
# 1 Hue = Manufacturer
for col_X in num_cols:
    for col_y in num_cols:
        sbn.scatterplot(x=dataset[col_X],y=dataset[col_y],hue=dataset['Manufacturer'])
        plt.show()

g = sbn.PairGrid(dataset,hue='Manufacturer')
g.map(plt.scatter)
plt.show()

for col_X in num_cols:
    for col_y in num_cols:
        sbn.relplot(x=col_X,y=col_y, hue="Manufacturer", size="Weight",sizes=(40, 400), alpha=.5, palette="muted",height=6,data=dataset)
        plt.show()
# 2 Hue 
for col_X in num_cols:
    for col_y in num_cols:
        sbn.scatterplot(x=dataset[col_X],y=dataset[col_y],hue=dataset['Type'])
        plt.show()

g = sbn.PairGrid(dataset,hue='Type')
g.map(plt.scatter)
plt.show()

for col_X in num_cols:
    for col_y in num_cols:
        sbn.relplot(x=col_X,y=col_y, hue="Type", size="Weight",sizes=(40, 400), alpha=.5, palette="muted",height=6,data=dataset)
        plt.show()

