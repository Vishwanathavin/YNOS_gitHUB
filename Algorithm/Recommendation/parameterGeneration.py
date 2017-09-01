import pandas as pd
import numpy as np
from datetime import datetime

def getcityCoord(startupData):
    # Getting the co-ordniates from the file
    coordData = pd.read_csv('./data/citi_co-ordinates.csv')
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

    eduData=pd.read_csv('./data/educationData.csv')
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

def getTier(personData):

    eduData=pd.read_csv('./data/educationData.csv')
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