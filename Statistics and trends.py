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
    years = [35,40,45,50,55,60,64]
    countries=[2,35,55,81,109,119,202,205,251]
    def group_f(col, value1, years, countries):
        df1=df.groupby(col, group_keys= True)
        df1= df1.get_group(value1)
        df1 = df1.reset_index()
        a = df1['Country Name']
        df1= df1.iloc[countries,years]
        df1.insert(loc=0, column='Country Name', value=a)
        df1= df1.dropna(axis = 1)
        df2 = df1.set_index('Country Name').T
        return df1,df2
    df1,df2 = group_f("Indicator Name","Urban population",years,countries)
    df3, df4 = group_f("Indicator Name","Total greenhouse gas emissions (kt of CO2 equivalent)",years,countries)
    return df1,df2,df3,df4

Urban_population_c,Urban_population_y,Green_gas_c,Green_gas_y = dataFrame("API_19_DS2_en_csv_v2_4700503.csv")
print("Urban_population country\n",Urban_population_c)
print("Urban_population year\n",Urban_population_y)

print("Forest country\n",Green_gas_c)

print("Forest Year/n",Green_gas_y)


def plot_p(DataFrame, col, types):
    DataFrame.plot(x=col,rot=45,figsize=(20,10),kind= types)
    return
plot_p(Urban_population_c,"Country Name","bar")
plot_p(Green_gas_c,"Country Name","bar")