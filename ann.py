from random import seed
from random import random
import numpy as np
import os
import math
import scipy.stats
from numpy import mean, sqrt, square, arange
data = open("inputf.txt", "r")
m=np.genfromtxt(data,usecols=(0,1,2,3,4,5,6,7,8,9),delimiter=" ")
numm=m.shape[0]/4
data = open("input_testf.txt", "r")
m1=np.genfromtxt(data,usecols=(0,1,2,3,4,5,6,7,8,9),delimiter=" ")
numm1=m1.shape[0]/4
for x in range (numm*4):
	m[x][9]=int(m[x][9])
for x in range (numm1*4):
	m1[x][9]=int(m1[x][9])
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network

#seed(1)
#network = initialize_network(9, 1, 3)
#for layer in network:
#	print(layer)
# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	#print("weight "),
	#print(weights[-1])
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation
# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + math.exp(-activation))
# Forward propagate input to a network output
def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			#print('output'),
			#print('weights')
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs
# Calculate the derivative of an neuron output
def transfer_derivative(output):
	return output * (1.0 - output)
# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])
# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:9]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']
# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[int(row[9])] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		#print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
# Make a prediction with a network
def predict(network, row):
	outputs = forward_propagate(network, row)
	return outputs.index(max(outputs))
a=np.array(m)
for i in range(0,9):
	maxi=a[:,i].max()
	mini=a[:,i].min()
	for j in range(0,4*numm):
		#print(a[j][i]),
		#print(maxi),
		#print(mini)
		m[j][i]=(a[j][i]-mini)*1.0/(maxi-mini)
#print(m)
a=np.array(m1)
for i in range(0,9):
	maxi=a[:,i].max()
	mini=a[:,i].min()
	for j in range(0,4*numm1):
		#print(a[j][i]),
		#print(maxi),
		#print(mini)
		m1[j][i]=(a[j][i]-mini)*1.0/(maxi-mini)
n_inputs = len(m[0]) - 1
n_outputs = len(set([row[9] for row in m]))
network = initialize_network(n_inputs, 25, n_outputs)
train_network(network, m, 1 , 10, n_outputs)
#for layer in network:
#	print(layer)
c=0
for row in m1:
	prediction = predict(network, row)
	print('Expected=%d, Got=%d' % (row[9], prediction))
	if row[9]==prediction :
		c+=1
print(c)
print("Accuracy: "),
print(c*100.0/(numm1*4.0))
