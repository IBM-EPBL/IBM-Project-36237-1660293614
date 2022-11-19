from json import load

import numpy as np
import pandas as pd
import seaborn as sns
from flask import Flask, render_template, request, send_file
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

sns.set_style('whitegrid')
# import plotly.express as px
import warnings
from itertools import cycle

warnings.filterwarnings("ignore")
import pickle

# from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("Heart_Disease_Prediction.csv")    
dtclas=DecisionTreeClassifier()
X= df.drop(['Target'], axis=1)
y= df['Target']
X_train, X_test,y_train, y_test=train_test_split(X,y,test_size=0.25,random_state=40)
modeldt=dtclas.fit(X_train,y_train)
pickle.dump(modeldt, open('heart_disease_detector.pkl', 'wb'))


app = Flask(__name__)
cors = CORS(app)



@app.post("/input")
@cross_origin()
def predict():   
    
    mod = pickle.load(open('heart_disease_detector.pkl', 'rb')) 
    features = [float(i) for i in request.form.values()]
    print(features)
    array_features = [np.array(features)]

    prediction = mod.predict(array_features)
    
    output = prediction

    if output == 1:
        # return render_template('home.html', 
        #                        result = 'The patient is not likely to have heart disease!')
        return "The patient is not likely to have heart disease!"
    else:
        # return render_template('home.html', 
        #                        result = 'The patient is likely to have heart disease!')
        return "The patient is likely to have heart disease!"




# @app.get("/results")
# def results():
#     return send_file("Plot.png")
# @app.post('/predict')
# def predict():
    
#     features = [float(i) for i in request.form.values()]
#     array_features = [np.array(features)]

#     prediction = mod.predict(array_features)
    
#     output = prediction

#     if output == 1:
#         return render_template('home.html', 
#                                result = 'The patient is not likely to have heart disease!')
#     else:
#         return render_template('home.html', 
#                                result = 'The patient is likely to have heart disease!')


app.run()
