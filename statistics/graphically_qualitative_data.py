# Importing libraries
import pandas as pd

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

frequency_table = dataset.value_counts().to_frame(name='frequency').rename_axis('pizza_restaurants').sort_index()

print(frequency_table)

# Frequency Table with relative_frequency

frequency_table['relative_frequency'] = frequency_table['frequency']/frequency_table['frequency'].sum()

print(frequency_table)

# Frequency Table with percentage_frequency
frequency_table['percentage_frequency'] = frequency_table['frequency']/frequency_table['frequency'].sum()*100

print(frequency_table)

