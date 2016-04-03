import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Health.csv")
df.as_matrix()

death_per1000=[float(t) for t in df[df.columns[0]].values]
o=[1 for x in range(len(death_per1000))]
doc=[float(t) for t in df[df.columns[1]].values]
hosp=[float(t) for t in df[df.columns[2]].values]
inc=[float(t) for t in df[df.columns[3]].values]
pop=[float(t) for t in df[df.columns[4]].values]

inputs=[o,doc,hosp,inc,pop]

# Widrow-Hoff Method
def lin_widrow_hoff(inputs,targets):
	weights=[1,1]
	al=.000005
	error=[]
	h_weights=0
	for n in range(len(inputs)):
		h_weights=weights[0]+weights[1]*inputs[n]
		error.append(targets[n]-h_weights)
		weights[0]+=al*error[n]
		weights[1]+=al*error[n]*inputs[n]
	print(weights)
	x_axis=[x for x in range(int(min(inputs)),int(max(inputs))+1)]
	h=[(weights[0]+weights[1]*x) for x in x_axis]
	print(x_axis[:5],h[:5])
	plt.plot(x_axis,h)
	plt.scatter(inputs,targets)

lin_widrow_hoff(doc,death_per1000)
#lin_widrow_hoff(hosp,death_per1000)
#lin_widrow_hoff(inc,death_per1000)
#lin_widrow_hoff(pop,death_per1000)

def multi_widrow_hoff(targets,inputs):
	weights=[[1 for x in range(len(inputs))] for y in range(len(targets)+1)]
	al=0.00000005
	error=[]
	for n in range(len(targets)):
		h_weights=0
		for k in range(len(inputs)):
			h_weights+=inputs[k][n]*weights[n][k]
		error.append(targets[n]-h_weights)
		#print(targets[n],weights[n],h_weights,error[n])
		for k in range(len(inputs)):
			weights[n+1][k]=weights[n][k]+al*error[n]*inputs[k][n]
	print(weights[len(weights)-1])
	h_weights1=[]
	for n in range(len(targets)):
		h_weights=0
		for k in range(len(inputs)):
			h_weights+=inputs[k][n]*weights[len(weights)-1][k]
		h_weights1.append(h_weights)
	plt.scatter(targets,h_weights1,color='red')
	#plt.scatter(targets,error)


multi_widrow_hoff(death_per1000,inputs)

plt.show()
