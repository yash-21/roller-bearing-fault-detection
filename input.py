from random import random
import numpy as np
import os
import math
import scipy.stats
from numpy import mean, sqrt, square, arange
fille= open("input.txt",'w')
numm=0
path = '/home/kabir/bearing_fault/1_train'
for fi in os.listdir(path):
	numm+=1
print(numm)
path1= '/home/kabir/bearing_fault/2_train'
for fi in os.listdir(path1):
	numm+=1
print(numm)
path2 = '/home/kabir/bearing_fault/3_train'
for fi in os.listdir(path2):
	numm+=1
print(numm)
k=0
cnt=0
m=[[0 for x in range(10)] for y in range(numm*4)]
for filename in os.listdir(path):
	current = os.path.join(path, filename)
	if os.path.isfile(current):
        	data = open(current, "r")
		cnt+=1
         	#print (data.read())
	   	ds=np.genfromtxt(data,usecols=(0,1,2,3,4,5,6,7),delimiter="\t")
		print("Reading File No.-"),
		print(cnt)
	   	#print(type(ds))
		#print(ds.shape)
		a=[0 for x in range(0,ds.shape[0]*2)]
		for j in range(0,ds.shape[1],2):
			for i in range(0,ds.shape[0]):
				a[i]=ds[i][j]
				a[i+ds.shape[0]]=ds[i][j+1]
			m[k][0]=scipy.stats.kurtosis(a, axis=0, fisher=False, bias=False) #kurtosis
			m[k][1]=scipy.stats.skew(a, axis=0, bias=False) #skewness
			m[k][2]=sqrt(mean(square(a))) #rms
			m[k][3]=np.var(a) #variance
			m[k][4]=max(a) #max value
			m[k][5]=m[k][4]/m[k][2] #crest factor
                        m[k][6]=mean(a)  #mean
			m[k][7]=m[k][4]/m[k][6] #impulse factor
			m[k][8]=m[k][2]/m[k][6] #shape factor
			if(j==0 or j==2):
				m[k][9]=0
			elif(j==4):
				m[k][9]=1
			else:
				m[k][9]=2
			k+=1
cnt=0
for filename in os.listdir(path1):
	current = os.path.join(path1, filename)
	if os.path.isfile(current):
        	data = open(current, "r")
		cnt+=1
         	#print (data.read())
	   	ds=np.genfromtxt(data,usecols=(0,1,2,3),delimiter="\t")
		print("Reading File No.-"),
		print(cnt)
	   	#print(type(ds))
		#print(ds.shape)
		a=[0 for x in range(0,ds.shape[0])]
		for j in range(0,ds.shape[1]):
			for i in range(0,ds.shape[0]):
				a[i]=ds[i][j]
			m[k][0]=scipy.stats.kurtosis(a, axis=0, fisher=False, bias=False) #kurtosis
			m[k][1]=scipy.stats.skew(a, axis=0, bias=False) #skewness
			m[k][2]=sqrt(mean(square(a))) #rms
			m[k][3]=np.var(a) #variance
			m[k][4]=max(a) #max value
			m[k][5]=m[k][4]/m[k][2] #crest factor
                        m[k][6]=mean(a)  #mean
			m[k][7]=m[k][4]/m[k][6] #impulse factor
			m[k][8]=m[k][2]/m[k][6] #shape factor
			if(j==3 or j==1 or j==2):
				m[k][9]=0
			elif(j==0):
				m[k][9]=3
			k+=1
cnt=0
for filename in os.listdir(path2):
	current = os.path.join(path2, filename)
	if os.path.isfile(current):
        	data = open(current, "r")
		cnt+=1
         	#print (data.read())
	   	ds=np.genfromtxt(data,usecols=(0,1,2,3),delimiter="\t")
		print("Reading File No.-"),
		print(cnt)
	   	#print(type(ds))
		#print(ds.shape)
		a=[0 for x in range(0,ds.shape[0])]
		for j in range(0,ds.shape[1]):
			for i in range(0,ds.shape[0]):
				a[i]=ds[i][j]
			m[k][0]=scipy.stats.kurtosis(a, axis=0, fisher=False, bias=False) #kurtosis
			m[k][1]=scipy.stats.skew(a, axis=0, bias=False) #skewness
			m[k][2]=sqrt(mean(square(a))) #rms
			m[k][3]=np.var(a) #variance
			m[k][4]=max(a) #max value
			m[k][5]=m[k][4]/m[k][2] #crest factor
                        m[k][6]=mean(a)  #mean
			m[k][7]=m[k][4]/m[k][6] #impulse factor
			m[k][8]=m[k][2]/m[k][6] #shape factor
			if(j==0 or j==1 or j==3):
				m[k][9]=0
			elif(j==2):
				m[k][9]=3
			k+=1
for i in range (0,4*numm):
	print >>fille,(m[i])
