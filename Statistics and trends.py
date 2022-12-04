# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:50:02 2022

@author: Puneet
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sts

def dataFrame(file_name):
    df= pd.read_csv(file_name, skiprows=4)
   # df= df.drop(df.iloc[:, -6:],axis=1)
    a = df['Country Name']
    #print(a)
    df= df.iloc[8:18, 45:55]
    df.insert(loc=0, column='Country Name', value=a)
    #df['Country Name']= a
    df= df.dropna(axis = 0)
   # print(df)
    df1 = df.set_index('Country Name').T
    #print(df1)
    return df, df1

a,b = dataFrame("API_EN.ATM.CO2E.LF.KT_DS2_en_csv_v2_4538194.csv")
print(a)
print(b)
c,d = dataFrame("API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_4695288.csv")
print(c)
print(d)
def Bar_p(value_x, value_y):
    a.plot.bar(x = value_x,
                    y= value_y,
                    colormap='viridis', legend=True, figsize=(15,8), rot=45 )
    return
a["Average"] = a.mean(axis = 1,numeric_only= True)
Bar_p("Country Name", "Average")