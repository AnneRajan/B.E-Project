import numpy as np
import pandas as pd

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

from flask import Flask, request, jsonify, render_template

 


app = Flask(__name__)

from keras.models import load_model
model = load_model('Job_Role_model.h5')

@app.route('/jobprofile.html', methods=['POST'])

def predict():
    data = request.get_json(force=True)

    data.update((x,[y]) for x,y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    result = model.predict(data_df)
    output = {'result': int(result[0])}

    return jsonify(results=output)




    if _name_ == '_main_':
        app.run(port = 5000, debug = True)