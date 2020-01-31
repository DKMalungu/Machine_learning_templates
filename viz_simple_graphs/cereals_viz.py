# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ENSz6KUUaoN3aBqVV_f0ZEUrDLM2wZWG
"""

# Importing core libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

"""# **Content**

## Fields in the dataset:

   1. Name: Name of cereal
   1. mfr: Manufacturer of cereal
       * A = American Home Food Products
       * G = General Mills
       * K = Kelloggs
       * N = Nabisco
       * P = Post
       * Q = Quaker Oats
       * R = Ralston Purina 
   1. type:
        * cold
        * hot 
   1. calories: calories per serving
   1. protein: grams of protein
   1. fat: grams of fat
   1. sodium: milligrams of sodium
   1. fiber: grams of dietary fiber
   1. carbo: grams of complex carbohydrates
   1. sugars: grams of sugars
   1. potass: milligrams of potassium
   1. vitamins: vitamins and minerals - 0, 25, or 100, indicating the typical percentage of FDA recommended
   1. shelf: display shelf (1, 2, or 3, counting from the floor)
   1. weight: weight in ounces of one serving
   1. cups: number of cups in one serving
   

### Acknowledgements

These datasets have been gathered and cleaned up by Petra Isenberg, Pierre Dragicevic and Yvonne Jansen. The original source can be found here

This dataset has been converted to CSV

Inspiration

The rise of non-communicable disease (NCD) has been attributed to the poor nutrition in most of the common cerials at the market place.
Question:

1. Amount of Protein, Carbonhydrate and Fat for Each Cereals #LINE CHART AND FILLED AREA PLOT
1. Amount of Protein and Fiber for Each Cereal #SCATTER CHART
1. Amount of Calori in the Top 3 Cereal According to Rating Score #BAR PLOT
"""

# Importing dataset into pyhton
file_path = '/content/cereals.csv'
dataset = pd.read_csv(file_path)

# Displaying the dataset as is:
print(dataset)

# Droping colunms
dataset = dataset.drop('Cereal',axis=1)
print(dataset)

dataset.dtypes

# Amount of Protein, Carbohydrates and Fat for Each Cereals Hue = Type
g = sbn.PairGrid(dataset[['Protein','Carbohydrates','Fat','Type']],hue='Type',)
g.map(plt.scatter)
plt.show()

# Amount of Protein, Carbohydrates and Fat for Each Cereals Hue = Type
g = sbn.PairGrid(dataset[['Protein','Carbohydrates','Fat','Manufacturer']],hue='Manufacturer',)
g.map(plt.scatter)
plt.legend()
plt.show()

# Amount of Protein and Fiber for Each Cereal
plt.scatter(x='Protein',y='Fiber',data=dataset)
plt.show()

# Examing the different Nutrients and shelf placement
fig, axs = plt.subplots(3,3,constrained_layout=True)

axs[0, 0].bar(x='Shelf',height='Protein',data=dataset)
axs[0, 0].set_title('Protein', fontsize=10)

axs[0, 1].bar(x='Shelf',height='Fat',data=dataset)
axs[0, 1].set_title('Fat', fontsize=10)

axs[0, 2].bar(x='Shelf',height='Sodium',data=dataset)
axs[0, 2].set_title('Sodium', fontsize=10)

axs[1, 0].bar(x='Shelf',height='Fiber',data=dataset)
axs[1, 0].set_title('Fiber', fontsize=10)

axs[1, 1].bar(x='Shelf',height='Carbohydrates',data=dataset)
axs[1, 1].set_title('Carbohydrates', fontsize=10)

axs[1, 2].bar(x='Shelf',height='Sugars',data=dataset)
axs[1, 2].set_title('Sugars', fontsize=10)

axs[2, 0].bar(x='Shelf',height='Potassium',data=dataset)
axs[2, 0].set_title('Potassium', fontsize=10)

axs[2, 1].bar(x='Shelf',height='Vitamins',data=dataset)
axs[2, 1].set_title('Vitamins', fontsize=10)

axs[2, 2].bar(x='Shelf',height='Weight',data=dataset)
axs[2, 2].set_title('Weight', fontsize=10)
plt.show()