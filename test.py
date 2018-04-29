# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:21:56 2018

@author: Charlotte
"""

#testes

import numpy as np
import features


def predict(trainlabelset,outcomeprob,probmat,testintarray):
    testfeatures=features.basicFeatures(testintarray)
   # print testfeatures
    predictedoutcomes=[]
    for i in range(len(testfeatures)):
        #for each single test image, get a prediction and return a number
        #here we are getting a value for each possible outcome
        outcomeprobvector=[]
        testvec=testfeatures[i]
        for k in range(len(probmat)):
            probvec=probmat[k]
            singleprobvector=np.zeros((len(testvec),),dtype=float)
            for j in range(len(testvec)):
                singleprobvector[j]=testvec[j]*probvec[j]
            singleprobvector[ singleprobvector == 0] = 1
            probprod=np.prod(singleprobvector)
            
            probprod=outcomeprob[k]*probprod
            outcomeprobvector.append(probprod)
        print outcomeprobvector
        predictedoutcomes.append(np.argmax(outcomeprobvector))
    return predictedoutcomes

### prediction for our test images that are digits
### weightVector is the list of 10 weight vectors
### testintarray is the images we are testing
def predictPerceptronDigit(weightVector, testintarray):
    ### creates features from test images
    testfeatures = features.basicFeatures(testintarray)
    ### what perceptron will predict
    predictedoutcomes = []
    ### go through every image
    for i in range(len(testfeatures)):
        ### guess for each of the weight vectors, if >= 0, yes, else no
        dotProducts = []
        ### check with each of the weight vectors
        for j in range(len(weightVector)):
            ### take the dot product of each weight vector and store it
            dotProducts.append(np.dot(testfeatures[i], weightVector[j]))
        ### actual prediction will be which weight vector (0,1,...,9) has the greatest dot product (meaning it was weighed higher)
        predictedoutcomes.append(np.argmax(dotProducts))
    ### return list of the predicted outcome for each image
    return predictedoutcomes
         
### prediction for our test images that are face
### weightVector is a single weight vector
### testintarray is the images we are testing        
def predictPerceptronFace(weightVector, testintarray):
     ### creates features from test images
    testfeatures = features.basicFeatures(testintarray)
    predictedoutcomes = []
    for i in range(len(testfeatures)):
        ### guess for each of the weight vectors, if >= 0, yes, else no
        dotProduct = np.dot(testfeatures[i], weightVector)
        if dotProduct >= 0:
            predictedoutcomes.append(1)
        else:
            predictedoutcomes.append(0)
    return predictedoutcomes


def error(predictedoutcomes,testlabelarray):
    counter=0
    for i in range(len(predictedoutcomes)):
        if predictedoutcomes[i]==testlabelarray[i]:
            counter+=1
    return float(counter)/float(len(predictedoutcomes))