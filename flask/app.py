import numpy as np
from flask import Flask, request, jsonify, render_template

import tensorflow as tf
import keras
from keras.models import load_model

app = Flask(__name__)

model = load_model('Job_Role_model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    y=model.predict( np.array( [final_features,] )  )
    result = np.where(y == np.amax(y))
    
    '''
    For rendering results on HTML GUI
    '''
   
   

   

#Here i am printing this on the terminal but u have to put it like this on the website

    if result[0]==[0]:
        return render_template('index.html', prediction_text='Business Intelligence')
        print('Business Intelligence Analyst')
    elif result[0]==[1]:
        return render_template('index.html', prediction_text='Database Administrator')
        print('Database Administrator')
    elif result[0]==[2]:
        return render_template('index.html', prediction_text='Project Manager')
        print('Project Manager')
    elif result[0]==[3]:
        return render_template('index.html', prediction_text='Security Administrator')
        print('Security Administrator')
    elif result[0]==[4]:
        return render_template('index.html', prediction_text='Software Developer')
        print('Software Developer')
    else:
        return render_template('index.html', prediction_text='Technical Support')
        print('Technical Support')
   

   # return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
