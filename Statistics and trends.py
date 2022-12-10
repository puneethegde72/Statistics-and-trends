# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:50:02 2022

@author: Puneet
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sts
import plotly.express as px
import seaborn as sns
"""Readng manupulating file and returning a dataframe and transpose of the dataframe"""
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
Up_c,Up_y = dataFrame("API_19_DS2_en_csv_v2_4700503.csv",years,countries,"Indicator Name","Urban population")
india = stats_f("API_19_DS2_en_csv_v2_4700503.csv",[3,35,40,45,50,55,60,64],"Country Name","India")
print("india/n", india)



def plot_p(DataFrame, col, types, name):
    DataFrame.plot(x=col, rot=45, figsize=(50,25), kind= types, title= name)
    ax.legend(fontsize=36)
    ax.set_title(name,pad=20, fontdict={'fontsize':40})
    return
plot_p(population_c,"Country Name","bar","Total population")
plt.savefig('Total population.jpg')
plot_p(Green_gas_c,"Country Name", "bar","Total greenhouse gas emissions (kt of CO2 equivalent)")
plt.savefig('Total greenhouse gas emissions.jpg')

legend_properties = {'weight':'bold','size':36}
ax1 = Up_y.plot(figsize=(50,25),kind="line",fontsize=36,linewidth=4.0)
ax1.set_title("Total Urban population",pad=20, fontdict={'fontsize':40})
ax1.legend(loc=2,prop=legend_properties)
plt.savefig('Total Urban population line.jpg')


ax2 = co2_y.plot(figsize=(50,25),kind="line",fontsize=36,linewidth=4.0)
ax2.set_title("Total Co2 Emission",pad=30, fontdict={'fontsize':40})
ax2.legend(prop=legend_properties)
plt.savefig('Total Co2 Emission line.jpg')
"""
Up_y.plot(figsize=(20,10),kind="line",title="Total Urban Population")
co2_y.plot(figsize=(20,10),kind="line",title="Total Co2 Emission")
"""
india.corr()
india = india.loc[:,["Population, total","Urban population","Foreign direct investment, net inflows (% of GDP)", "CO2 emissions (kt)"] ]
print(india)

print(india.corr())
'''
india.corr(). style. background_gradient (cmap = 'GnBu')

plt.figure(figsize=(50,25))
plt.imshow( india.corr(), interpolation = 'nearest',cmap="GnBu");

plt.title('Heat map for India',fontsize=46)
plt.xticks([0, 1, 2,3,4], ["Population, total","Urban population","Foreign direct investment, net inflows (% of GDP)","Cereal yield (kg per hectare)","CO2 emissions (kt)"],rotation=90,fontsize=46)
plt.yticks([0, 1, 2,3,4], ["Population, total","Urban population","Foreign direct investment, net inflows (% of GDP)","Cereal yield (kg per hectare)","CO2 emissions (kt)"],fontsize=46)
plt.show()
'''
fig, ax = plt.subplots( figsize=(10,10))
im = ax.imshow(india.corr(),cmap="YlOrBr")
cbar = ax.figure.colorbar(im,
                          ax = ax,
                          shrink=0.5 )
x=["Population, total","Urban population","Foreign direct investment, net inflows (% of GDP)","CO2 emissions (kt)"]
# add tick labels
ax.set_xticks(np.arange(len(x)),
              labels=x,
              size=12)
ax.set_yticks(np.arange(len(x)),
              labels=x,size=12)
# Rotate the tick labels to be more legible
plt.setp(ax.get_xticklabels(),
         rotation = 45,
         ha = "right",
         rotation_mode = "anchor")
ax.set_title("India's Heatmap", size=20)
fig.tight_layout()
plt.savefig("inda's Heatmap.png",
                    format='png',dpi=150)
