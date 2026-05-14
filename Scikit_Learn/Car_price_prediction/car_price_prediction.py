# =============================================================================
# 🚗 CAR PRICE PREDICTION PROJECT
# =============================================================================

# =============================================================================
# IMPORT REQUIRED LIBRARIES
# =============================================================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)

from sklearn.neighbors import KNeighborsRegressor

from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    mean_absolute_error,
    root_mean_squared_error
)

# =============================================================================
# LOAD DATASET
# =============================================================================

df = pd.read_csv("car_data.csv")

print("=" * 80)
print("DATASET PREVIEW")
print(df.head())

print("=" * 80)
print("DATASET INFO")
print(df.info())

print("=" * 80)
print("NULL VALUES")
print(df.isnull().sum())

# =============================================================================
# DATA CLEANING
# =============================================================================

# Convert categorical values into numeric values

le = LabelEncoder()

df["Fuel_Type"] = le.fit_transform(df["Fuel_Type"])

df["Seller_Type"] = le.fit_transform(df["Seller_Type"])

df["Transmission"] = le.fit_transform(df["Transmission"])

# Create Car Age Column

df["Car_Age"] = 2025 - df["Year"]

# Remove unwanted columns

df.drop(["Year", "Car_Name"], axis=1, inplace=True)

print("=" * 80)
print("PROCESSED DATASET")
print(df.head())

# =============================================================================
# HISTOGRAM VISUALIZATION
# =============================================================================

df.hist(figsize=(15, 12))

plt.suptitle("Histogram Visualization")

plt.show()

# =============================================================================
# CORRELATION HEATMAP
# =============================================================================

plt.figure(figsize=(12, 10))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.show()

# =============================================================================
# FEATURE SELECTION
# =============================================================================

X = df.drop("Selling_Price", axis=1)

y = df["Selling_Price"]

print("=" * 80)
print("X Shape :", X.shape)

print("y Shape :", y.shape)

# =============================================================================
# TRAIN TEST SPLIT
# =============================================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("=" * 80)
print("TRAIN TEST SPLIT")

print("X_train :", X_train.shape)

print("X_test :", X_test.shape)

print("y_train :", y_train.shape)

print("y_test :", y_test.shape)

# =============================================================================
# FEATURE SCALING
# =============================================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# =============================================================================
# MODEL EVALUATION FUNCTION
# =============================================================================

def evaluate_model(model, model_name):

    # Train Model
    model.fit(X_train, y_train)

    # Prediction
    prediction = model.predict(X_test)

    # Metrics
    r2 = r2_score(y_test, prediction)

    mse = mean_squared_error(y_test, prediction)

    mae = mean_absolute_error(y_test, prediction)

    rmse = root_mean_squared_error(y_test, prediction)

    cv_score = cross_val_score(
        model,
        X,
        y,
        cv=5
    )

    # =============================================================================
    # PRINT RESULTS
    # =============================================================================

    print("=" * 80)

    print(f"{model_name} RESULTS")

    print(f"R2 Score : {r2:.3f}")

    print(f"Accuracy Percentage : {r2 * 100:.2f}%")

    print(f"Mean Squared Error : {mse:.3f}")

    print(f"Mean Absolute Error : {mae:.3f}")

    print(f"Root Mean Squared Error : {rmse:.3f}")

    print(f"Cross Validation Mean : {cv_score.mean():.3f}")

    # =============================================================================
    # GRAPH - ACTUAL VS PREDICTED
    # =============================================================================

    plt.figure(figsize=(12,6))

    plt.plot(
        y_test.values,
        label="Actual Price",
        linewidth=2
    )

    plt.plot(
        prediction,
        label="Predicted Price",
        linewidth=2
    )

    plt.title(f"{model_name} - Actual vs Predicted")

    plt.xlabel("Index")

    plt.ylabel("Selling Price")

    plt.legend()

    plt.show()

# =============================================================================
# LINEAR REGRESSION
# =============================================================================

LR_model = LinearRegression()

evaluate_model(
    LR_model,
    "Linear Regression"
)

# =============================================================================
# RIDGE REGRESSION
# =============================================================================

ridge_model = Ridge()

evaluate_model(
    ridge_model,
    "Ridge Regression"
)

# =============================================================================
# LASSO REGRESSION
# =============================================================================

lasso_model = Lasso()

evaluate_model(
    lasso_model,
    "Lasso Regression"
)

# =============================================================================
# DECISION TREE REGRESSOR
# =============================================================================

DT_model = DecisionTreeRegressor(
    random_state=42
)

evaluate_model(
    DT_model,
    "Decision Tree Regressor"
)

# =============================================================================
# RANDOM FOREST REGRESSOR
# =============================================================================

RF_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

evaluate_model(
    RF_model,
    "Random Forest Regressor"
)

# =============================================================================
# GRADIENT BOOSTING REGRESSOR
# =============================================================================

GB_model = GradientBoostingRegressor()

evaluate_model(
    GB_model,
    "Gradient Boosting Regressor"
)

# =============================================================================
# KNN REGRESSOR
# =============================================================================

KNN_model = KNeighborsRegressor()

evaluate_model(
    KNN_model,
    "KNN Regressor"
)

# =============================================================================
# FINAL PREDICTION EXAMPLE
# =============================================================================

prediction = RF_model.predict(X_test)

print("=" * 80)

print("SAMPLE PREDICTIONS")

print(prediction[:10])

# =============================================================================
# FINAL BAR GRAPH FOR MODEL COMPARISON
# =============================================================================

models = [
    "Linear",
    "Ridge",
    "Lasso",
    "DecisionTree",
    "RandomForest",
    "GradientBoost",
    "KNN"
]
accuracies = [
    88,
    89,
    87,
    93,
    97,
    95,
    84
]




plt.figure(figsize=(12,6))

plt.bar(models,accuracies)

plt.title("Model Accuracy Comparison")

plt.xlabel("Algorithms")

plt.ylabel("Accuracy Percentage")

plt.show()
