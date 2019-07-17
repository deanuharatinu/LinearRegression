"""
16/07/2019

This program calculates the regression equation from the value of X and Y 
inside a .csv file, and plot the result.

This program was converted from my previous C++ program, and some of
the codes were taken from online searches trough the documentations of 
Pandas, Matplotlib, Numpy, and IPython. 

by Deanu Haratinu Tu'u
"""

import numpy as np, pandas as pd, matplotlib.pyplot as plt
from IPython import get_ipython

#Plot the graph on separate window
get_ipython().run_line_magic('matplotlib', 'qt')

#The filename
filename = 'DATA.csv~'
df = pd.read_csv(filename, sep=',')

dfarray = np.array(df)
xar = dfarray[:,0] ; yar = dfarray[:,1]
total = xar * yar

for count, i in enumerate(total):
    totalxy = sum(total)          #Sum of X*Y   
    totalx = sum(xar)             #Sum of X
    totalxx = sum(np.square(xar)) #Sum of X^2
    totaly = sum(yar)             #Sum of Y
    totalyy = sum(np.square(yar)) #Sum of Y^2
    data = count + 1              #Count the total data inside .csv file
    
squarex = np.square(totalx)       #Square of sum X 
squarey = np.square(totaly)       #Square of sum Y

#Calculating the a and b
b = ((data*totalxy)-(totalx*totaly)) / ((data*totalxx)-(squarex)) 
a = ((totalxx*totaly)-totalx*totalxy) / ((data*totalxx)-(squarex))

#Print the Regression equation
print('The regression equation is \n   Y = ' 
      + str(round(b,3)) + 'X + ' + str(round(a, 3))) 

#Processing the value to be plot
minxar = min(xar)
maxxar = max(xar)
X = np.round(np.linspace(minxar-3,maxxar+3,num=5),3)
Y = (round(b,3)*X) + (round(a,3))

plt.grid()
plt.scatter(xar, yar)
plt.plot(X,Y)
plt.ylabel('Y Axis'); plt.xlabel('X Axis')
plt.show()