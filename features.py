# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:29:55 2018

@author: Charlotte
"""
#you need an improved dict class in order to count the total number of 
# vectors that have a certain value in the vector, this makes it easier to search
# by a specific value and count

import numpy as np

#make every feature vector a binary vector for easier training and comparison
#if you are looking at values, such as 5 pixels in a given area, create a floor function and
#just set up the part of the vector as:less than 10 pixels in this square, less than 20, etc
'''
class supportedVector:
    
    def __init__():
        
        
    def __totalSum__():
        
    def __normalize__():
'''        
    
def basicFeatures(dataarray):
    featurearray=[]
    numpixels=len(dataarray[0])*(len(dataarray[0][0]))
    for i in range(len(dataarray)):
        #for each single matrix
        singlematrix=dataarray[i]
        #784 pixels in digit image
        features=np.zeros((numpixels,), dtype=int)
        for j in range(len(singlematrix)):
            counter=0
            for k in range(len(singlematrix[0])):
                if singlematrix[j][k]==1:
                    counter+=1
     
            features[28*j+counter]=1
        featurearray.append(features)
       
    return featurearray


def mostBasicFeatures(dataarray):
    featurearray=[]
    numpixels=len(dataarray[0])*len(dataarray[0][0])
    for i in range(len(dataarray)):
        singlematrix=dataarray[i]
        features=np.zeros((numpixels,),dtype=int)
        counter=0
        for j in range(len(singlematrix)):
            for k in range(len(singlematrix[0])):
                if (singlematrix[j][k]==1):
                    counter+=1
        features[counter]=1
        featurearray.append(features)                     
    return featurearray
        
'''        
def featureDigit(dataconvert,featuretype):


def featureFace(dataconvert,featuretype):
'''

        