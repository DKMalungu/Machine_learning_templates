# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

data = [22, 19, 16, 18, 13, 16, 29, 17,
        15, 23, 18, 21, 16, 10, 16, 22, 17,
        25, 15, 21, 20, 16, 15, 19, 18, 15, 22,
        16, 24, 20, 17, 14, 14, 19, 15, 27, 12, 17,
        25, 13, 17, 16, 13, 18, 19, 18, 14, 17, 17,
        12, 23, 24, 18, 16, 16, 20, 15, 24, 17, 21,
        15, 14, 19, 26, 21]

dataset = pd.DataFrame(data)

# Histogram
fig, ax = plt.subplots()
dataset.plot.hist(ax=ax, bins=7, title='pandas implementation')
dataset.plot.kde(ax=ax)
ax.set_ylabel('Probability')
ax.grid(axis='y')
ax.set_facecolor('#d8dcd6')
plt.show()
plt.hist(x=dataset, bins=7)
plt.title('matplotlib implementation')
plt.show()
