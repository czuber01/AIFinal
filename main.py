# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 10:57:55 2018

@author: Charlotte
"""

FACE_HEIGHT=70
FACE_WIDTH=60
DIGIT_HEIGHT=28
DIGIT_WIDTH=28

import readfile
import features
import train
import numpy as np
import test
import matplotlib.pyplot as plt
import math

def wholeShebang(faceordigit,featuretype,trainingpercent,smoothfactor):
    if faceordigit=='face':
        print 'training on face\n'
        trainfile='facedata/facedatatrain'
        trainlabel='facedata/facedatatrainlabels'
        testfile='facedata/facedatatest'
        testlabel='facedata/facedatatestlabels'
        height=FACE_HEIGHT
        width=FACE_WIDTH
        testN=150
        trainN=451
        isDigit=False
    else:
        print 'training on mnist\n'
        trainfile='digitdata/trainingimages'
        trainlabel='digitdata/traininglabels'
        testfile='digitdata/testimages.txt'
        testlabel='digitdata/testlabels'
        height=DIGIT_HEIGHT
        width=DIGIT_WIDTH
        testN=1000
        trainN=5000
        isDigit=True
    trainN=int(math.floor(trainN*trainingpercent))
    fullrowsarray= readfile.loadImageFile(trainfile)
    intarray=readfile.filetoarray(fullrowsarray,height,trainN)
    labelarray=readfile.loadLabelFile(trainlabel,trainN)
    fullrowsarray=readfile.loadImageFile(testfile)
    testintarray=readfile.filetoarray(fullrowsarray,height,testN)
    testlabelarray=readfile.loadLabelFile(testlabel,testN)
    if (featuretype=='combinerow'):
        feature=features.combineRow(intarray)
        testfeatures=features.combineRow(testintarray)
    elif (featuretype=='pixel'):
        feature=features.pixelbypixel(intarray)
        testfeatures=features.pixelbypixel(testintarray)
    else:
        feature=features.basicFeatures(intarray)
        testfeatures=features.basicFeatures(testintarray)
    
    outcomeprob,probmat=train.NBClassifier(labelarray,feature,smoothfactor)
    labelset=train.labelSet(labelarray)
    testedmat=test.predict(labelset, outcomeprob,probmat,testfeatures) 
    NBerror=test.error(testedmat,testlabelarray)
    print NBerror
    
    # ###outputs a 1 weight vector if training for Face, and an array of 10 weight vectors for digit training
    
    weightVector,count = train.perceptronClassifier(labelarray,feature,isDigit)
    # ###outputs an array of the result of using the training vectors on test data
    if (isDigit):
        testedResults = test.predictPerceptronDigit(weightVector,testfeatures)
    else:
        testedResults=test.predictPerceptronFace(weightVector,testfeatures)
    # ###error from the test
    perceptronError = test.error(testedResults, testlabelarray)
    # print(testedResults)
    # print(perceptronError)
    
    return NBerror,perceptronError,count

percerror=np.zeros((10,1))
nberror=np.zeros((10,1))
convergtime=np.zeros((10,1))
percent=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
for i in range(10):
    nberror[i],percerror[i],convergtime[i]=wholeShebang('digit','pixel',percent[i],0)
    
plt.plot(percent,nberror)
plt.plot(percent,percerror)
plt.plot(percent,convergtime)
#test