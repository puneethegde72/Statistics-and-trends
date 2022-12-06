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
    years = [35,40,45,50,55,5,64]
    countries=[2,35,55,81,109,119,202,205,251]
    def group_f(col, value, years, countries):
        df1=df.groupby("Indicator Name", group_keys= True)
        df1= df1.get_group("Urban population")
        df1 = df1.reset_index()
        a = df1['Country Name']
        df1= df1.iloc[countries,years]
        df1.insert(loc=0, column='Country Name', value=a)
        df2 = df1.set_index('Country Name').T
        return df1,df2
    df1,df2 = group_f("Indicator Name","Urban population",years,countries)
    df3, df4 = group_f("Indicator Name","Forest area (sq. km)",years,countries)
    return df1,df2,df3,df4

Urban_population_c,Urban_population_y,forest_c,Forest_y = dataFrame("API_19_DS2_en_csv_v2_4700503.csv")

'''
def Bar_p(value_x, value_y):
    a.plot.bar(x = value_x,
                    y= value_y,
                    colormap='viridis', legend=True, figsize=(15,8), rot=45 )
    return
a["Average"] = a.mean(axis = 1,numeric_only= True)
Bar_p("Country Name", "Average")
'''