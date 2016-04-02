import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv("ds1.10.csv")
df.as_matrix()

no_p=10

data=[[1.0 for w in range(len(df[df.columns[3]]))]]
for i in range(no_p):
	data.append([float(t) for t in df[df.columns[i]].values])
y_axis=[float(t) for t in df[df.columns[10]].values]
#Sigmoid Function
def sigmoid(data):
	h=(1.0/(1.0+math.exp(-data)))
	return h

thetas=np.array([1 for x in range(no_p+1)])
al=.005 
limit=100
for i in range(20):
	print i
	grad_sum=[0.0 for j in range(len(thetas))]
	for k in range(len(y_axis[:limit])):
		y=y_axis[k];
		h=sigmoid(np.dot(np.array(thetas).T,np.array(data).T[k]))
		#print(h,thetas,np.array(data).T[k])
		for j in range(len(thetas)-1):
			grad_sum[j]+=(y-h)*data[j][k]
	thetas=[thetas[l]+(al*grad_sum[l]) for l in range(len(thetas))]
print(thetas)

h=[]
e=[]
for i in range(len(data[3][:limit])):
	h.append(sigmoid(np.dot(np.array(thetas).T,np.array(data).T[i])))
	e.append(y_axis[i]-h[i])
print(np.dot(np.array(thetas).T,np.array(data).T[i]))

for i in range(10):
	plt.scatter(data[i][:limit],e)

plt.ylabel('Success')

plt.show()