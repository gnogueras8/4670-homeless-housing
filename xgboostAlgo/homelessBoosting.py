import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

#read in data with dummy variables
data = pd.read_csv('../final_data_dummy.csv')

#split into testing and training sets
train,test=train_test_split(data,test_size=0.2)
print(train.head())

#load sets into DMatrice
d_train = xgb.DMatrix(test)
d_test = xgb.DMatrix(train)

