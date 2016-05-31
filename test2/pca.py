import pandas as pd
import numpy as np

df = pd.read_csv("Glass.csv")
df.as_matrix()

no_p=9

data=[]
for i in range(no_p):
	data.append([t for t in df[df.columns[i]].values])

#Eigen values and Vectors of Covariance Matrix
eigval,eigvec=np.linalg.eig(np.array(np.cov(np.array(data))))
arr=[]
for i in range(no_p):
	arr.append([eigval[i],eigvec[i]])

#No. of dimensions
k=2

#Dimensionally reduced vectors
sort=sorted(arr,key=lambda x: x[0])[-k:]
W=[]
for i in range(k):
	W.append(sort[i][1])
W=np.array(W).T

print(W)

data=[]
for i in range(no_p):
	data.append([t for t in df[df.columns[i]].values])

#Eigen values and Vectors of Covariance Matrix
eigval,eigvec=np.linalg.eig(np.array(np.cov(np.array(data))))
arr=[]
for i in range(no_p):
	arr.append([eigval[i],eigvec[i]])

#No. of dimensions
k=2

#Dimensionally reduced vectors
sort=sorted(arr,key=lambda x: x[0])[-k:]
W=[]
for i in range(k):
	W.append(sort[i][1])
W=np.array(W).T

print(W)
