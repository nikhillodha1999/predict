from flask import Flask, render_template, request
app = Flask(__name__)

#for data manipulations
import numpy as np
import pandas as pd     

#Reading the dataset
data = pd.read_csv('data.csv')

from sklearn.cluster import KMeans

#removing the labels column
x = data.drop(['label'], axis=1)

#selecting all the values of data
x = x.values

#Splitting the Dataset for predictive modelling

y = data['label']
x = data.drop(['label'], axis=1)

#Creating training and testing sets for results validation
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#Creating a Predictive Model

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

@app.route("/", methods=["GET"])
def home():
     return render_template('index.html')


@app.route('/', methods=['POST'])
def getInput():
    n = request.form['nitro']
    p = request.form['phos']
    k = request.form['pota']
    temp = request.form['temp']
    hum = request.form['hum']
    ph = request.form['ph']
    rain = request.form['rain']
    prediction = model.predict((np.array([[n, p, k, temp, hum, ph, rain]])))
    imageList={}
    for i in prediction:
     if i=='mango':
          imageList={'Mango':'../static/images/mango.jpg'}
     if i=='rice':
          imageList={'Rice':'../static/images/rice.jpg'}
     if i=='pomegranate':
          imageList={'Pomegranate':'../static/images/pomegranate.jpg'}
     if i=='pigeonpeas':
          imageList={'Pigeonpeas':'../static/images/pigeonpeas.jpeg'}
     if i=='papaya':
          imageList={'Papaya':'../static/images/papaya.jpg'}
     if i=='orange':
          imageList={'Orange':'../static/images/orange.jpg'}
     if i=='muskmelon':
          imageList={'Muskmelon':'../static/images/muskmelon.jpeg'}
     if i=='mungbean':
          imageList={'Mungbean':'../static/images/mungbeans.jpg'}
     if i=='mothbeans':
          imageList={'Mothbean':'../static/images/mothbean.jpeg'}
     if i=='lentil':
          imageList={'Letil':'../static/images/lentil.jpg'}
     if i=='kidneybeans':
          imageList={'Kidneybeans':'../static/images/kidneybean.jpeg'}
     if i=='grapes':
          imageList={'Grapes':'../static/images/grapes.jpeg'}
     if i=='jute':
          imageList={'Jute':'../static/images/jute.jpg'}
     if i=='blackgram':
          imageList={'Blackgram':'../static/images/blackgram.jpg'}
     if i=='apple':
          imageList={'Apple':'../static/images/apple2.jpeg'}
     if i=='coffee':
          imageList={'Coffee':'../static/images/coffee.jpeg'}
     if i=='maize':
          imageList={'Maize':'../static/images/maize.png'}
     if i=='watermelon':
          imageList={'Watermelon':'../static/images/watermelon.jpeg'}
     if i=='banana':
          imageList={'Banana':'../static/images/banana.jpeg'}
     if i=='coconut':
          imageList={'Coconut':'../static/images/coconut.jpg'}
     if i=='cotton':
          imageList={'Cotton':'../static/images/cotton.jpeg'}
     if i=='chickpea':
          imageList={'Chickpea':'../static/images/chickpea.jpg'}


     # xstr +=`<img src="../static/images/'+i+'.jpg">`+`<h1>MY</h1>`
    #return prediction
    return render_template('index.html', res=imageList)