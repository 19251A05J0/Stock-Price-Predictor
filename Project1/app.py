from flask import Flask, render_template, request

import pickle as pkl
from sklearn.linear_model import LinearRegression
app = Flask(__name__)

@app.route('/pre')
def pre():
    return render_template('pre.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST" :
        Open = request.form['Open']
        High = request.form['High']
        Low = request.form['Low']
        Volume = request.form['Volume']
        
        data = [[float(Open),float(High),float(Low),float(Volume)]]
        lr = pkl.load(open('price.pkl','rb'))
        prediction = lr.predict(data)[0]
    
    return render_template('pre.html',prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
