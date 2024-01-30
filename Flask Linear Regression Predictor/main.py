import pickle
from flask import Flask, render_template
import pandas as pd
from flask import request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)


# Load data
data = pd.read_csv('price-prediction.csv')
# Split data into training and testing sets 
X_train = data[['PLOT', 'PRICE']]
y_train = data['PLOTS']
X_test = data[['PLOT', 'PRICE']]
y_test = data['PLOTS']

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('linear_regression.pkl', 'wb') as f:
    pickle.dump(['PLOTS','PRICES'],f)

@app.route('/')
def index():
    title = 'My Website'
    heading = 'WELCOME'
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('form.html', title=title, heading=heading, items=items)
                       

class MyForm(FlaskForm):
    plot = StringField('PLOT', validators=[DataRequired()])
    price = StringField('PRICE', validators=[DataRequired()])
    submit = SubmitField('Submit')

    
    app = Flask(__name__)
    # Load the model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    model = pickle.load(open('linear_regression.pkl', 'rb'))
    # with open('linear_regression.pkl', 'rb') as f:
    #     m,b = pickle.load(f)
    data = request.get_json()
    X = np.array([data['PLOTS'], data['PRICES']])
    prediction = model.predict(X.reshape(1, -1))[0]
    return jsonify({'prediction':prediction})

if __name__ == '__main__':
    app.run()
