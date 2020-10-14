# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Creating the DataFrame
data = {'pizza_restaurants': ["Little Caesars",
                              "Papa John’s",
                              "Pizza Hut",
                              "Papa John’s",
                              "Bruno’s",
                              "Papa John’s",
                              "Will’s Uptown",
                              "Papa John’s",
                              "Will’s Uptown",
                              "Little Caesars",
                              "Papa John’s",
                              "Will’s Uptown",
                              "Little Caesars",
                              "Bruno’s",
                              "Papa John’s",
                              "Little Caesars",
                              "Papa John’s",
                              "Domino’s",
                              "Bruno’s",
                              "Papa John’s",
                              "Bruno’s",
                              "Papa John’s",
                              "Will’s Uptown",
                              "Papa John’s",
                              "Little Caesars",
                              "Bruno’s",
                              "Will’s Uptown",
                              "Papa John’s",
                              "Pizza Hut",
                              "Little Caesars",
                              "Papa John’s",
                              "Pizza Hut",
                              "Little Caesars",
                              "Will’s Uptown",
                              "Papa John’s",
                              "Will’s Uptown",
                              "Bruno’s",
                              "Pizza Hut",
                              "Papa John’s",
                              "Papa John’s",
                              "Domino’s",
                              "Little Caesars",
                              "Bruno’s",
                              "Papa John’s",
                              "Little Caesars",
                              "Papa John’s",
                              "Papa John’s",
                              "Will’s Uptown",
                              "Papa John",
                              "Bruno’s"]}

dataset = pd.DataFrame(data=data, columns=["pizza_restaurants"])

print(dataset)

# Frequency Table

frequency_table = dataset.value_counts().to_frame(name='frequency')  # name='frequency').rename_axis('pizza_restaurants').sort_index()

print(frequency_table)

# Frequency Table with relative_frequency

frequency_table['relative_frequency'] = frequency_table['frequency'] / frequency_table['frequency'].sum()

print(frequency_table)

# Frequency Table with percentage_frequency
frequency_table['percentage_frequency'] = frequency_table['frequency'] / frequency_table['frequency'].sum() * 100

print(frequency_table.dtypes)

# Bar chart of dataset
# 1 vertical bar graph
frequency_table.plot.bar(y='percentage_frequency', rot=70, title='frequency table of pizza restaurants')
plt.show()

# 2 horizontal bar graph
frequency_table.plot.barh(y='percentage_frequency', rot=70, title='frequency table of pizza restaurants')
plt.show()

# 3 neasted and stacked
frequency_table.plot.barh(stacked=True, title='frequency table of pizza restaurants')
plt.show()

# Bar charts
frequency_table.plot.pie(y='percentage_frequency', rot=70, title='frequency table of pizza restaurants', autopct='%1.1f%%')
plt.show()

label_data = {
              'frequency' : [78, 45, 33, 23, 14, 6, 12]
              }

# Pareto Graph
label_dataset = pd.DataFrame(data=label_data, index=['crooked_label', 'missing_label', 'printed_label', 'loose_label', 'wrinkled_label', 'smudged_label', 'other'])

# sorting the columns according to importance
label_dataset=label_dataset.sort_values(by='frequency', ascending=False)

# Creating a cumulative percentage column
label_dataset['cumulative_percentage'] = label_dataset['frequency'].cumsum()/label_dataset['frequency'].sum()*100

# Creating the pareto Graph
fig, ax = plt.subplots()
ax.bar(label_dataset.index, label_dataset['frequency'], color='blue')
ax2 = ax.twinx()
ax2.plot(label_dataset.index, label_dataset['cumulative_percentage'],marker='D' ,color='C1', ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis='y', color='C0')
ax2.tick_params(axis='y', color='C1')
plt.show()

