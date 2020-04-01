import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


## For index page
@app.route('/')
def home():
    return render_template('index.html')


## For Breast Cancer page
@app.route('/breast_cancer/', methods=['POST','GET'])
def index():
  return render_template('breast_cancer.html')


## For Prediction Page on Breast Cancer
@app.route('/predict/',methods=['POST'])
def predict():
    model = pickle.load(open('model.pkl', 'rb'))
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter', 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension']
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)
        
    if output == 0:
        res_val = "** breast cancer **"
    else:
        res_val = "no breast cancer"
    return render_template('breast_cancer.html', prediction_text='Patient has {}'.format(res_val))



@app.route('/malaria/', methods=['POST','GET'])
def malaria():
  return render_template('malaria.html')


## For Prediction Page on Breast Cancer
@app.route('/predict_malaria/',methods=['POST'])
def predict_malaria():
  model = pickle.load(open('malaria.pickle', 'rb'))
  input_features = [float(x) for x in request.form.values()]
  features_value = [np.array(input_features)]
    
  features_name = ['area_0', 'area_1', 'area_2', 'area_3','area_4']

    
  df = pd.DataFrame(features_value, columns=features_name)
  output = model.predict(df)
        
  if output == 'Parasitized':
    res_val = "** Parasitized **"
  else:
    res_val = "Uninfected"
  return render_template('malaria.html', prediction_text='Patient has {}'.format(res_val))





@app.route('/diabetes/', methods=['POST','GET'])
def diabetes():
  return render_template('diabetes.html')


## For Prediction Page on Breast Cancer
@app.route('/predict_diabetes/',methods=['POST'])
def predict_diabetes():
  model = pickle.load(open('diabetes.pickle', 'rb'))
  input_features = [float(x) for x in request.form.values()]
  features_value = [np.array(input_features)]
  output = model.predict([np.array(input_features)])
        
  if output == 1:
    res_val = "** Parasitized **"
  if output == 0:
    res_val = "Uninfected"
  return render_template('diabetes.html', prediction_text='Patient has {}'.format(res_val))



    
if __name__ == "__main__":
    app.run(debug=True)
