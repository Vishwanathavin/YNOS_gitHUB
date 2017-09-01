import sys
sys.path.insert(0, "../../dataGeneration")
from consolidation import dataConsolidate
from parameterGeneration import getAge,getTier,getcityCoord
import os
import pandas as pd
import numpy as np

def getPersonParams(personData):
    personData=getAge(personData)
    personData=getTier(personData)
    return personData

def getStartupParams(startupData,personData):

    startupData = getcityCoord(startupData)

    startupData["founderAgeAvg"] = ""
    startupData["collegeTierAvg"] = ""

    # Get the average of the columns
    for index, row in startupData.iterrows():
        row["founders"] = row["founders"].replace('\'', '').replace('[', '').replace(']', '')
        row["founders"] = row["founders"].split(',')
        agesum = []

        for foundername in range(len(row['founders'])):
            row.founders[foundername] = row.founders[foundername].strip()
            agesum = np.append(agesum, personData[personData.name == row.founders[foundername]]["Age"].values)

        ageAvg = agesum.mean()
        startupData.loc[index, 'founderAgeAvg'] = ageAvg

        tiersum = []
        for foundername in range(len(row['founders'])):
            row.founders[foundername] = row.founders[foundername].strip()
            tiersum = np.append(tiersum, personData[personData.name == row.founders[foundername]]["Tier"].values)


        tierAvg = tiersum.mean()

        startupData.loc[index, "collegeTierAvg"] = tierAvg

    return startupData

def generateTrainingData():



    if (os.path.exists('../../dataGeneration/output/personData.csv') and os.path.exists('../../dataGeneration/output/startupData.csv')):
        personData=pd.read_csv('../../dataGeneration/output/personData.csv')
        startupData=pd.read_csv('../../dataGeneration/output/startupData.csv')
    else:
        startupData,personData=dataConsolidate()

    startupData = startupData[['startupName'] + ['startupClassification'] + ['founders'] + ['InvestorName'] + ['City']]
    personData=getPersonParams(personData)
    startupData=getStartupParams(startupData,personData)

    # Do onehot encoding
    oneHot = pd.get_dummies(startupData['startupClassification'], prefix='Classification')
    startupData = pd.concat([startupData, oneHot], axis=1)
    startupData.to_csv('./output/startupData.csv', index=False)
    return startupData


if __name__ =='__main__':
    startupData=generateTrainingData()