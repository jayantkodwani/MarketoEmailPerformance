import numpy as np
from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')
    #return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    #output = round(prediction[0], 2)
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    #data = request.get_json(force=True)
    #prediction = model.predict([np.array(list(data.values()))])

    output = 'Hello'
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
