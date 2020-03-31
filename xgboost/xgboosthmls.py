        1 file(s) copied.
import numpy as np
import pandas as pd
import xgboost as xgb

#read in data with dummy variables
data = pd.read_csv('../final_data_dummy.csv')

#split training and testing sets
data_test = data[]
data_train =data[]
data_validate = data[]

#load sets into DMatrice
#d_train = xgb.DMatrix(data_test)
#d_test = xgb.DMatrix(data_train)
#d_validate = xgb.DMatrix(data_validate)