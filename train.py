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
  
### method intializes 10 weight vectors,1 for each digit, with an initial weight of 5
### returns an array that contains all 10 weight vectors
### length of each weight vector is the number of features+1, extra is for weight w0
def createDigitWeightVector(numFeatures):
    allWeightVector = np.full((1,numFeatures),.5,dtype=float)
    allWeightVector[0]=1
    for j in range(9):
        weightVector = np.full((1,numFeatures),.5,dtype=float)
        weightVector[0]=1
        '''
        for i in range(numFeatures+1):
            ###extra weight, w0, starts at 1
            if i == 0:
                weightVector.append(1)
            else:
                weightVector.append(5) #initial weights are all 5
        '''
        
        allWeightVector=np.append(allWeightVector,weightVector,axis=0)
    return allWeightVector

### method initializes and returns single weight vector for face or not face
### initial weights are 5
### length of each weight vector is the number of features+1
def createFaceWeightVector(numFeatures):
    weightVector=np.full((numFeatures,),.5,dtype=float)
    weightVector[0]=1
    return weightVector
    '''   
    weightVector=[]         
    for i in range(numFeatures+1):
        if i == 0:
            weightVector.append(1)
        else:
            weightVector.append(5)
    '''

### method used to train if our images or digits
def trainingDigit(labelarray,featureArray):
    ###create the 10 weight vectos
    weightVector = createDigitWeightVector(len(featureArray[0]))
    ###used to check how many times a vector has to be corrected
    correctness = 101
    counter=0
        ###reset correctness for each loop through all the images
        ###go through each image's feature vector
    while correctness>100:
        counter+=1
        correctness=0
        for i in range(len(featureArray)):
            label=labelarray[i]
            labelvec=np.zeros((10,1),dtype=int)
            labelvec[label]=1
            for j in range(10):
                dotprod=np.dot(featureArray[i], weightVector[j])
                if dotprod>=0:
                    if label != j:
                        correctness+=1
                        weightVector[j]=np.subtract(weightVector[j],featureArray[i])
                else:
                    if label == j:
                        correctness+=1
                        weightVector[j]=np.add(weightVector[j],featureArray[i])
#        if counter>1000:
 #           return weightVector
    return weightVector,counter
        
### method used used for training if our image is a face
def trainingFace(labelarray,featureArray):
    ### only one weight vector is needed for face
    weightVector = createFaceWeightVector(len(featureArray[0]))
    
    correctness = 0
    counter=0
    while True:
        correctness = 0
        for i in range(len(featureArray)):
            ### multiply the feature vector and weight vector
            dotProduct = np.dot(featureArray[i], weightVector)
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
        counter+=1
        if counter> 10000:
            print 'early end'
            return weightVector,counter
        if correctness == 0:
            ### return corrected weight vector
            return weightVector,counter



def perceptronClassifier(labelarray,featureArray,isDigit):
    #featureArray = features.basicFeatures(intarray)
    weightVector = []
    ###we must insert a 1 before every feature vector for dot product with weight vector
    onesvec=np.ones((len(featureArray),1))
    featureArray=np.append(onesvec,featureArray,1)
    
    #for featureVector in featureArray:
     #   featureVector.insert(0,1)

    if(isDigit == True): #digit
        weightVector,count = trainingDigit(labelarray,featureArray)

    else: #face
        weightVector,count = trainingFace(labelarray,featureArray)

    ### returns corrected weight vector
    return weightVector,count
