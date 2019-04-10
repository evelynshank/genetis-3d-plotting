#For importing libraries
import matplotlib
#matplotlib.use('Agg')
#Made to recognise requests to generate other output formats (specifically png files) 
#if you want it in a different file format (ex. pdf) you would type 'matplotlib.use('PDF')
import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv

#creating interpol of the data because the z coordinate is being uncooperative
def Interpol(mat):
    thetaExp= np.zeros((2*mat.shape[0]-1,mat.shape[1]))
    
    for i in range(thetaExp.shape[0]):
        if i % 2 == 0:
            thetaExp[i] = mat[(i-1)/2]
        if i % 2 == 1:   
            thetaExp[i] = mat[(i-1)/2]
            

#####################################################
theta=[] 
phi=[] 
gain=[] 
xcoord=[] 
ycoord=[] 
zcoord=[] 
            
with open('3519run.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(plots):
        if i != 0:
            theta.append(float(row[1]))
            phi.append(float(row[2]))
            gain.append(float(row[4]))

theta = np.array(theta)*np.pi/180.
phi = np.array(phi)*np.pi/180.
theta = theta[:325]
phi = phi[:325]
gain = gain[:325]


#converting the spherical coordinates to cartesian coordinates        
xcoord = gain*np.sin(theta)*np.cos(phi)
ycoord = gain*np.sin(theta)*np.sin(phi)
zcoord = gain*np.cos(theta)

#converting xcoord and ycoord into 2d arrays
xMesh = np.ones((xcoord.shape[0], xcoord.shape[0]))*xcoord
yMesh = np.ones((xcoord.shape[0], xcoord.shape[0]))*ycoord

fig = plt.figure(figsize=(13,13))

ax_gainplot = fig.add_subplot(221, projection='3d')
ax_gainplot.plot_surface(xcoord, ycoord, zcoord)
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