import pandas as pd 
import numpy as np 

class NeuralNet():
    def __init__(self):
        self.weights = []
        self.nodes = []

    def printall(self):
        '''test function to test import '''
        print("NN class")

    def InitializeWeights(self,nodes):
        ''' Initailises the theta matrix with random valuse'''
        self.weights = []
        self.nodes = nodes
        layers = len(nodes)
        for i in range(1,layers):
            w = np.array([[np.random.uniform(-1,1) for k in range(nodes[i-1]+1)] for j in range(nodes[i])])
            print('Theta1 {} is {}'.format(i,w.shape))
            self.weights.append(w)
        return self.weights