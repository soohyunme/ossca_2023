import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def mse(y_true, y_pred):
    return metrics.mean_squared_error(y_true, y_pred)


def msa(y_true, y_pred):
    return metrics.mean_absolute_error(y_true, y_pred)


# Load the data - 1
df = pd.read_csv("study.csv")

# Draw a scatter plot - 2
plt.scatter(df["hours"], df["score"])
plt.show()

# Split the data into training and test sets - 3
X = np.array(df["hours"]).reshape(-1, 1)
y = np.array(df["score"]).reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create a model - 4
reg = LinearRegression()

# Train the model
reg.fit(X_train, y_train)

# Make predictions
y_pred = reg.predict(X_test)

# Evaluation - 5
print(f"Mean Squared Error: {mse(y_test, y_pred) * 100:.2f}%")
print(f"Mean Absolute Error: {msa(y_test, y_pred) * 100:.2f}%")

# Save the model - 6
joblib.dump(reg, "./regression_model.pkl")

# Load the model - 6
loaded_model = joblib.load("./regression_model.pkl")

# Predict sample data - 7
X_sample = np.array([12, 14]).reshape(-1, 1)
y_sample_pred = loaded_model.predict(X_sample)

for X, pred in zip(X_sample, y_sample_pred):
    print(f"Study for {X.item()} hours, prediction score : {int(pred.item())}")
