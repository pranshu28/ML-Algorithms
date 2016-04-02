
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv("Glass.csv")
df.as_matrix()

no_p=9

data=[]
for i in range(no_p):
	data.append([t for t in df[df.columns[i]].values])
y_list=[t for t in df[df.columns[9]].values]

#Gaussiun Discriminant Analysis

#Mean Matrix
def mean(x_list,y,data_y):
	mean_col=[]
	for col in x_list:
		col_dist_y=[]
		for x_ind in range(len(y)):
			if y[x_ind]==data_y:
				col_dist_y.append(col[x_ind])
		#print(dist_y,np.mean(col_dist_y))
		mean_col.append(np.mean(col_dist_y))
		#print("---------")
	return np.array(mean_col).T


#GDA
def gda(x,data_x,y,data_y):
	mean_list=mean(data,y_list,data_y)
	cov_x=np.cov(data)
	#print(mean_list)
	#print(cov_x)
	n=len(cov_x)
	dev=[]
	for i in range(len(data_x)):
		dev.append(data_x[i]-mean_list[i])
	#print(dev)
	den=(((2*math.pi)**n)*np.linalg.det(cov_x))**.5
	exp=math.exp(-.5*np.dot(np.dot(np.array(dev).T,np.linalg.inv(cov_x)),dev))
	#print(np.array(dev).T.shape,np.array(cov_x).shape,np.array(dev).shape)
	#print(1.0/den,exp)
	prob=(1.0/den)*exp
	#print(prob)
	return prob

test=[1.51514,14.01,2.68,3.50,69.89,1.68,5.87,2.10,0.00]
#print(gda(data,test,y_list,1))
for dist in list(set(y_list)):
	ans=gda(data,test,y_list,dist)
	if ans<=1:
		print(dist,ans)
	else:
		print(dist,0)
