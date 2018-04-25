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

def error(predictedoutcomes,testlabelarray):
    counter=0
    for i in range(len(predictedoutcomes)):
        if predictedoutcomes[i]==testlabelarray[i]:
            counter+=1
    return float(counter)/float(len(predictedoutcomes))