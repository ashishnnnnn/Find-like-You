import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
data=pd.read_csv('mycsv.csv',index_col=False)
X=[]
Name=[]
for i,j in data.iterrows():
    Name.append(j[0])
    X.append(list(j)[1:])
k=pickle.load(open('model.pkl','rb'))
jj=list(k.labels_)
cluster={}
for i in range(len(jj)):
    if jj[i] in cluster.keys():
        cluster[jj[i]].append(Name[i])
    else:
        cluster[jj[i]]=[Name[i]]
cluster_names=list(cluster.values())    

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    args=[str(x) for x in request.form.values()]
    final_name = args[0].lower()
    for i in cluster_names:
        if final_name in i:
            prediction=i
            break
    else:
        prediction=["You have not entered your name during survay"]        

    output = prediction

    return render_template('index.html', prediction_text='People like you are {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)