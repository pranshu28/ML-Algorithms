import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv("household_power_consumption.txt",sep=";")
df.as_matrix()

no_p=9

data=[]
for i in range(no_p):
	data.append([t for t in df[df.columns[i]].values])
