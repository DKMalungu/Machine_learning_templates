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

# Plotting frequency plot data in defines classes (The test involves class scores)
marks = [32,
         45,
         50,
         56,
         58,
         60,
         61,
         61,
         63,
         64,
         64,
         65,
         66,
         67,
         67,
         68,
         69,
         69,
         72,
         76,
         78,
         81,
         83,
         83,
         85,
         86,
         87,
         87,
         88,
         89,
         90,
         90,
         91,
         92,
         92,
         93,
         93,
         94,
         96,
         98]

# Creating the classes
g = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for i in marks:
    print(i)
    if i < 40:
        print(i)
        g += 1
        print(g)
    elif i < 50:
        f += 1
    elif i < 60:
        e += 1
    elif i < 70:
        d += 1
    elif i < 80:
        c += 1
    elif i < 90:
        b += 1
    else:
        a = +1
data_class = {'scores_frequency': [a, b, c, d, e, f, g],
              'score_classes': ['90<100', '80<90', '70<80', '60<70', '50<60', '40<50', '30<40']}

marks_data = pd.DataFrame(data=data_class)
print(marks_data)
marks_data.plot.bar(x='score_classes', y='scores_frequency')
plt.show()
