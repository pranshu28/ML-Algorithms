import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import random

df = pd.read_csv("Ground Water Survey.csv")
df.as_matrix()

X=[float(t) for t in df[df.columns[0]].values]
axis=[float(t) for t in df[df.columns[1]].values]

#sigmoid function
def sigmoid(data):
	g=(1.0/(1.0+math.exp(-data)))
	return g

#Length of training set
m=len(X)

n=m

#Learning rate
alpha=.0026

#Initialize W (n*m)
W=[]
for j in range(n):
	r=[]
	for i in range(m):	
		r.append(random.random())
	W.append(r)

#Stochastic Gradient Ascent
def sga(W,X):
	ga=[]
	row=[]
	for j in range(n):
		wx=np.dot(np.array(W[j]),np.array(X).T)
		row.append(1-2*sigmoid(wx))
	#print(np.array(row),np.array(X).reshape(1,m))
	#print(np.dot(np.array(row),np.array(X)))
	#print(np.linalg.inv(np.array(W).T))
	ga=np.dot(np.array(row).reshape(n,1),np.array(X).reshape(1,m))+np.linalg.inv(np.array(W).T)
	return ga

#Learning
t=1
while t<10000:
	prev_W=W
	W=W+alpha*sga(W,X)
	t+=1
print(W)

#Source
S=np.dot(np.array(W),np.array(X))
print(S)

W=np.array(W).T
Y=[]
for i in range(m):
	Y.append(np.dot(np.array(W[i]),np.array(S).T))


fig=plt.figure()

ax1=fig.add_subplot(211)
ax1.scatter(axis,X,marker='x',c='red')		#Graph for X
ax2=fig.add_subplot(212)
ax2.scatter(axis,Y)							#Graph for Y

plt.show()