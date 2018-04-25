# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 23:18:37 2018

@author: Charlotte
"""

#for training:
#count total for each true result, ie how many ones, twos, etc
# for each result, add the feature vector together and divide by the total count to get a probability vector
# for each outcome
#when predicting an outcome, multiply test feature vector by each probability vector. multiply inverve by inverse
#during training, have object for each outcome and append vector while reading and add counter
import features
import numpy as np
 
def labelSet(labelarray):
    return set(labelarray)

def outcomeIndexMatrix(labelarray):
    labelset=labelSet(labelarray)
    indiceslist=[]
    for i in labelset:
        indices=[j for j, x in enumerate(labelarray) if x==i]
        indiceslist.append(indices)
    return indiceslist

def outcomeTotals(indiceslist):
    outcomenumber=np.zeros((len(indiceslist),),dtype=int)
    for i in range(len(indiceslist)):
        outcomenumber[i]=len(indiceslist[i])
    return outcomenumber

def ProbabilityMatrix(features, outcomenumber, indiceslist,labelset):
    combinedfeaturesmatrices=[]
    probabilitymatrices=[]
    for i in labelset:
        combinedfeaturesmatrix=np.zeros((outcomenumber[i],len(features[0])),dtype=float)
        #print outcomenumber[i]
        #print indiceslist[i]
        for k in range(outcomenumber[i]):
            combinedfeaturesmatrix[k]=features[indiceslist[i][k]]
        combinedfeaturesmatrices.append(combinedfeaturesmatrix)
        probabilityvector=np.sum(combinedfeaturesmatrices[i],axis=0)    
        probabilityvector=np.divide(probabilityvector, outcomenumber[i])
        probabilitymatrices.append(probabilityvector)
    return probabilitymatrices

def NBClassifier(labelarray,intarray):
    indiceslist=outcomeIndexMatrix(labelarray)
    outcomenumbers=outcomeTotals(indiceslist)
    proboutcome=np.divide(outcomenumbers,float(len(labelarray)))
    print proboutcome
    feature= features.mostBasicFeatures(intarray)
    labelset=labelSet(labelarray)
    probabilitymatrix=ProbabilityMatrix(feature,outcomenumbers,indiceslist,labelset)
    return proboutcome,probabilitymatrix

#def perceptronClassifier(labelarray,intarray):
    