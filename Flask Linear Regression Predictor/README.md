# Flask Linear Regression Predictor

This repository contains a Flask web application (`main.py`) for predicting prices based on a Linear Regression model. The application uses a trained model saved in a pickle file and allows users to input plot size and price through a web form.

## Contents

- **main.py**: This Python script contains the Flask web application. It loads a pre-trained Linear Regression model, defines routes for rendering HTML templates and handling predictions, and runs the Flask app.

- **model.pkl**: This pickle file stores the trained Linear Regression model.

- **linear_regression.pkl**: This pickle file contains information about the features used in the model.

- **templates/form.html**: This HTML template file defines the structure of the web form.

## How to Use

1. Run the Flask application by executing `main.py`.
2. Open your web browser and go to `http://127.0.0.1:5000/`.
3. Fill in the plot size and price in the provided form and click "Submit."
4. The application will make a prediction using the pre-trained model, and the result will be displayed.

## Dependencies

Ensure you have the required dependencies installed before running the application. You can install them using the following:

```bash
pip install flask pandas scikit-learn
```

## Note

This application uses a Linear Regression model to predict prices based on the input features. Adjustments can be made to the features and model training process as needed.



Enjoy using the Flask Linear Regression Predictor!
