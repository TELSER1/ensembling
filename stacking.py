import pandas as pd
import numpy as np
import pandas as pd
import pdb
from sklearn.ensemble import GradientBoostingRegressor,GradientBoostingClassifier

class stacked_regressor:
    def __init__(self,modellist,stacking_function=GradientBoostingRegressor()):
        '''
        modellist:A list of names/models to stack, as well as the data transform necessary to make a prediction with that model stacking_function [Modelinstance,transforminstance]. E.G., for Random Forest Regressor RFR and DataFrameMapper DFM and Gradient Boosting Regressor GBR with DataFrameMapper DFM1, we would pass [('RFR',RFR,DFM),('GBR',GBR,DFM1)]
        stacking_function:An instance of the model used to stack predictions; defaults to gradient boosted trees
        '''
        self.modellist=modellist
        self.stacker=stacking_function
        return
    def fit(self,X,transformer,y):
        '''
        X: The matrix of independent variables; this needs to match up to the passed transform functions in modellist.  This should be training data that the models in modellist were NOT trained on
transform:The transformation you wish to apply to X and the predictions from the component models before fitting the stacking_function
y: The target variable                                                                                                                                                                                 
        '''
        self.transformer=transformer
        preds=pd.DataFrame({i[0]:i[1].predict(i[2].transform(X)) for i in self.modellist})
        for i in preds.keys():
            X[i]=preds[i]
        self.stacker.fit(self.transformer.fit_transform(X),y)
        return
    def predict(self,X):
        return(self.stacker.predict(self.transformer.transform(pd.concat([X.reset_index(),pd.DataFrame({i[0]:i[1].predict(i[2].transform(X)) for i in self.modellist})],axis=1))))
        

class stacked_classifier:
    def __init__(self,modelist,stacking_function=GradientBoostingClassifier):
        '''
modellist:A list of names/models to stack, as well as the data transform necessary to make a prediction with that model stacking_function [Modelinstance,transforminstance]. E.G., for Random Forest Regressor RFC and DataFrameMapper DFM and Gradient Boosting Regressor GBC with DataFrameMapper DFM1, we would pass [('RFC',RFC,DFM),('GBC',GBC,DFM1)]
stacking_function:An instance of the model used to stack predictions; defaults to gradient boosted trees                                                                 
        '''
        self.modellist=modellist
        self.stacker=stacking_function
        return
    def fit(self,X,transformer,y):
        '''
        X: The matrix of independent variables; this needs to match up to the passed transform functions in modellist.  This should be training data that the models in modellist were NOT trained on
        transform:The transformation you wish to apply to X and the predictions from the component models before fitting the stacking_function
        y: The target variable'''
        self.transformer=transformer
        preds=pd.DataFrame({i[0]:i[1].predict(i[2].transform(X)) for i in self.modellist})
        for i in preds.keys():
            X[i]=preds[i]
        self.stacker.fit(self.transformer.fit_transform(X),y)
        return
    def predict(self,X):
        return(self.stacker.predict(self.transformer.transform(pd.concat([X.reset_index(),pd.DataFrame({i[0]:i[1].predict_proba(i[2].transform(X)) for i in self.modellist})],axis=1))))
    def predict_proba(self,X):
        return(self.stacker.predict_proba(self.transformer.transform(pd.concat([X.reset_index(),pd.DataFrame({i[0]:i[1].predict_proba(i[2].transform(X)) for i in self.modellist})],axis=1))))
