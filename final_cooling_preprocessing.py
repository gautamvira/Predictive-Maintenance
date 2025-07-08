import numpy as np
import pandas as pd
import random as rand
import matplotlib.pyplot as plt
import random

dsets = []
for i in range(31,39):         #Creating a list of all the datasets
    dsets.append(pd.read_csv(r'Generated_cooling_sys\synthetic_cooling+'+str(i)+'.csv'))

print(dsets[1].head())

import math
for i, df in enumerate(dsets):
    prob = random.random()
    dsets[i] = dsets[i].drop(['Unnamed: 0', 'example_id'], axis=1)       #Dropping irrelevant columns created during generation
    for index,rows in dsets[i].iterrows():                               #Making sure that the values are in the accepted ranges
        if(rows[0] < -40):
            rows[0] = -40
        elif(rows[0] > 210):
            rows[0] = 210
        if(rows[1] < 0):
            rows[1] = 0
        elif(rows[1]>100):
            rows[1] = 100
        if(rows[2] < 0):
            rows[2] = 0
        elif(rows[2] > 8031.875):
            rows[2] = 8031.875

print(dsets[1].head())

#Function to plot moving average graph
def moving_avg(x, N=1000):
    return np.convolve(x, np.ones((N,))/N, mode='valid')

plt.figure(figsize=(15,5))
plt.plot(dsets[0]['65262-110'], linewidth = 1, alpha = 0.5, label = 'Actual')
plt.plot(moving_avg(dsets[0]['65262-110'], 1000), 'C0', label = 'moving average, N = 1000')
plt.xlim(0,len(dsets[0]['65262-110']))
plt.ylim(60, 100)
plt.title('Before dip - Coolant Temperature (Celsius) - Synthetic')
plt.legend()
plt.figure(figsize=(15,5))
plt.plot(dsets[0]['64817-1598'], linewidth = 1, alpha = 0.5, label = 'Actual')
plt.plot(moving_avg(dsets[0]['64817-1598'], 1000), 'C0', label = 'moving average, N = 1000')
plt.xlim(0,len(dsets[0]['64817-1598']))
plt.ylim(4040, 4100)
plt.title('Before Turning off - Fan speed (rpm) - Synthetic')
plt.legend()

for k in range(len(dsets)):
    '''
    Introducing the behavior of coolant temperature dipping.
    '''
    flag = True
    counter = int(len(dsets[k])/5)
    for i in range(len(dsets[k])):
            prob = random.random()

            if(dsets[0].iloc[i, 2] != 0):           #Making sure fan values are constant when on
                dsets[0].iloc[i, 2] = 4096.0

            if((prob <= 0.00009) and (i > (counter+8000)) and (i < int(len(dsets[k]) - (len(dsets[k]) * 0.20))) and (dsets[k].iloc[i,0] >= 86.0)):
                if flag == True:
                    dipsize = random.randrange(4, 28, 1)
                else:
                    dipsize = random.randrange(4, 15, 1)
                row = dsets[k].iloc[i]
                currval = row[0]
                tarval = currval - int((dipsize/100)*currval)
                if(dipsize <= 10):
                    first = 600
                    second = 600
                    third = 920
                elif(dipsize <= 12):
                    first = 1200
                    second = 1000
                    third = 2100
                else:
                    if dipsize > 20:
                        flag = False
                    first = 2800
                    second = 2400
                    third = 5000

                for j in range(i, i+first, 1):                       #decrease in temperature
                    sub = random.randint(0,100)
                    if((0 <= sub < 2) and (currval < row[0])):
                        dsets[k].iloc[j, 0] = currval + 1
                    elif((5 <= sub <= 9) and (currval > tarval)):
                        dsets[k].iloc[j, 0] = currval - 1
                    else:
                        dsets[k].iloc[j, 0] = currval
                    currval = dsets[k].iloc[j, 0]

                fandrop = random.randrange(1,7,1)
                for j in reversed(range(i+first, i+first+fandrop,1)):             #Introducing fan turning off
                    dsets[k].iloc[j, 2] = 0
                fandrop = random.randrange(1,7,1)
                for j in range(i+second, i+second+fandrop,1):             #Introducing fan turning off
                    dsets[k].iloc[j, 2] = 0

                for j in range(i+first, i+third, 1):                  #Rise in temperature
                    sub = random.randint(0,100)
                    if((0 <= sub < 2) and (currval > tarval)):
                        dsets[k].iloc[j, 0] = currval - 1
                    elif((5 <= sub <= 9) and (currval < 92)):
                        dsets[k].iloc[j, 0] = currval + 1
                    else:
                        dsets[k].iloc[j, 0] = currval
                    currval = dsets[k].iloc[j, 0]
                    counter = j
plt.figure(figsize=(15,5))                
plt.plot(dsets[0]['65262-110'], linewidth = 1, alpha = 0.5, label = 'Actual')
plt.plot(moving_avg(dsets[0]['65262-110'], 1000), 'C0', label = 'moving average, N = 1000')
plt.xlim(0,len(dsets[0]['65262-110']))
plt.ylim(60, 100)
plt.title('After Dip - Coolant Temperature (Celsius) - Synthetic')
plt.legend()
plt.figure(figsize=(15,5))
plt.plot(dsets[0]['64817-1598'], linewidth = 1, alpha = 0.5, label = 'Actual')
plt.plot(moving_avg(dsets[0]['64817-1598'], 1000), 'C0', label = 'moving average, N = 1000')
plt.xlim(0,len(dsets[0]['64817-1598']))
plt.ylim(4040, 4100)
plt.title('After Turning Off - Fan speed (rpm) - Synthetic')
plt.legend()
plt.figure(figsize=(15,5))                
plt.plot(dsets[1]['65262-110'], linewidth = 1, alpha = 0.5, label = 'Actual')
plt.plot(moving_avg(dsets[1]['65262-110'], 1000), 'C0', label = 'moving average, N = 1000')
plt.xlim(0,len(dsets[1]['65262-110']))
plt.ylim(60, 100)
plt.title('After Dip - Coolant Temperature (Celsius) - Synthetic')
plt.legend()
plt.figure(figsize=(15,5))
plt.plot(dsets[1]['64817-1598'], linewidth = 1, alpha = 0.5, label = 'Actual')
plt.plot(moving_avg(dsets[1]['64817-1598'], 1000), 'C0', label = 'moving average, N = 1000')
plt.xlim(0,len(dsets[1]['64817-1598']))
plt.ylim(4040, 4100)
plt.title('After Turning Off - Fan speed (rpm) - Synthetic')
plt.legend()

for i in range(len(dsets)):                     #Changing coolant levels for robustness
    vals = random.random()
    if(vals <= 0.3):
        inc = random.randint(5,15)
        dsets[i]['65263-111'] += inc
    elif(0.30 <= vals <= 0.45):
        inc = random.randint(15,30)
        dsets[i]['65263-111'] += inc

#Saving all the modified datasets
path = r'cool_tests'
for i in range(len(dsets)):         #Creating a list of all the datasets
    dsets[i].to_csv(path+'\\final_cooling_dset_test_'+str(i)+'.csv')

plt.show()
