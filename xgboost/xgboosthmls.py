import numpy as np
import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt

#read in data with dummy variables
data = pd.read_csv('../final_data_dummy.csv')
data.head()
data.describe()

#plt.scatter(data['Total_Homeless '], data['Rent'])
#plt.scatter(data['pcthmlsofciv'], data['year_2011'])

#split training and testing sets
#data_test = data[]
#data_train = data[]
#data_validate = data[]

#load sets into DMatrice
#d_train = xgb.DMatrix(data_test)
#d_test = xgb.DMatrix(data_train)
#d_validate = xgb.DMatrix(data_validate)