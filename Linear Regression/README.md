# Linear Regression for Plot Price Prediction

This repository contains a Jupyter Notebook (`main.ipynb`) implementing linear regression for predicting plot prices. The notebook uses the gradient descent algorithm to find the best-fitting line for the given dataset.

## Necessary Imports
- `numpy` and `matplotlib` for numerical operations and plotting.
- `pandas` for handling and manipulating the dataset.

## Usage
1. Run the notebook `main.ipynb`.
2. The notebook reads the dataset ('price-prediction.csv') and visualizes the datapoints.
3. The linear regression model is trained using gradient descent for a specified number of epochs.
4. The script then prompts the user to input a plot size for price prediction.

## Functions
- `plot_data(m, b, dataset)`: Plots the dataset and the linear regression line.
- `loss_function(m, b, points)`: Calculates the average error of the linear regression model.
- `gradient_descent(current_m, current_b, points, lr)`: Performs gradient descent to update the model parameters.

## Running Script
- The script initializes the slope (m) and y-intercept (b) to 0.
- It performs gradient descent for a specified number of epochs.
- Plots are displayed at intervals, showing the data and the current regression line.

## Predicting New Data
- The user can input a plot size, and the model predicts the corresponding price.

Enjoy exploring linear regression for plot price prediction!
