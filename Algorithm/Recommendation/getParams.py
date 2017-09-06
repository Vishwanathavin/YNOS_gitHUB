import sys
sys.path.insert(0, "../../dataGeneration")
from addParams import addParamsToData,getcityCoord
import os
import pandas as pd
import numpy as np
from inspect import getsourcefile

def getInputParams(columns):
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    testData = pd.read_csv(path+'/data/inputFile.csv')
    testData = getcityCoord(testData)
    testData["FounderAvgAge"] = 0.354838709677
    testData["CollegeAvg"] = 0.0
    testData.startupClassification = 'Classification_' + testData.startupClassification.astype(str)

    onehotCols = [c for c in columns if c[:14] == 'Classification']
    testData[testData.startupClassification.iloc[0]] = 1
    missing_cols = set(onehotCols) - set(testData.startupClassification)
    for c in missing_cols:
        testData[c] = 0
    testData.to_csv(path+'/output/testdata.csv',index=False)
    return testData

def generateTrainingData():
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    if (os.path.exists(path+'/../../dataGeneration/output/personData.csv') and os.path.exists(path+'/../../dataGeneration/output/startupData.csv')):
        personData=pd.read_csv(path+'/../../dataGeneration/output/personData.csv')
        startupData=pd.read_csv(path+'/../../dataGeneration/output/startupData.csv')
    else:
        startupData,personData=addParamsToData()



    # Do onehot encoding
    oneHot = pd.get_dummies(startupData['startupClassification'], prefix='Classification')
    startupData = pd.concat([startupData, oneHot], axis=1)
    startupData.to_csv(path+'/output/startupData.csv', index=False)
    return startupData


if __name__ =='__main__':
    startupData=generateTrainingData()