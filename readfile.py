# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:55:56 2018

@author: Charlotte
"""

#face files are 70x60
#mnist files are 28x28
 #matrices are stored as lists of lists
 


'''
class singleVec:

    def __init__(self,data,height,width):
        self.dataconvert=convertInt(data)
        self.height=height
        self.width=width
        
    def __getalldata__(self):
        return self.dataconvert
    def __getdata__(self,i,j):
        return self.dataconvert[i][j]
    def __setLabel__(self,label):
        self.label=label
 '''   
    
    #change from ascii to 0/1's here?
'''def convertInt(data):
    if type(data)!=type([]):
        return convertInteger(data)
    else:
        return map(convertInt,data)
'''

def convertInteger(data):
    if(data == ' '):
        return 0
    elif(data =='#'):
        return 1
    else:
        return 2
        

def loadImageFile(filename):
    fullrowsarray=[]
    with open(filename) as f:
        fullrowsarray = f.readlines()
        #print fullrowsarray
    return fullrowsarray


    
def loadLabelFile(filename,n):
    labelarray=[]
    with open(filename) as f:
        labelarray=f.readlines()
    for i in range(len(labelarray)):
        labelarray[i]=int(labelarray[i][0])
    labelarray=labelarray[:n]
    return labelarray
        #right now you have a list of lists? each with one element
        #return an array of integers as labels

def filetoarray(fullrowsarray,height,n):
    allimages=[]
    for j in range(n):
        singleimage=[]
        for i in range(height):
            rowtointlist=[]
            fullrowsarray[j*height+i]=fullrowsarray[j*height+i][:-1]
            for k in fullrowsarray[j*height+i]:
                rowtointlist.append(convertInteger(k))
            singleimage.append(rowtointlist)
        allimages.append(singleimage) 
    return allimages
        

#finish by returnnig list of vector objects
        