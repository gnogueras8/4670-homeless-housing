# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

data = pd.read_csv('../final_data.csv')

data = pd.get_dummies(data, prefix_sep='_')

data = pd.concat([data, pd.get_dummies(data['Region_ID'], prefix="region_")], axis=1)
data.drop(['Region_ID'], axis=1, inplace=True)

data = pd.concat([data, pd.get_dummies(data['Year'], prefix="year_")], axis=1)
data.drop(['Year'], axis=1, inplace=True)

print(data.columns)

data.to_csv('../final_data_dummy.csv',index=False)
