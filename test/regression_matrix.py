import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("GDP_and_Major_Industrial_Sectors_of_Economy_Dataset.xls")
df.as_matrix()

year=[int(t[:4]) for t in df[df.columns[0]].values][:-1]
gdp_crs=[float(t) for t in df[df.columns[1]].values][:-1]
o=[1 for x in range(len(gdp_crs))]
a=[float(t) for t in df[df.columns[2]].values][:-1]
b=[float(t) for t in df[df.columns[3]].values][:-1]
c=[float(t) for t in df[df.columns[4]].values][:-1]
d=[float(t) for t in df[df.columns[5]].values][:-1]
e=[float(t) for t in df[df.columns[6]].values][:-1]
f=[float(t) for t in df[df.columns[7]].values][:-1]

print "Least mean squared:"

#Least mean square method
inputs=[o,a,b,c,d,e,f]

#Matrix Method
def matrix(year,targets,inputs_t):
	inputs=np.array(inputs_t).T
	targets=np.array(targets).T
	weights=np.dot(np.dot(np.linalg.inv(np.dot(inputs_t,inputs)),inputs_t),targets)
	h_weights=np.dot(inputs,weights)
	error=((h_weights-targets)**2)**.5
	j_weights=.5*np.dot(np.array(error).T,error)
	print "\t Matrix Method - J(weights) =",j_weights
	plt.plot(year,error)

matrix(year,gdp_crs,inputs)

# Widrow-Hoff Method
"""def lin_widrow_hoff(targets,inputs):
	weights=[1,1]
	al=.0000000005
	error=[]
	h_weights=0
	for n in range(len(targets)):
		h_weights=weights[0]+weights[1]*inputs[n]
		error.append(targets[n]-h_weights)
		weights[0]+=al*error[n]
		weights[1]+=al*error[n]*inputs[n]
	print(weights)
	x_axis=[x for x in range(int(inputs[0]),int(inputs[len(inputs)-1]))]
	h=[(weights[0]+weights[1]*x) for x in x_axis]
	print(len(inputs),len(x_axis),len(h),inputs[:5],h[:5])
	plt.plot(x_axis,h)
	plt.scatter(inputs,targets)

lin_widrow_hoff(gdp_crs,year)"""

"""def multi_widrow_hoff(year,targets,inputs):
	weights=[[1 for x in range(len(inputs))] for y in range(len(year)+1)]
	al=0.0000000000000005
	error=[]
	for n in range(len(year)):
		h_weights=0
		for k in range(len(inputs)):
			h_weights+=inputs[k][n]*weights[n][k]
		error.append(targets[n]-h_weights)
		#print(targets[n],weights[n],h_weights,error[n])
		for k in range(len(inputs)):
			weights[n+1][k]=weights[n][k]+al*error[n]*inputs[k][n]
	print(weights[len(weights)-1])
"""

#multi_widrow_hoff(year,gdp_crs,inputs)

"""plt.scatter(year,gdp_crs)
plt.scatter(a,gdp_crs)
plt.scatter(b,gdp_crs)
plt.scatter(c,gdp_crs)
plt.scatter(d,gdp_crs)
plt.scatter(e,gdp_crs)
plt.scatter(f,gdp_crs)"""

plt.show()
