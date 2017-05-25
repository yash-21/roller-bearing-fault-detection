from random import random
import numpy as np
import os
import math
import scipy.stats
from numpy import mean, sqrt, square, arange
fille= open("dataset.txt",'w')
numm=0
path = '/home/kabir/bearing_fault/1st_test'
for fi in os.listdir(path):
	numm+=1
print(numm)
path1= '/home/kabir/bearing_fault/2nd_test'
for fi in os.listdir(path1):
	numm+=1
print(numm)
path2 = '/home/kabir/bearing_fault/4th_test/txt'
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
			if(j==0 or j==2):
				m[k][0]=0
			elif(j==4):
				m[k][0]=1
			else:
				m[k][0]=2
			m[k][1]=scipy.stats.kurtosis(a, axis=0, fisher=False, bias=False) #kurtosis
			m[k][2]=scipy.stats.skew(a, axis=0, bias=False) #skewness
			m[k][3]=sqrt(mean(square(a))) #rms
			m[k][4]=np.var(a) #variance
			m[k][5]=max(a) #max value
			m[k][6]=m[k][5]/m[k][3] #crest factor
                        m[k][7]=mean(a)  #mean
			m[k][8]=m[k][5]/m[k][7] #impulse factor
			m[k][9]=m[k][3]/m[k][7] #shape factor
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
			if(j==3 or j==1 or j==2):
				m[k][0]=0
			elif(j==0):
				m[k][0]=3
			m[k][1]=scipy.stats.kurtosis(a, axis=0, fisher=False, bias=False) #kurtosis
			m[k][2]=scipy.stats.skew(a, axis=0, bias=False) #skewness
			m[k][3]=sqrt(mean(square(a))) #rms
			m[k][4]=np.var(a) #variance
			m[k][5]=max(a) #max value
			m[k][6]=m[k][5]/m[k][3] #crest factor
                        m[k][7]=mean(a)  #mean
			m[k][8]=m[k][5]/m[k][7] #impulse factor
			m[k][9]=m[k][3]/m[k][7] #shape factor
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
				if(j==0 or j==1 or j==3):
					m[k][0]=0
				elif(j==2):
					m[k][0]=3
			m[k][1]=scipy.stats.kurtosis(a, axis=0, fisher=False, bias=False) #kurtosis
			m[k][2]=scipy.stats.skew(a, axis=0, bias=False) #skewness
			m[k][3]=sqrt(mean(square(a))) #rms
			m[k][4]=np.var(a) #variance
			m[k][5]=max(a) #max value
			m[k][6]=m[k][5]/m[k][3] #crest factor
                        m[k][7]=mean(a)  #mean
			m[k][8]=m[k][5]/m[k][7] #impulse factor
			m[k][9]=m[k][3]/m[k][7] #shape factor	
			k+=1
for i in range (0,4*numm):
	print >>fille,m[i][0],
	for j in range (1,10):
		print>>fille,str(j) + ":" + str(m[i][j]),
	print>>fille,'' 
