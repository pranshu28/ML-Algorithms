import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv("household_power_consumption.txt",sep=";")
df.as_matrix()

data=[]
for i in range(len(df.columns)):
	data.append([t for t in df[df.columns[i]].values])
data=np.array(data).T

#print(data)

