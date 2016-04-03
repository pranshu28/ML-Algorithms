import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv("household_power_consumption.txt",sep=";")
df.as_matrix()

data=[]
for i in range(2,len(df.columns)):
	data.append([float(t) for t in df[df.columns[i]].values])

d=np.array(data).T

x_axis=[int(t) for t in range(len(data[0]))]
y_axis=data[3]

x_min, x_max = np.array(x_axis).min() - 1,np.array(x_axis).max()+ 1
y_min, y_max = np.array(y_axis).min() - 1,np.array(x_axis).max()+ 1

plt.scatter(x_axis,y_axis)

plt.xlim(x_min,x_max)
#plt.ylim(y_min, y_max)

plt.show()
