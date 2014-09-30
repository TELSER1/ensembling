import pandas as pd
import pandas as pd
import numpy as np
from stacking import stacked_regressor
from sklearn_pandas import DataFrameMapper
from sklearn.linear_model import LinearRegression
class rself():
    def __init__(self):
        return
    def fit(self,X,y=None):
        return
    def transform(self,X,y=None):
        a=X.shape[0]
        return(np.reshape(X,(a,1)))
    def fit_transform(self,X,y=None):
        return(X)
class rself2():
    def __init__(self):
        return
    def fit(self,X,y=None):
        return
    def transform(self,X,y=None):
        return(X)
    def fit_transform(self,X,y=None):
        return(X)    
data=pd.read_csv("soiltrain.csv")
data['randint']=np.random.randint(0,high=10,size=data.shape[0])
train=data[data['randint']<7]
test=data[data['randint']>=7]
RS1=DataFrameMapper([("m7497.96",rself())])
RS2=DataFrameMapper([('m7496.04',rself())])
LR1=LinearRegression()
LR2=LinearRegression()
LR1.fit(RS1.transform(train),train['Sand'])
LR2.fit(RS1.transform(train),train['Sand'])
SR=stacked_regressor([("model1",LR1,RS1),("model2",LR2,RS2)])
SR.fit(train,DataFrameMapper([("m7494.11",rself())]),train['Sand'])
print SR.predict(test).shape

