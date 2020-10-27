# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# creating the dataset
data = {
    'Alcohol': [6.5, 6.1, 6.2, 4.9, 5.6, 4.5, 5.9, 4.8, 5.3, 6.1, 4.0],
    'Tobacco': [4.0, 3.8, 3.8, 3.3, 3.5, 2.9, 3.2, 2.7, 3.5, 4.5, 4.6]
}

dataset = pd.DataFrame(data=data)

# Splitting the dataset into training and test sets

x_train, x_test, y_train, y_test = train_test_split(dataset['Alcohol'].values, dataset['Tobacco'].values, test_size=0.3, random_state=0)

# creating the linear regresion object
regr = LinearRegression()

x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)
# Training the model
regr.fit(x_train, y_train)

# Making prediction using the testing set
y_pred = regr.predict(X=x_test)

# The coefficiencts
print('Coefficientc: ', regr.coef_)

# The mean squared error
print('Mean squared error: ', mean_squared_error(y_true=y_test, y_pred=y_pred))

# The coefficient of determination: 1 is perfect prediction
print('Coefficien of determination: ', r2_score(y_true=y_test, y_pred=y_pred))

# Plotting the output
plt.scatter(dataset['Alcohol'], dataset['Tobacco'], color='Blue')
plt.plot(x_test, y_pred, color='green')
plt.xticks(())
plt.yticks(())
plt.show()
