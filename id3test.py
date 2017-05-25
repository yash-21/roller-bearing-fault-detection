
import os
import math
import numpy as np
import scipy.stats
from numpy import mean, sqrt, square, arange
data = open('output_id3f.txt', "rb")
data1=open('input_testf.txt',"rb")
ds=np.genfromtxt(data,usecols=(0,1,2,3,4,5),delimiter=" ")
m=np.genfromtxt(data1,usecols=(0,1,2,3,4,5,6,7,8,9),delimiter=" ")
numm=m.shape[0]/4
#print(ds)
ss=np.array(ds)
h=[0 for x in range(0,4*numm)]
ans = []
index=0
count2,count1=0,0
def func(row,test):
	global h
	global count2
	global count1
	val=row
	if h[test]==1:
		return
	#print("row"),
	#print(row)
	if int(ss[row][4])%2==0:
		if m[test][int(ss[row][2])] >= ss[row][3]:
			return
	else:
		if m[test][int(ss[row][2])] < ss[row][3]:
			return 				

	if(int(ss[row][5]!=-1)):
		h[test]=1
		if(ss[row][5]==m[test][9]):
			count1+=1
		else:
			count2+=1
		return
	 
	else:
		if int(ss[row][4])%2==0:
			if m[test][int(ss[row][2])] < ss[row][3]:
				for i in range(0,len(ss)):
					if int(ss[i][4]) == int(ss[row][4])*2:
						val=i
						break
				func(val,test)
				func(val+1,test)
			else:
				return
		else:
			if m[test][int(ss[row][2])] >= ss[row][3]:
				for i in range(0,len(ss)):
					if int(ss[i][4]) == int(ss[row][4])*2:
						val=i
						break
				func(val,test)
				func(val+1,test)
			else:
				return
for i in range (0,numm*4):
	func(1,i)
	func(2,i)
print(count1)
print(count2)
print(count1+count2)
print(numm*4)
print("Accuracy: "),
print((count1*100.0)/(numm*4.0))
