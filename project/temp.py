import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset = pd.read_csv('IndianWeatherRepository.csv')

# print(dataset.head(5))

dataset.drop(["temperature_fahrenheit"], axis=1, inplace=True)
dataset.drop(["precip_mm"], axis=1, inplace=True)

dataset.dropna(inplace=True)
dataset.drop(["last_updated_epoch"], axis=1, inplace=True)

# Delete all values from the pressure which has a value -9999
indexn = dataset[dataset['pressure_mb'] == -9999].index
dataset.drop(indexn, inplace=True)

# Taking all the features into x variable and y for prediction
Y = dataset.iloc[:, len(dataset.columns)-1]
X = dataset.iloc[:, 0:len(dataset.columns)-1]

'''
print("Prediction data for x and y:")
print(' prediction data for Y\n', Y)
print()
print('prediction data for X\n', X)
'''

# Set the dummies value as a level for the weather classification
weather_condition = pd.get_dummies(X['condition_text'])

# Delete last dummies value which is null
weather_condition.drop(["Partly cloudy"], axis=1, inplace=True)
print("After did the Normalization:\n\n", weather_condition.head(10))

# Concat the dummies value with the input feature X
X = pd.concat([X, weather_condition], axis=1)

print(X.head(10))
X.drop(["condition_text"], axis=1, inplace=True)
print(X.shape)

# Now the final dataset has been created
print("After finished pre-processing and create filter dataset:\n\n\n")
print(X.head(10))

############################################################

# Train and testing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def predict():
    # Splitting Dataset into train set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_prediction = model.predict(X_test)
    score = r2_score(y_test, y_prediction)
    print("Temperature prediction Accuracy= ", score*100)

    # Histogram of data how they look like on graphical representation
    plt.hist(y_prediction, facecolor='red', edgecolor='blue', bins=10, range=(5, 35))
    plt.title("Predicted temperature histogram")
    plt.show()

def original():
    # Original temperature vs predicted temperature graph
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_prediction = model.predict(X_test)
    score = r2_score(y_test, y_prediction)

    plt.plot(y_test)
    plt.plot(y_prediction)
    plt.title('Original temperature vs temperature')
    plt.xlabel("------------x-axis    ")
    plt.ylabel("------------y-axis    ")
    plt.legend()
    plt.show()

# predict()
original()
