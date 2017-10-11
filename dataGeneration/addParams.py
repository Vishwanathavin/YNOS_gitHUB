import codecs
import os
from datetime import datetime
from inspect import getsourcefile

import numpy as np
import pandas as pd

from dataGeneration.mergingRoutines.consolidation import dataConsolidate


def getTier(personData):
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    eduData=pd.read_csv(path+'/metaOutput/educationData.csv')
    eduData = eduData.dropna(subset=['name','college'], how='any').reset_index(drop=True)

    # Check if the string is present
    searchFor =  ['INDIAN INSTITUTE', 'NATIONAL INSTITUTE', 'IIT', 'NIT', 'BITS', 'BIRLA INSTITUTE', 'IIM', 'ISB', 'INDIAN SCHOOL', 'HARVARD']
    commonData = eduData[eduData['college'].str.contains('|'.join(searchFor))]
    commonData['Tier'] = 1
    eduData['Tier']=commonData.Tier
    eduData['Tier']=eduData['Tier'].replace(np.nan,int(0))

    eduData = eduData.groupby(["name"]).agg(
    {'Tier': lambda x: max(x)}).reset_index()


    personData = personData.merge(eduData[['name'] + ['Tier']], how='left')

    return personData
def getPersonParams(personData):
    personData=getAge(personData)
    personData=getTier(personData)
    return personData
def getcityCoord(startupData):
    # Getting the co-ordniates from the file
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    with codecs.open(path+'/data/citi_co-ordinates.csv', "r", encoding='utf-8', errors='ignore') as coord_data_temp:
        coordData = pd.read_csv(coord_data_temp)
    # coordData = pd.read_csv(path+'/data/citi_co-ordinates.csv')
    coordData["City"] = coordData["City"].str.strip()
    coordData.drop_duplicates("City", inplace=True)

    for index, row in startupData.iterrows():
        lat = coordData[row['City'] == coordData['City']]['Lat'].astype(float).values
        lon = coordData[row['City'] == coordData['City']]['Lon'].astype(float).values
        if (lat.size & lon.size):
            startupData.loc[index, "Lat"] = lat
            startupData.loc[index, "Lon"] = lon
        else:
            startupData.loc[index, "Lat"] = np.nan
            startupData.loc[index, "Lon"] = np.nan
    return startupData


def getAge(personData):
    today = datetime.today()
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    eduData=pd.read_csv(path+'/metaOutput/educationData.csv')
    eduData = eduData.dropna(subset=['name','duration','degree'], how='any').reset_index(drop=True)

    # Check if the string is present
    searchFor = ['12', 'SECONDARY', 'SCHOOL']
    eduData=eduData[~eduData['degree'].str.contains('|'.join(searchFor))].reset_index(drop=True)

    eduData['duration'] = eduData['duration'].apply(lambda x: x.strip())
    eduData['duration'] = eduData['duration'].apply(lambda x: x.split('-')[0])
    eduData['duration'] = eduData['duration'].apply(lambda x: x.split(' ')[0])

    eduData = eduData.groupby(["name"]).agg(
    {'duration': lambda x: (min(x))}).reset_index()
    eduData['Age']=today.year - eduData['duration'].astype(int) + 17

     # personData=personData.drop_duplicates('name').reset_index(drop=True)
    # eduData=eduData.drop_duplicates('name').reset_index(drop=True)
    # eduData.to_csv('./temp.csv')
    personData=personData.merge(eduData[['name']+['Age']],how='left')

    return personData

def getStartupParams(startupData,personData):

    startupData = getcityCoord(startupData)

    startupData["founderAgeAvg"] = ""
    startupData["collegeTierAvg"] = ""

    # Get the average of the columns
    for index, row in startupData.iterrows():
        # row["founders"] = row["founders"].replace('\'', '').replace('[', '').replace(']', '')
        # row["founders"] = row["founders"].split(',')
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

def addParamsToData():
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    if (os.path.exists(path + '/../../dataGeneration/output/personData.csv') and os.path.exists(
                path + '/../../dataGeneration/output/startupData.csv')):
        personData = pd.read_csv(path + '/../../dataGeneration/output/personData.csv')
        startupData = pd.read_csv(path + '/../../dataGeneration/output/startupData.csv')
    else:
        startupData, personData = dataConsolidate()
    personData=getPersonParams(personData)
    startupData=getStartupParams(startupData,personData)
    startupData.to_csv(path + '/output/startupData.csv', index=False)
    personData[['F_or_I']+['name']+['Age']+['Tier']+['file_id']].to_csv(path + '/output/personData.csv', index=False)
    return startupData,personData
if __name__ =='__main__':
    addParamsToData()