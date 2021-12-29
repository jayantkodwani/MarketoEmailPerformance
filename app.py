import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle


app = Flask(__name__)

@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')

@app.route('/predict',methods = ['POST'])
def predict():
    return render_template('home.html')   

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
        output = 'Hello'
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
