import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

url = 'https://datahub.io/core/co2-ppm/r/co2-mm-mlo.csv'
url2='https://pkgstore.datahub.io/JohnSnowLabs/nasa-global-temperature-anomalies-time-series-1880-2017/nasa-global-temperature-anomalies-time-series-1880-2017-csv_csv/data/d0f07b1b1f0f66bd16e07848ac8794cd/nasa-global-temperature-anomalies-time-series-1880-2017-csv_csv.csv'
url3='https://datahub.io/core/sea-level-rise/r/epa-sea-level.csv'
url4='https://pkgstore.datahub.io/core/co2-fossil-global/global_csv/data/09015539c2fc32bb3c4afead7df461b5/global_csv.csv'
co2_ppm = pd.read_csv(url)
temp = pd.read_csv(url2)
sea= pd.read_csv(url3)
fossil=pd.read_csv(url4)


plt.figure(figsize=(10, 5))
x = range(0,co2_ppm.shape[0]) 
y = co2_ppm['Interpolated']
y2=co2_ppm['Trend']
plt.plot( x, y, marker='', color='blue', linewidth=2, linestyle='dashed')
plt.plot( x, y2, marker='', color='red', linewidth=2)
plt.xlabel('Month')
plt.ylabel('Atmospheric CO2 concentration (PPM)')
plt.title('Trends in Atmospheric Carbon Dioxide 1958-2016')
plt.legend()
plt.show()


newco2_ppm=co2_ppm.iloc[10:707,3]
x2 = range(0,newco2_ppm.shape[0]) 
y3 = newco2_ppm
newtemp=temp.iloc[::-1]
y4=[]
for i in range(479,822,6):
    for j in range(2,14):
        y4.append(newtemp.iloc[i,j])
#print(newco2_ppm.shape)
#print(len(y4))
fig, ax1 = plt.subplots()
ax1.set_xlabel('Month')
ax1.set_ylabel('Atmospheric CO2 concentration (PPM)', color='blue')
ax1.plot(x2, y3, color='blue',linewidth=1)
ax1.tick_params(axis='y', labelcolor='blue')
ax2 = ax1.twinx()
ax2.set_ylabel('The average temperature (in Celsius degrees)', color='red') 
ax2.plot(x2, y4, color='red',linewidth=1)
ax2.tick_params(axis='y', labelcolor='red')
plt.title('Logarithmic dependence of temperature on CO2 levels 1949-2016')
fig.tight_layout()
plt.show()


x3 = range(0,sea.shape[0]) 
y5 = sea['CSIRO Adjusted Sea Level']
y6 = sea['Upper Error Bound']
y7 = sea['Lower Error Bound']
plt.figure(figsize=(10, 7))
plt.plot(y6, '--', y7, '--',linewidth=1)
plt.plot( x3, y5, marker='', color='red', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Comulative changes (in inches) in sea level for the world’s oceans(inches)')
plt.title('Global Average Absolute Sea Level Change 1880-2014')
plt.legend(['Upper Error Bound', 'Lower Error Bound', 'CSIRO Adjusted Sea Level'])
plt.gca().fill_between(range(len(x3)),y6, y7,facecolor='blue',alpha=0.25)
plt.show()


y8 = []
y9 = []
y10 = []
y11 = []
y12 = []
for ii in range(fossil.shape[0]):
    y8.append(fossil.iloc[ii,2])
    y9.append(fossil.iloc[ii,3])
    y10.append(fossil.iloc[ii,4])
    y11.append(fossil.iloc[ii,5])
    y12.append(fossil.iloc[ii,6])
yy8=sum(y8)
yy9=sum(y9)
yy10=sum(y10)
yy11=sum(y11)
yy12=sum(y12)
y13=[yy8,yy9,yy10,yy11,yy12]
plt.figure(figsize=(10, 5))
expl = [0,0,0.1,0,0]
labels=['Gas Fuel','Liquid Fuel','Solid Fuel','Cement','Gas Flaring']
plt.pie(y13, explode=expl, labels=labels, autopct='%1.1f%%',pctdistance=0.8, shadow=True)
plt.title('The proportion of Fossil Fuels consumption and cement production for global CO2 emissions 1751-2010', bbox={'facecolor':'0.8', 'pad':5})
plt.show()


x = range(0,fossil.shape[0])
y8 = fossil['Gas Fuel']
y9 = fossil['Liquid Fuel']
y10 = fossil['Solid Fuel']
y11 = fossil['Cement']
y12 = fossil['Gas Flaring']
plt.figure(figsize=(10, 7))
plt.plot( x, y8, marker='', color='blue', linewidth=2)
plt.plot( x, y9, marker='', color='green', linewidth=2)
plt.plot( x, y10, marker='', color='red', linewidth=2)
plt.plot( x, y11, marker='', color='yellow', linewidth=2)
plt.plot( x, y12, marker='', color='brown', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Carbon emissions from fossil fuel consumption and cement production (million metric tons of C)')
plt.title('Global CO2 Emissions from Fossil Fuels consumption and cement production 1751-2010')
plt.legend()
plt.show()