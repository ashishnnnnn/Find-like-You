from sklearn.cluster import KMeans
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from tqdm import tqdm_notebook as tqdm
import pickle
data=pd.read_csv('mycsv.csv',index_col=False)
X=[]
Name=[]
for i,j in data.iterrows():
    Name.append(j[0])
    X.append(list(j)[1:])
kmeans = KMeans(n_clusters=10, random_state=0).fit(X)
pickle.dump(kmeans, open('model.pkl','wb'))
  
