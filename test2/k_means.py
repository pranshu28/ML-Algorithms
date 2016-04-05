import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

df = pd.read_csv("household_power_consumption.txt",sep=";")
df.as_matrix()

data=[]
for i in range(2,len(df.columns)):
	data.append([float(t) for t in df[df.columns[i]].values])

x_axis=[int(t) for t in range(len(data[0]))]
y_axis=data[3]
d=np.array([x_axis,y_axis]).T

#number of clusters
k=3

x_min,x_max=np.array(x_axis).min()-1,np.array(x_axis).max()+1
y_min,y_max=np.array(y_axis).min()-1,np.array(y_axis).max()+1

plt.scatter(x_axis,y_axis,marker='x',c='yellow')
clr = np.arange(k)

#Get Labels
def get_labels(data,cent):
	l=[]
	for i in data:
		dist=[]
		for c in cent:
			dist.append((i[0]-c[0])**2 + (i[1]-c[1])**2)
			#print(i[0],c[0],i[1],c[1],(i[0]-c[0])**2,(i[1]-c[1])**2)
		#print(dist,dist.index(min(dist)))
		l.append(dist.index(min(dist)))
	return l

#Get Centroids
def get_cent(data,labels,k):
	data=np.array(data).T
	new_c=[]
	for j in range(k):
		num_x,num_y,den=0,0,0
		for i,l in enumerate(labels):
			if l==j:
				num_x+=data[0][i]
				num_y+=data[1][i]
				den+=1
		if den!=0:
			#print(j,num_x,num_y,den,float(num_x/den),float(num_y/den))
			new_c.append([float(num_x/den),float(num_y/den)])
		else:
			return []
	return new_c

#Generate Random Centroids
cent=[]
for pair in range(k):
	cent.append([random.randint(x_min+1,x_max),random.randint(y_min+1,y_max)])
print(cent)
cent_t=np.array(cent).T
plt.scatter(cent_t[0],cent_t[1],c=clr)

#Iteration
i=1
prev_c=None
while i<=1000 and prev_c!=cent:		#Convergence
	prev_c=cent
	i+=1
	labels=get_labels(d,cent)
	cent=get_cent(d,labels,k)
	cent_t=np.array(cent).T
	plt.scatter(cent_t[0],cent_t[1],c=clr)

print(i)
print(cent)

plt.scatter(cent_t[0],cent_t[1],s=100,c=clr)
plt.xlim(x_min,x_max)
plt.ylim(y_min, y_max)

plt.show()
