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
phase=[]
thetarad=[]
phirad=[]
xcoord=[]
ycoord=[]
zcoord=[]

with open('2uan.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        theta.append(int(row[0]))
        phi.append(int(row[1]))
        gain.append(float(row[2]))
        phase.append(float(row[3]))
        

for i in range(len(theta)):

        thetarad.append(theta[i]*math.pi/180)

        phirad.append(phi[i]*math.pi/180)
        
        
xcoord = gain*np.sin(thetarad)*np.cos(phirad)
ycoord = gain*np.sin(thetarad)*np.sin(phirad)

xcoord, ycoord = np.meshgrid(xcoord, ycoord)

zcoord = gain*np.cos(thetarad)

'''EmptySq= np.arange(zcoord).reshape(325,325)

EmptySquare= np.ones((325,325))
x= (EmptySquare*xcoord)
y= (EmptySquare*ycoord).T

thetarad= np.array(thetarad).reshape((len(thetarad),1))
phirad= np.array(phirad).reshape((len(thetarad),1))
gain= np.array(gain).reshape((len(thetarad),1))'''

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