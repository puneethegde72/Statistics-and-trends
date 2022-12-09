# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:50:02 2022

@author: Puneet
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sts

def dataFrame(file_name,years,countries,col, value1):
    df= pd.read_csv(file_name, skiprows=4)
    df1=df.groupby(col, group_keys= True)
    df1= df1.get_group(value1)
    df1 = df1.reset_index()
    a = df1['Country Name']
    df1= df1.iloc[countries,years]
    df1.insert(loc=0, column='Country Name', value=a)
    df1= df1.dropna(axis = 1)
    df2 = df1.set_index('Country Name').T
    return df1,df2
'''
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
    df5, df6 = group_f("Indicator Name","CO2 emissions (kt)",years,countries)
    return df1,df2,df3,df4,df5,df6
'''
def stats_f(file_name,years,col, value1):
    df= pd.read_csv(file_name, skiprows=4)
    df1=df.groupby(col, group_keys= True)
    df1= df1.get_group(value1)
    df1 = df1.reset_index()
    df1= df1.iloc[:,years]
    #df1.insert(loc=0, column='Country Name', value=a)
    #df1.to_csv("C:/Users/Puneet/OneDrive/Documents/india.csv")
    df1= df1.dropna(axis = 0)
    df1= df1.dropna(axis = 1)
    df2 = df1.set_index("Indicator Name").T
    #df2.columns=df2.iloc[0]
    return df2

years = [35,40,45,50,55,60,64]
countries=[35,40,55,81,109,119,202,205,251]
population_c,population_y =dataFrame("API_19_DS2_en_csv_v2_4700503.csv",years,countries,"Indicator Name","Population, total")
Green_gas_c,Green_gas_y = dataFrame("API_19_DS2_en_csv_v2_4700503.csv",years,countries,"Indicator Name","Total greenhouse gas emissions (kt of CO2 equivalent)")
co2_c,co2_y = dataFrame("API_19_DS2_en_csv_v2_4700503.csv",years,countries,"Indicator Name","CO2 emissions (kt)")
india = stats_f("API_19_DS2_en_csv_v2_4700503.csv",[3,35,40,45,50,55,60,64],"Country Name","India")
print("india/n", india)



def plot_p(DataFrame, col, types, name):
    DataFrame.plot(x=col, rot=45, figsize=(20,10), kind= types, title= name)
    return
plot_p(population_c,"Country Name","bar","Total population")
plot_p(Green_gas_c,"Country Name", "bar","Total greenhouse gas emissions (kt of CO2 equivalent)")

population_y.plot(figsize=(20,10),kind="line",title="Total population")
co2_y.plot(figsize=(20,10),kind="line",title="Total Co2 Emission")

india.corr()
india = india.loc[:,["Population, total","Urban population","Foreign direct investment, net inflows (% of GDP)","Mortality rate, under-5 (per 1,000 live births)","Cereal yield (kg per hectare)","CO2 emissions (kt)"] ]
print(india)
india.corr()
india.corr().style.background_gradient(cmap="YlOrBr")

plt.figure()
plt.imshow( india.corr(), interpolation = 'nearest',cmap="GnBu")
plt.title('HeatMap Using Matplotlib Library')
plt.tight_layout()
plt.show()