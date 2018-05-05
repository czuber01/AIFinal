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
def pixelbypixel(dataarray):
    
    numrows=len(dataarray[0])
    numcols=len(dataarray[0][0])
    numpixels=numrows*numcols
    features=np.zeros((len(dataarray),numrows*numcols),dtype=int)
    for i in range(len(dataarray)):
        for j in range(numrows):
            for k in range(numcols):
                if dataarray[i][j][k]!=0:
                    features[i][numcols*j+k]=1
    return features

def basicFeatures(dataarray):
    featurearray=[]
    numrows=len(dataarray[0])
    numcols=len(dataarray[0][0])
    numpixels=numrows*numcols
    '''
    for i in range(len(dataarray)):
        print dataarray[i]
    '''
   # print dataarray
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


def mostBasicFeatures2(dataarray):
    
    featurearray=[]
    numrows=len(dataarray[0])
    numcols=len(dataarray[0][0])
    numpixels=numrows*numcols

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
  
   

    
def combineRow(dataarray):
    featurearray=[]
    numrows=len(dataarray[0])
    numcols=len(dataarray[0][0])
    numpixels=numrows*numcols
    '''
    for i in range(len(dataarray)):
        singlemat=dataarray[i]
        print len(singlemat)
        print len(singlemat[0])'''
    for i in range(len(dataarray)):
        singlemat=dataarray[i]
        
        features=np.zeros((numrows,),dtype=int)
        for j in range(numrows/4):
            counter=0
            for m in range(4):
                for k in range(numcols):
                    #print k
                    if(singlemat[4*j+m][k] != 0):
                        counter+=1
            #if counter is less than 1/4 number of spaces
            if (counter<=numcols):
                features[4*j]=1
            elif (counter<=numcols*2):
                features[4*j +1]=1
            elif (counter<= numcols*3):
                features[4*j +2]=1
            else:
                features[4*j+3]=1
        featurearray.append(features)
    #print featurearray
    return featurearray
      
'''        
def featureDigit(dataconvert,featuretype):


def featureFace(dataconvert,featuretype):
'''

        