"""
Dealing with missing values in Pandas
The default missing values in pandas is NaN but python None, not available or NA should all be considered as missing values
"""
#If you want to consider inf and -inf to be “NA” in computations, you can set
import pandas as pd
import numpy as np
pd.options.mode.use_inf_as_na = True

# Creating a dummy DataFrame
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])

print('Dummy DataFrame:\n', df)

# Inserting New column into a DataFrame
df['four'] = 'bar'
df['five'] = df['one'] > 0
# Craeting a dataframe with missing values

df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

print('Dummy dataframe with missing values\n', df2)

# Detecting if Values are missing or not missing
print('Detecting if value is missing\n', df2.isna(), '\n if the value is missing True')

print('Detecting if value is not missing\n', df2.notna(), '\n if the value is not missing True')




