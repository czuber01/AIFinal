# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 10:57:55 2018

@author: Charlotte
"""

print 'haha hey\n'

FACE_HEIGHT=70
FACE_WIDTH=60
DIGIT_HEIGHT=28
DIGIT_WIDTH=28

import readfile
import features
import train
import numpy as np
import test

filename1='digitdata/trainingimages'
filename2='digitdata/traininglabels'
filename3='digitdata/testimages.txt'
filename4='digitdata/testlabels'
testn=1000
trainingn=5000
trainsubset=100
height=DIGIT_HEIGHT
fullrowsarray= readfile.loadImageFile(filename1)
intarray=readfile.filetoarray(fullrowsarray,height,trainingn)
labelarray=readfile.loadLabelFile(filename2,trainingn)
fullrowsarray=readfile.loadImageFile(filename3)
testintarray=readfile.filetoarray(fullrowsarray,height,testn)
testlabelarray=readfile.loadLabelFile(filename4,testn)

#smoothingfactor currently set to zero and not written into prob mat function yet
feature=features.basicFeatures(intarray)
outcomeprob,probmat=train.NBClassifier(labelarray,feature)


labelset=train.labelSet(labelarray)
testfeatures=features.basicFeatures(testintarray)
testedmat=test.predict(labelset, outcomeprob,probmat,testfeatures) 
#print testedmat
print test.error(testedmat,testlabelarray)

def wholeShebang(faceordigit,featuretype,trainingpercent,smoothfactor):
    if faceordigit=='face':
        trainfile='facedata/facedatatrain'
        trainlabel='facedata/facedatatrainlabels'
        testfile='facedata/facedatatest'
        testlabel='facedata/facedatatestlabels'
        height=FACE_HEIGHT
        width=FACE_WIDTH
        testN=150
        trainN=451
    else:
        trainfile='digitdata/trainingimages'
        trainlabel='digitdata/traininglabels'
        testfile='digitdata/testimages.txt'
        testlabel='digitdata/testlabels'
        height=DIGIT_HEIGHT
        width=DIGIT_WIDTH
        testN=1000
        trainN=5000
    trainN=trainN*trainingpercent
    fullrowsarray= readfile.loadImageFile(trainfile)
    intarray=readfile.filetoarray(fullrowsarray,height,trainN)
    labelarray=readfile.loadLabelFile(trainlabel,trainN)
    fullrowsarray=readfile.loadImageFile(testfile)
    testintarray=readfile.filetoarray(fullrowsarray,height,testN)
    testlabelarray=readfile.loadLabelFile(testlabel,testN)
    if (featuretype=='combinerow'):
        feature=features.combineRow(intarray)
        testfeatures=features.combineRow(testintarray)
    else:
        feature=features.basicFeatures(intarray)
        testfeatures=features.basicFeatures(testintarray)

    outcomeprob,probmat=train.NBClassifier(labelarray,feature,smoothfactor)
    labelset=train.labelSet(labelarray)
    testedmat=test.predict(labelset, outcomeprob,probmat,testfeatures) 
    print test.error(testedmat,testlabelarray)


#test