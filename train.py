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

def ProbabilityMatrix(features, outcomenumber, indiceslist,labelset,smoothingfactor):
    combinedfeaturesmatrices=[]
    probabilitymatrices=[]
    for i in labelset:
        #combined feeatures matrix takes the entire matrix of all feature vectors and partitions
        #based on outcome. so one matrix will have all of the feature vectors from one outcome
        #this single combined features matrix can then be summed by row, and divided by the total
        #number of columns in order to get the probability of that single feature for the given outcome
        combinedfeaturesmatrix=np.zeros((outcomenumber[i],len(features[0])),dtype=float)
        for k in range(outcomenumber[i]):
            combinedfeaturesmatrix[k]=features[indiceslist[i][k]]
        combinedfeaturesmatrices.append(combinedfeaturesmatrix)

        probabilityvector=np.sum(combinedfeaturesmatrices[i],axis=0)    
        probabilityvector=np.divide(probabilityvector, outcomenumber[i])
        '''
        if i == 1 or i==2:
            print combinedfeaturesmatrix
            print probabilityvector
        '''
        probabilitymatrices.append(probabilityvector)
    return probabilitymatrices

def NBClassifier(labelarray,feature,smoothfactor):
    indiceslist=outcomeIndexMatrix(labelarray)
    outcomenumbers=outcomeTotals(indiceslist)
    #probability for each pssible outcome, this is an array of prior probs
    proboutcome=np.divide(outcomenumbers,float(len(labelarray)))
  
    #feature= features.basicFeatures(intarray)
    labelset=labelSet(labelarray)
    smoothingfactor=smoothfactor
    probabilitymatrix=ProbabilityMatrix(feature,outcomenumbers,indiceslist,labelset,smoothingfactor)
    return proboutcome,probabilitymatrix

#def perceptronClassifier(labelarray,intarray):
    