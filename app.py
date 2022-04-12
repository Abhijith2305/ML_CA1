# -*- coding: utf-8 -*-
"""App.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_CKdsMI2jWxKPRPb1Z9pgyGl7Qs0snqh
"""

import os 
from flask import send_from_directory     
from flask import Flask, render_template, request
import pandas as pd
import pickle as pkl
import json


app = Flask(__name__)
model = pkl.load(open('model.pkl', 'rb'))

@app.route('/', methods=["GET"])
def index():
    return render_template("ML_CA_html.html")

@app.route('/predict', methods=["POST"])
def predict():
    value = ''
    data = request.form['jsonData']
    data_jfy = json.loads(data)
    df = pd.DataFrame(data_jfy, index=[0])
    value = model.predict(df)
    return render_template("ML_CA_html.html", j = round(value[0], 2))


@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)