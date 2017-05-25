#from scipy import sklearn
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
data = open("inputf.txt", "r")
data1 = open("input_testf.txt", "r")
#print (data.read())
m=np.genfromtxt(data,usecols=(0,1,2,3,4,5,6,7,8,9),delimiter=" ")
m1=np.genfromtxt(data1,usecols=(0,1,2,3,4,5,6,7,8,9),delimiter=" ")

ind=0
a=[0 for x in range(m.shape[0])]
b=[[0 for x in range(9)] for y in range(m.shape[0])]
for i in range (0,m.shape[0]):
	a[ind]=int(m[i][9])
	ind+=1
	for j in range(0,8):
		b[i][j]=m[i][j]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(10,10,10,10,10), random_state=1)

clf.fit(b, a)
b1=[[0 for x in range(9)] for y in range(m1.shape[0])]
a1=[0 for x in range(m1.shape[0])]
for i in range (0,m1.shape[0]):
	a1[i]=int(m1[i][9])
	for j in range(0,8):
		b1[i][j]=m1[i][j]

predicted=clf.predict(b1)
cnt=0
cntt=0
for x in range(0,m1.shape[0]):
	if(predicted[x]==a1[x]):
		cnt+=1
	cntt+=1
print(cnt)
print(cntt)
print(cnt*100.0/cntt*1.0)
