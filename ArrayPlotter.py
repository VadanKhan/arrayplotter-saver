# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:23:09 2022

@author: Student2
"""

#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
name = "16-12_39_54, Disconnect, VK second tests"
fmt = ".csv"
lbnd = 30
upbnd = 70
average = False
graphname = "Disconnect Test"
if average == True:
    graphname = graphname + " avg"
#%%
if average == False:
    raw = np.genfromtxt(name + fmt,dtype='float',delimiter=',',skip_header=2)
else: 
    pass
if average == True:
    raw = np.genfromtxt(name + fmt,dtype='float',delimiter=',',skip_header=4)
else:
    pass
vald = raw[:,6]
print(len(vald))
pred = raw[:,7]
print(len(pred))
deltas = raw[:,10]

datapnts = len(vald)

#%%
adelts = abs(deltas)
avgdelta = np.mean(adelts)
print(avgdelta)
graphname = graphname + ": " + str("{:#.3g}".format(avgdelta))

#%%
time = np.linspace(20, 60, datapnts)
plt.plot(time, vald, label="Validation")
plt.plot(time, pred, label="Prediction")
plt.xlabel('time (seconds)') # creates a label 'x' for the x-axis
plt.ylabel('temperature (°C)') # creates a label 'y' for the y-axis
plt.ylim(lbnd, upbnd)
plt.title('Experiment Live: 3 sensor Numerical Results, ' + graphname)
plt.legend()
plt.show()
plt.savefig(graphname + ".png", dpi=600)

#%%
