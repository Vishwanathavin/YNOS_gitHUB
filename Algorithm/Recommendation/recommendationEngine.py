import os
from inspect import getsourcefile

import pandas as pd
from sklearn.neighbors import NearestNeighbors

from getParams import generateTrainingData,getInputParams




def topKcompanies(trainingData,testData):
    neigh_list = NearestNeighbors(n_neighbors=10)
    neigh_list.fit(trainingData.drop(['startupName', 'InvestorName'], 1))
    output = neigh_list.kneighbors(testData.drop(['startupName'], 1), return_distance=True)
    # print trainingData.iloc[output[1][0]]["startupName"], trainingData.iloc[output[1][0]]["InvestorName"]

    # print topKcompanies

    return output

def topKinvestors(topinvestors):
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    personData = pd.read_csv(path+'/../../dataGeneration/output/personData.csv')

    InvList = []
    for index,row in topinvestors.iterrows():
        row["InvestorName"] = row["InvestorName"].replace('u\'','').replace('\'','').replace('[','').replace(']','')
        row["InvestorName"] = row["InvestorName"].split(',')
        for investorindex in range(len(row['InvestorName'])):
            InvList.append(row['InvestorName'][investorindex])


    testData = personData[personData['name'].isin(InvList)]

    neigh_list = NearestNeighbors(n_neighbors=10)
    neigh_list.fit(personData.drop(['F_or_I', 'file_id','name'], 1).dropna())
    output = neigh_list.kneighbors(testData.drop(['F_or_I', 'file_id','name'], 1), return_distance=True)
    return output

    # _=[[InvList.append(x) for x in rows.InvestorName] for index,rows in topinvestors.iterrows() ]
    # print InvList






    #     row["InvestorName"] = row["InvestorName"].replace('u\'','').replace('\'','').replace('[','').replace(']','')
    #     row["InvestorName"] = row["InvestorName"].split(',')
    #     for investorindex in range(len(row['InvestorName'])):
    #         row.InvestorName[investorindex] = row.InvestorName[investorindex].strip()
    #         investorName =  row['InvestorName'][investorindex]
    #
    #         age = ageFile[ageFile.Name== investorName]["Age"].values
    #
    #         tier=collegeFile[collegeFile.Name == investorName]["Tier"].values
    #
    #         if(len(age)!=0 and len(tier)!=0):
    #             investorSeries = pd.Series([investorName,age[0],tier[0]],index=['Name','Age','Tier'])
    #             investorList.append(investorSeries)
    # testData = pd.DataFrame(investorList)
    #
    # neigh_list = NearestNeighbors(n_neighbors=3)
    # neigh_list.fit(trainingData.drop(['Name'], 1))
    # output = neigh_list.kneighbors(testData.drop(['Name'], 1), return_distance=True)

    # print'Input investor Names: ', testData.Name.values,testData.Age.values,testData.Tier.values

    # matchingInvestorList = []
    # # print 'Output Investor Names: '
    # for i in range(len(output[1])):
    #     for j in range(len(output[1][i])):
    #         # print output[1][i][j],trainingData.iloc[output[1][i][j]]["Name"],trainingData.iloc[output[1][i][j]]["Age"],trainingData.iloc[output[1][i][j]]["Tier"]
    #         matchingInvestorList.append(trainingData.iloc[output[1][i][j]]["Name"])
    #

def recommendationEngine():
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    if (os.path.exists(path+'/output/startupData.csv')):
        trainingData=pd.read_csv(path+'/output/startupData.csv')
    else:
        trainingData= generateTrainingData()

    testData = getInputParams(trainingData.columns)

    trainingData = trainingData.drop(['City', 'founders', 'startupClassification','dealDate','Round_Investment_Amount_INR','InvestorID'], 1)
    testData = testData.drop(['City', 'founders', 'startupClassification', 'InvestorName'], 1)

    trainingData = trainingData[sorted(trainingData.columns.tolist())]
    testData = testData[sorted(testData.columns.tolist())]

    trainingData=trainingData.dropna()

    output= topKcompanies(trainingData,testData)

    topinvestors = pd.DataFrame(trainingData.iloc[output[1][0]]["InvestorName"])

    output = topKinvestors(topinvestors)

    personData = pd.read_csv(path+'/../../dataGeneration/output/personData.csv')
    topinvestors = pd.DataFrame(personData.iloc[output[1][0]]["name"])

    print topinvestors



if __name__ =='__main__':
    recommendationEngine()