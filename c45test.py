import os
import math
import numpy as np
import scipy.stats
from numpy import mean, sqrt, square, arange
data = open('output_c45f.txt', "rb")
ds=np.genfromtxt(data,usecols=(0,1,2,3,4,5),delimiter=" ")
data1=open("input_testf.txt","rb")
m=np.genfromtxt(data1,usecols=(0,1,2,3,4,5,6,7,8,9),delimiter=" ")
#print(ds)
ss=np.array(ds)
numm=m.shape[0]/4
h=[0 for x in range(0,4*numm)]
ans = []
index=0
count2,count1=0,0
def func(row,test):
	#print("row"),
	#print(ss[row][4])
	global h
	global count2
	global count1
	val=row
	if h[test]==1:
		return
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
			#print(test)
			count2+=1
		#print(int(ss[row][5])),
		#print(m[test][9]),
		#print(test),
		#print("hello")
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
for i in range (0,4*numm):
	func(1,i)
	func(2,i)
print("correctly predicted "),
print(count1)
print("incorrectly predicted "),
print(count2)
print("total predicted "),
print(count1+count2)
print("total inputs "),
print(numm*4)
print("Accuracy: "),
print((count1*100.0)/(numm*4.0))
