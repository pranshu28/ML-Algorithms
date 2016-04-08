import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import mixture

df = pd.read_csv("household_power_consumption.txt",sep=";")
df.as_matrix()

data=[]
for i in range(2,len(df.columns)):
	data.append([float(t) for t in df[df.columns[i]].values])

x_axis=[int(t) for t in range(len(data[0]))]
y_axis=data[3]
d=np.array([x_axis,y_axis]).T

x_min,x_max=np.array(x_axis).min()-1,np.array(x_axis).max()+1
y_min,y_max=np.array(y_axis).min()-1,np.array(y_axis).max()+1

plt.scatter(x_axis,y_axis,marker='x',c='yellow')

em = mixture.GMM(n_components=2, covariance_type='full')
em.fit(d)
x = np.linspace(x_min,x_max)
y = np.linspace(y_min,y_max)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -em.score_samples(XX)[0]
Z = Z.reshape(X.shape)
CS = plt.contour(X, Y, Z,levels=np.logspace(0, 3, 10))
CB = plt.colorbar(CS, shrink=0.8, extend='both')

plt.xlim(x_min,x_max)
plt.ylim(y_min, y_max)

plt.show()
