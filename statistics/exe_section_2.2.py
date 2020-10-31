"""Question 2.18:
a. Draw the frequency histogram for the ratings data, and describe the distribution shape. DS Design
b. Construct a relative frequency distribution and a percent frequency distribution for the bottle
design ratings.
c. Construct a cumulative frequency distribution and a cumulative percent frequency distribution.
e. Draw a frequency ogive for the bottle design ratings.
"""

# Imparting dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating the dataset
data = {'rating': [34,
                   32,
                   24,
                   32,
                   31,
                   32,
                   33,
                   25,
                   30,
                   28,
                   28,
                   30,
                   33,
                   27,
                   20,
                   30,
                   33,
                   34,
                   29,
                   33,
                   34,
                   31,
                   31,
                   32,
                   26,
                   22,
                   31,
                   31,
                   32,
                   30,
                   33,
                   27,
                   32,
                   33,
                   28,
                   30,
                   28,
                   32,
                   30,
                   29,
                   26,
                   32,
                   25,
                   33,
                   35,
                   27,
                   29,
                   31,
                   32,
                   32,
                   33,
                   34,
                   32,
                   29,
                   33,
                   29,
                   31,
                   31,
                   34,
                   33]}

dataset = pd.DataFrame(data=data)

# A
dataset.plot.hist(bins=6)
plt.show()
"""The dataset is skewed to the right"""

# B (creating frequency table bin = 3 class length = 3)


dataset_freq = dataset.value_counts().to_frame(name='frequency_distribution')
dataset_freq.reindex()
print(dataset_freq.index[0])

# Drawing Dot plots
dataset_freq.plot.scatter(x=dataset_freq.index, y='frequency_distribution')