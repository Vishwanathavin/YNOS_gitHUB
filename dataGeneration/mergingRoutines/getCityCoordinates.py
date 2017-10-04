import pandas as pd
import numpy as np
def getCityCoordinates():
    startupData = pd.read_csv('../metaOutput/internCrunchbaseMerge.csv')

    coordData = pd.read_csv('../data/citi_co-ordinates.csv')
    # coordData = pd.read_csv(path+'/data/citi_co-ordinates.csv')
    coordData["City"] = coordData["City"].str.strip()
    coordData.drop_duplicates("City", inplace=True)

    for index, row in startupData.iterrows():
        lat = coordData[row['city'] == coordData['City']]['Lat'].astype(float).values
        lon = coordData[row['city'] == coordData['City']]['Lon'].astype(float).values
        if (lat.size & lon.size):
            startupData.loc[index, "Lat"] = lat
            startupData.loc[index, "Lon"] = lon
        else:
            startupData.loc[index, "Lat"] = np.nan
            startupData.loc[index, "Lon"] = np.nan
    startupData.to_csv('../output/startupData.csv',index=False)
    return startupData
getCityCoordinates()