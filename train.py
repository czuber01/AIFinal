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


### method intializes 10 weight vectors,1 for each digit, with an initial weight of 5
### returns an array that contains all 10 weight vectors
### length of each weight vector is the number of features+1, extra is for weight w0
def createDigitWeightVector(numFeatures):
    allWeightVector = []
    for j in range(10):
        weightVector = []
        for i in range(numFeatures+1):
            ###extra weight, w0, starts at 1
            if i == 0:
                weightVector.append(1)
            else:
                weightVector.append(5) #initial weights are all 5
        allWeightVector.append(weightVector)
    return allweightVector

### method initializes and returns single weight vector for face or not face
### initial weights are 5
### length of each weight vector is the number of features+1
def createFaceWeightVector(numFeatures):
    weightVector = []
    for i in range(numFeatures+1):
        if i == 0:
            weightVector.append(1)
        else:
            weightVector.append(5)

### method used to train if our images or digits
def trainingDigit(labelarray,featureArray):
    ###create the 10 weight vectos
    weightVector = createDigitWeightVector(len(featureArray[0]))
    ###used to check how many times a vector has to be corrected
    correctness = 0
    while True:
        ###reset correctness for each loop through all the images
        correctness = 0
        ###go through each image's feature vector
        for i in range(len(featureArray)):
            ###go thor
            for j in range(10):
                ###multiplies the feature vector by the weightvector for each digit
                dotProduct = np.dot(featureArray[i], weightVector[j])
                ###correct label (0,1,2,...,etc)
                label = labelarray[i]
                ###if dotProduct is >= 0 then the weight vector is predicting that the image is the digit corresponding to
                ###that specific weight vector
                if dotProduct >= 0:
                    ###if the digit corresponding to the weight vector does not match the label of the image
                    if not label == j:
                        ###since the current weight vector gave a false positive, subtract the feature vector from the weight vector
                        weightVector[j] = np.subtract(weightVector[j],featureArray[i])
                        ### a weight vector was changed
                        correctness = correctness + 1

                ### weight vector predicted that image does not correspoing to its digit
                else:
                    ### if label of image actually corresponds to the digit the weight vector represents
                    if label == j:
                        ### false negative, so we add the feature vector the weight vector
                        weightVector[j] = np.add(weightVector[j],featureArray[i])
                        ### a weight vector was changed
                        correctness = correctness + 1
        ### weight vectors stop changing, break and return the array of weight vectors
        if correctness == 0:
            return weightVector

### method used used for training if our image is a face
def trainingFace(labelarray,featureArray):
    ### only one weight vector is needed for face
    weightVector = createFaceWeightVector(len(featureArray[0]))
    correctness = 0
    while True:
        correctness = 0
        for i in range(len(featureArray)):
            ### multiply the feature vector and weight vector
            dotProduct = np.dot(featureArray[i], weightVector[j])
            ### 1 for face, 0 for not face
            label = labelarray[i]
            ### weight vector predicted face
            if dotProduct >= 0:
                ### false positive
                if label == 0:
                    weightVector = np.subtract(weightVector,featureArray[i])
                    correctness = correctness + 1
            ### weight vector predicted not face
            else:
                ### false negative
                if label == 1:
                    weightVector = np.add(weightVector,featureArray[i])
                    correctness = correctness + 1
        if correctness == 0:
            ### return corrected weight vector
            return weightVector



def perceptronClassifier(labelarray,intarray,isDigit):
    featureArray = features.mostBasicFeatures(intarray)
    weightVector = []
    ###we must insert a 1 before every feature vector for dot product with weight vector
    for featureVector in featureArray:
        featureVector.insert(0,1)

    if(isDigit == True): #digit
        weightVector = trainingDigit(labelarray,featureArray)

    else: #face
        weightVector = trainingFace(labelarray,featureArray)

    ### returns corrected weight vector
    return weightVector










