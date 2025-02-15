#Author: Abhigna Isukamatla
#this code is written on 10/29/2024. It determines the airlines with the most dangerous flights.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv('airline-safety.csv')
dataframe.sort_values('fatal_accidents_00_14')
dataframe.sort_values('incidents_00_14')

#ratio calculator
def ratio_calculator(column_one,column_two):
    result = column_one/column_two
    return result
column_one = dataframe['incidents_00_14']
colum_two = dataframe['avail_seat_km_per_week']

#judging basing on no. of incidents
dataframe['incidents_per_seat']= ratio_calculator(column_one,colum_two)
#sorted data
sorted = dataframe['incidents_per_seat'].sort_values(ascending=False)
print(sorted)
#bargraph
plt.figure(figsize=(12, 8))
plt.barh(dataframe['airline'],dataframe['incidents_per_seat'],color='red')
plt.yticks(rotation=0, fontsize=6)
plt.xlabel('Incidents Rate')
plt.ylabel('Airline')
plt.title('Airlines and no. of Incidents from 2000 to 2014')
plt.show()

#judging basing on fatal accidents
dataframe['fatal_accidents_per_seat']= ratio_calculator(dataframe['fatal_accidents_00_14'],dataframe['avail_seat_km_per_week'])
sorted2 = dataframe['fatal_accidents_per_seat'].sort_values(ascending=False)
print(sorted2)
#bargraph2
plt.figure(figsize=(12, 8))
plt.barh(dataframe['airline'],dataframe['fatal_accidents_per_seat'],color='blue')
plt.yticks(rotation=0, fontsize=6)
plt.xlabel('fatal accidents Rate')
plt.ylabel('Airline')
plt.title('Airlines and no. of fatal Accidents from 2000 to 2014')
plt.show()

#judging basing on the number of fatalities from 2000 to 2014
dataframe['fatalities_per_seat']= ratio_calculator(dataframe['fatalities_00_14'],dataframe['avail_seat_km_per_week'])
sorted3 = dataframe['fatalities_per_seat'].sort_values(ascending=False)
print(sorted3)
#bargraph
plt.figure(figsize=(12, 8))
plt.barh(dataframe['airline'],dataframe['fatalities_per_seat'],color='yellow')
plt.yticks(rotation=0, fontsize=6)
plt.xlabel('fatalities Rate')
plt.ylabel('Airline')
plt.title('Airlines and no. of fatalities from 2000 to 2014')
plt.show()

#judging basing on the number of incidents in incidents in 1985 and 1999
dataframe['incidents_per_seat_85_99']= ratio_calculator(dataframe['incidents_85_99'],dataframe['avail_seat_km_per_week'])
sorted4 = dataframe['incidents_per_seat_85_99'].sort_values(ascending=False)
print(sorted4)
#bargraph3
plt.figure(figsize=(12, 8))
plt.barh(dataframe['airline'],dataframe['incidents_per_seat_85_99'],color='red')
plt.yticks(rotation=0, fontsize=6)
plt.xlabel('Incidents_85_99 Rate')
plt.ylabel('Airline')
plt.title('Airlines and no. of Incidents from 1985 to 1999')
plt.show()

#judging basing on fatal accidents in 1985 and 1989
dataframe['fatal_accidents_per_seat_85_99']= ratio_calculator(dataframe['fatal_accidents_85_99'],dataframe['avail_seat_km_per_week'])
sorted5 = dataframe['fatal_accidents_per_seat_85_99'].sort_values(ascending=False)
print(sorted5)
#bargraph
plt.figure(figsize=(12, 8))
plt.barh(dataframe['airline'],dataframe['fatal_accidents_per_seat_85_99'],color='blue')
plt.yticks(rotation=0, fontsize=6)
plt.xlabel('fatal accidents Rate_85_99')
plt.ylabel('Airline')
plt.title('Airlines and no. of fatal Accidents from 1985 to 1999')
plt.show()

#judging basing on the number of fatalities from 1985 to 1989
dataframe['fatalities_per_seat_85_99']= ratio_calculator(dataframe['fatalities_85_99'],dataframe['avail_seat_km_per_week'])
sorted6 = dataframe['fatalities_per_seat_85_99'].sort_values(ascending=False)
print(sorted6)
#bargraph
plt.figure(figsize=(12, 8))
plt.barh(dataframe['airline'],dataframe['fatalities_per_seat_85_99'],color='yellow')
plt.yticks(rotation=0, fontsize=6)
plt.xlabel('fatalities Rate_85_99')
plt.ylabel('Airline')
plt.title('Airlines and no. of fatalities from 1985 to 1999')
plt.show()






