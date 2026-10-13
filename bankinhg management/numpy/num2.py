import numpy as np
data=np.genfromtxt('C:/Users/HP/OneDrive/Documents/pythonpractice/bankinhg management/numpy/weather_data.csv', delimiter=',',dtype=None,encoding='utf-8',names=True)
# print(data)
# print(data.dtype) 

## EXTRACT DATA OF CITY
# print(data['City'])

## EXTRACT DATA OF CITY
# print(data['Rainfall'])


## FETCHED COLUMNS 'Temprature, Rainfall, Humidity' 
# a=np.column_stack((data['Temperature'],data['Rainfall'],data['Humidity']))
# print(a)

## HIGHEST TEMPERATURE
# b=np.max(data['Temperature'])
# print('Highest temp :- ', b)

## HIGHEST RAINFALL IN CITY
# c=np.argmax(data['Rainfall'])
# print('Highest rainfall :- ', data['Rainfall'][c])
# print('City :-',data['City'][c])
# delhi=data[data['City']=='Delhi']
# print(delhi['Temperature'].sum())
# kol=data[data['City']=='Kolkata']
# print(kol['Rainfall'].max())
# mum=data[data['City']=='Mumbai']
# print(mum['Humidity'].min())
print()
