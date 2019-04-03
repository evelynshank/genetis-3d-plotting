#For importing libraries
import matplotlib
matplotlib.use('Agg')
#Made to recognise requests to generate other output formats (specifically png files) 
#if you want it in a different file format (ex. pdf) you would type 'matplotlib.use('PDF')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np
import csv

#####################################################

theta=[]
phi=[]
gain=[]
thetarad=[]
phirad=[]
xcoord=[]
ycoord=[]
zcoord=[]

#adding the data of the first frequency from the csv file to the arrays
with open('3519run.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    next(plots, None)
    for row in plots:
        if row != 0:
            theta.append(float(row[1]))
            phi.append(float(row[2]))
            gain.append(float(row[4]))

theta = theta[:325]
phi = phi[:325]
gain = gain[:325]

#converting into radians
for i in range(len(theta)):

        thetarad.append(theta[i]*math.pi/180)

        phirad.append(phi[i]*math.pi/180)
        
#converting the spherical coordinates to cartesian coordinates        
xcoord = gain*np.sin(thetarad)*np.cos(phirad)
ycoord = gain*np.sin(thetarad)*np.sin(phirad)
zcoord = gain*np.cos(thetarad)

#converting xcoord, ycoord, and zcoord into 2d arrays
xcoord, ycoord = np.meshgrid(xcoord, ycoord)


EmptySq= np.arange(zcoord).reshape(325,325)

EmptySquare= np.ones((325,325))
x= (EmptySquare*xcoord)
y= (EmptySquare*ycoord).T


fig = plt.figure(figsize=(13,13))

ax_gainplot = fig.add_subplot(221, projection='3d')
ax_gainplot.scatter(xcoord, ycoord, zcoord)
ax_gainplot.set_title('Gain Plot')
ax_gainplot.set_xlabel('Theta')
ax_gainplot.set_ylabel('Phi')
ax_gainplot.set_zlabel('Gain')

ax_phaseplot = fig.add_subplot(222, projection= '3d')
ax_phaseplot.scatter(xcoord, ycoord, zcoord)
ax_phaseplot.set_title('Phase Plot')
ax_phaseplot.set_xlabel('Theta')
ax_phaseplot.set_ylabel('Phi')
ax_phaseplot.set_zlabel('Phase')
ax_phaseplot.set_ylim()


plt.savefig('plots')

#added and saved

#this is the most recent version of this code as of 4/3/19