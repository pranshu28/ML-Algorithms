import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv("weather.csv")
df.as_matrix()

no_p=4

data=[]
for i in range(no_p):
	data.append([t for t in df[df.columns[i]].values])
y_list=[t for t in df[df.columns[4]].values]


#Naive Bayes Algorithm

def prob(x,data_x):
	num=0
	for i in x:
		if i==data_x:
			num+=1
	if num==0:
		return 1.0/(den+1)
	return 1.0*num/len(x)

def prob_c(x,data_x,y,data_y):
	den=0
	num=0
	for i in range(len(x)):
		if y[i]==data_y:
			den+=1
			if x[i]==data_x:
				num+=1
	if num==0:
		return 1.0/(den+1)
	return 1.0*num/den

def prob_list():
	probs=[]
	for i in range(len(data)):
		#print "Column :",i+1
		prob_dist=[]
		for dist_y in list(set(y_list)):
			prob_disty=[]
			for dist_x in list(set(data[i])):
				#print dist_x,dist_y 
				#print "-----------",prob(data[i],dist_x,y_list,dist_y)
				prob_disty.append(prob_c(data[i],dist_x,y_list,dist_y))
			prob_dist.append(prob_disty)
		probs.append(prob_dist)
	return probs
#print(prob_list())

def prob_rev(y,data_y,x_index):
	p=prob_list()
	prod_yes=1
	prod_no=1
	for disty1 in p[x_index][0]:
		prod_no*=disty1
	for disty2 in p[x_index][1]:
		prod_yes*=disty2
	den=prod_yes+prod_no
	if data_y=='yes ':
		num=prod_yes*prob(y,data_y)
	else:
		num=prod_no*prob(y,data_y)
	#print(num,den,prod_yes,prod_no,prob(y,data_y))
	return 1.0*num/den
	
print(prob_rev(y_list,'yes ',3))

