#from scipy import sklearn
import numpy as np
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
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
	for j in range(0,9):
		b[i][j]=m[i][j]
seed = 7
num_trees = 50
max_features = 6
#kfold = model_selection.KFold(n_splits=10, random_state=seed)
model = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
#model1 = GradientBoostingClassifier(n_estimators=num_trees, random_state=seed)
model.fit(b,a)
#model1.fit(b,a)
b1=[[0 for x in range(9)] for y in range(m1.shape[0])]
a1=[0 for x in range(m1.shape[0])]
for i in range (0,m1.shape[0]):
	a1[i]=int(m1[i][9])
	for j in range(0,9):
		b1[i][j]=m1[i][j]

predicted=model.predict(b1)
cnt=0
cntt=0
for x in range(0,m1.shape[0]):
	if(predicted[x]==a1[x]):
		cnt+=1
	cntt+=1
print(cnt)
print(cntt)
print(cnt*100.0/cntt*1.0)
