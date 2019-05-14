import matplotlib
#For importing libraries
matplotlib.use('Agg')
#Made to recognise requests to generate other output formats (specifically png files) 
#if you want it in a different file format (ex. pdf) you would type 'matplotlib.use('PDF')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv
from scipy.interpolate import interp1d

#creating a function that makes an interpol of the data because the z coordinate is being uncooperative 
'''def Interpol(x, r, newX):
    F = interp1d(x, r, kind="cubic" )
    newG = F(newX)
    return newG

def InterpMat(mat, numTheta, numPhi):
    oldThetaVals= np.arange(0, np.pi, mat.shape[0])
    oldPhiVals= np.arange(0, np.pi, mat.shape[1])
    newThetaVals= np.arange(0, np.pi, numTheta)
    newPhiVals= np.arange(0, 2*np.pi, numPhi)
    
    stretchTheta= np.zeros((numTheta, mat.shape[1]))
    stretchBoth= np.zeros((numTheta, numPhi))
    
    for phiInd in range(mat.shape[1]):
        stretchTheta[:,phiInd] = Interpol(oldThetaVals, mat[:,phiInd], newThetaVals)
    for thetaInd in range(stretchTheta.shape[0]):
        stretchBoth[thetaInd,:] = Interpol(oldPhiVals, mat[thetaInd,:], newPhiVals)
        
    return stretchBoth

mat= np.ones((5,5))
InterpolMat= InterpMat(mat, 10, 10)
print(InterpolMat)'''
        
    
    
'''thetaExp= np.zeros((2*mat.shape[0]-1,mat.shape[1]))
    
    for i in range(thetaExp.shape[0]):
        if i % 2 == 0:
            thetaExp[i] = mat[(i-1)/2]
        if i % 2 == 1:   
            thetaExp[i] = mat[(i-1)/2]'''
#####################################################
theta=[] 
phi=[] 
gain=[] 
thetauan=[]
phiuan=[]
gainuan=[]
thetacsv=[]
phicsv=[]
gaincsv=[]
xcoord=[] 
ycoord=[] 
zcoord=[] 

#reading in the csv file    
'''with open('1_10.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(plots):
        if i != 0:
            thetauan.append(float(row[0]))
            phiuan.append(float(row[1]))
            gainuan.append(10**(float(row[2])/10))'''
            
with open('3519run.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(plots):
        if i != 0:
            thetacsv.append(float(row[1]))
            phicsv.append(float(row[2]))
            gaincsv.append(float(row[4]))
theta=thetauan
phi=phiuan
gain=gainuan

#converting theta and phi to radians and selecting only the first frequency of data 2701
theta = np.array(theta)*np.pi/180.
phi = np.array(phi)*np.pi/180.
theta = theta[:2701]
phi = phi[:2701]
gain = gain[:2701]

#converting the spherical coordinates to cartesian coordinates        
xcoord = gain*np.sin(theta)*np.cos(phi)
ycoord = gain*np.sin(theta)*np.sin(phi)
zcoord = gain*np.cos(theta)

#converting xcoord and ycoord into 2d arrays
xMesh = np.ones((xcoord.shape[0], xcoord.shape[0]))*xcoord
yMesh = np.ones((xcoord.shape[0], xcoord.shape[0]))*ycoord

#making the figures
fig = plt.figure(figsize=(13,13))

ax_gainplot = fig.add_subplot(221, projection='3d')
ax_gainplot.scatter(xcoord, ycoord, zcoord)
ax_gainplot.set_title('Gain Plot')
ax_gainplot.set_xlabel('x')
ax_gainplot.set_ylabel('y')
ax_gainplot.set_zlabel('z')

ax_phaseplot = fig.add_subplot(222, projection= '3d')
ax_phaseplot.scatter(xcoord, ycoord, zcoord)
ax_phaseplot.set_title('Phase Plot')
ax_phaseplot.set_xlabel('x')
ax_phaseplot.set_ylabel('y')
ax_phaseplot.set_zlabel('z')
ax_phaseplot.set_ylim()

#saving the figure as 'plots'
plt.savefig('plots')

#this is the most recent version of this code as of 4/17/19