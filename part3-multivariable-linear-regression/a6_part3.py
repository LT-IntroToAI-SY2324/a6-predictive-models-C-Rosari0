import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles", "age"]].values  # Use double square brackets here
y = data["Price"].values
# Create a linear regression model
model = LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model.fit(x_train, y_train)

# Split the data into training and testing sets

coefficients = np.round(model.coef_, 2)
intercept = np.round(model.intercept_, 2)
r_squared = np.round(model.score(x_test, y_test), 2)


# Fit the model to the training data

print(f"Coefficients: {coefficients}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_squared}")

# Loop through the data and print out the predicted prices and the
# actual prices
print("***************")
print("Testing Results")
predictions = model.predict(x_test)
for i in range(len(predictions)):
    print(f"Predicted Price: {np.round(predictions[i], 2)}, Actual Price: {y_test[i]}")
# Make predictions on the test data
predictions = model.predict(x_test)

predictions_car1_data = pd.DataFrame({"miles": [89000, 150000], "age": [10, 20]})
predictions_car1_data = model.predict(predictions_car1_data)


for i, prediction in enumerate(predictions_car1_data):
    print(f"Predicted price for Car {i+1}: ${prediction:.2f}")

predictions_car2_data = pd.DataFrame({"miles": [150000,0], "age": [0, 20]})
predictions_car2_data = model.predict(predictions_car2_data)
for i, prediction in enumerate(predictions_car1_data):
    print(f"Predicted price for Car{i+1}: ${prediction:.2f}")
