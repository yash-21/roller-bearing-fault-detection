import os
#import a
import math
import numpy as np
import scipy.stats
from numpy import mean, sqrt, square, arange
from operator import itemgetter, attrgetter
def entropy(n1,n2,n3,n4):
	s=(n1+n2+n3+n4)*1.0
	if(n1==0):
		n1=s
	if(n2==0):
		n2=s
	if(n3==0):
		n3=s
	if(n4==0):
		n4=s
        if(s==0): 
                e=0
        else:
                e=-( ( (n1/s)*math.log(n1/s,2) ) + ( (n2/s)*math.log(n2/s,2) ) +  ( (n3/s)*math.log(n3/s,2) ) + ( (n4/s)*math.log(n4/s,2) ) )
	return e
numm=0
numfinal=0
k=0
strng=["Kurtosis" , "Skewness" , "rms" , "variance" , "max" , "crest factor", "mean" , "impulse factor" , " shape factor" , "result", "location"]
fille= open("output_id31.txt",'w')
ans = []
index=0
data = open("inputf.txt", "r")
#print (data.read())
m=np.genfromtxt(data,usecols=(0,1,2,3,4,5,6,7,8,9),delimiter=" ")
numm=m.shape[0]/4
print(numm)
print(m)
h=[0 for x in range(0,4*numm)]
def id3(mat,n,p,sa,sv):
	global strng
	global h
	global numm
	global numfinal
	global ans
	global index
	num1,num2,num3,num4=0,0,0,0
	for x in range (0,n):
		if(mat[x][9]==0):
			num1+=1
		if(mat[x][9]==1):
			num2+=1
		if(mat[x][9]==2):
			num3+=1
		if(mat[x][9]==3):
			num4+=1
	if(num1==n or num2==n or num3==n or num4==n):
		numfinal+=n
		ans.append([])
		print("classifying"),
		ans[index].append(n)
		ans[index].append(numfinal)
		ans[index].append(sa)
		ans[index].append(sv)
		ans[index].append(p)
		print(n),
		print(numfinal),
		print(strng[sa]),
		print(sv),
		print(p),
		if(num1==n):
			print("0")
			ans[index].append(0)
		elif(num2==n):
			print("1")
			ans[index].append(1)
		elif(num3==n):
			print("2")
			ans[index].append(2)
		else:
			print("3")
			ans[index].append(3)
		index+=1
		return
	else:
		ans.append([])
		ans[index].append(0)
		ans[index].append(numfinal)
		ans[index].append(sa)
		ans[index].append(sv)
		ans[index].append(p)
		ans[index].append(-1)
		index+=1
	if(numfinal>=4*numm):
		return
	b=[[0 for x in range(10)] for y in range(n)]
	matf=[[0 for x in range(10)] for y in range(n)]
	mini=1000000000
	indi=-1
	indj=-1
	matf=mat
	flag=0
	b=mat
	for i in range (0,9):
		b=np.array(sorted(b, key=lambda  l:l[i]))
		for k in range (1,n):
			n1,n2,n3,n4=0,0,0,0
			for l in range (0,k):
				if(b[l][9]==0):
					n1+=1
				elif(b[l][9]==1):
					n2+=1
				elif(b[l][9]==2):
					n3+=1
				else:
					n4+=1
			ent=entropy(n1,n2,n3,n4)
			n1,n2,n3,n4=0,0,0,0
			for l in range (k,n):
				if(b[l][9]==0):
					n1+=1
				elif(b[l][9]==1):
					n2+=1
				elif(b[l][9]==2):
					n3+=1
				else:
					n4+=1
			entu=entropy(n1,n2,n3,n4)
			gain=(k)/(n*1.0)*ent+((n)-k)/(n*1.0)*entu
			if(mini>gain):
				mini=gain
				indi=i
				indj=k
	z=0
	matf=np.array(sorted(mat, key=lambda  l:l[indi]))
	m1=[[0 for x in range(10)] for y in range(indj)]
	for x in range(0,indj):
		for y in range(0,10):
			m1[z][y]=float(matf[x][y])
		z+=1	
	id3(m1,z,2*p,indi,float(matf[indj][indi]))
	m2=[[0 for x in range(10)] for y in range(n-indj)]
	z=0
	for x in range(indj,n):
		for y in range(0,10):
			m2[z][y]=float(matf[x][y])
		z+=1
	id3(m2,z,2*p+1,indi,float(matf[indj][indi]))
id3(m,4*numm,1,-1,0)
print("Number of rows classified: "),
print(numfinal)
#sorted(ans, key=itemgetter(4))
ans=sorted(ans,key=lambda x: x[4])
for i in range (0,index):
	print >>fille,(ans[i])
	print(ans[i])
