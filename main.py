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
height=DIGIT_HEIGHT
fullrowsarray= readfile.loadImageFile(filename1)
intarray=readfile.filetoarray(fullrowsarray,height,trainingn)
labelarray=readfile.loadLabelFile(filename2)
fullrowsarray=readfile.loadImageFile(filename3)
testintarray=readfile.filetoarray(fullrowsarray,height,testn)
testlabelarray=readfile.loadLabelFile(filename4)

outcomeprob,probmat=train.NBClassifier(labelarray,intarray)
#print outcomeprob
#print probmat
#print probmat

labelset=train.labelSet(labelarray)
testedmat=test.predict(labelset, outcomeprob,probmat,testintarray)


print testedmat
print test.error(testedmat,testlabelarray)

# ###uncomment to use perceptron
# ###outputs a 1 weight vector if training for Face, and an array of 10 weight vectors for digit training
# weightVector = train.perceptronClassifier(labelarray,intarray,True)
# ###outputs an array of the result of using the training vectors on test data
# testedResults = test.predictPerceptronDigit(weightVector,testintarray)
# ###error from the test
# perceptronError = test.error(testedResults, testlabelarray)
# print(testedResults)
# print(perceptronError)
    


#test