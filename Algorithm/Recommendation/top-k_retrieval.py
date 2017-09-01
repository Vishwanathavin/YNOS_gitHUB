import pandas as pd
from parameterGeneration import getcityCoord
from getParams import generateTrainingData
import os
from sklearn.neighbors import NearestNeighbors

def getInputParams(columns):
    testData = pd.read_csv('./data/inputFile.csv')
    testData = getcityCoord(testData)
    testData["FounderAvgAge"] = 0.354838709677
    testData["CollegeAvg"] = 0.0
    testData.startupClassification = 'Classification_' + testData.startupClassification.astype(str)

    onehotCols = [c for c in columns if c[:14] == 'Classification']
    testData[testData.startupClassification.iloc[0]] = 1
    missing_cols = set(onehotCols) - set(testData.startupClassification)
    for c in missing_cols:
        testData[c] = 0
    testData.to_csv('./output/testdata.csv',index=False)
    return testData
def topK_retrieval():
    if (os.path.exists('./output/startupData.csv')):
        trainingData=pd.read_csv('./output/startupData.csv')
    else:
        trainingData= generateTrainingData()

    testData = getInputParams(trainingData.columns)

    trainingData = trainingData.drop(['City', 'founders', 'startupClassification'], 1)
    testData = testData.drop(['City', 'founders', 'startupClassification', 'InvestorName'], 1)

    trainingData = trainingData[sorted(trainingData.columns.tolist())]
    testData = testData[sorted(testData.columns.tolist())]

    trainingData=trainingData.dropna()
    neigh_list = NearestNeighbors(n_neighbors=3)
    neigh_list.fit(trainingData.drop(['startupName', 'InvestorName'], 1))
    output = neigh_list.kneighbors(testData.drop(['startupName'], 1), return_distance=True)

    print trainingData.iloc[output[1][0]]["startupName"], trainingData.iloc[output[1][0]]["InvestorName"]
    topKcompanies = pd.DataFrame(trainingData.iloc[output[1][0]]["InvestorName"])
    print topKcompanies



if __name__ =='__main__':
    topK_retrieval()