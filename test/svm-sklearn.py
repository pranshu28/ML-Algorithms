import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from itertools import groupby

df = pd.read_csv("Indian Liver Patient Dataset (ILPD).csv")
df.as_matrix()

no_p=11

d=[]
for i in range(0,no_p):
	if i!=1:
		d.append([t for t in df[df.columns[i]].values])
gend=[]
for i in df[df.columns[1]].values:
	if i=="Male":
		gend.append(1)
	else:
		gend.append(0)
d.append(gend)
data=np.array(d).T

x_axis=d[0]
y_axis=d[-2]
x=np.array([x_axis,y_axis]).T
target=d[-1]

#plt.hist(x_axis)
svc = svm.SVC(kernel='rbf', gamma=0.7, C=1.0).fit(x, target)
x_min, x_max = np.array(x_axis).min() - 1,np.array(x_axis).max()+ 1
y_min, y_max = np.array(y_axis).min() - 1,np.array(x_axis).max()+ 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),np.arange(y_min, y_max, .02))
Z=svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
plt.scatter(x_axis,y_axis, c=target, cmap=plt.cm.Paired)
plt.xlim(x_min,x_max)
plt.ylim(y_min, y_max)
plt.show()
