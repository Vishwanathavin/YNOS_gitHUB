import pandas as pd
import numpy as np
startupData = pd.read_csv('../metaOutput/internKeyurMerge.csv')
crunchbase = pd.read_csv('../metaOutput/crunchbaseData.csv')

# Get the union of rows where no information is present

# startupData['founderName'] = crunchbase[startupData.startupName.isin(crunchbase.startupName)]['founderName']
#
commonData = pd.merge(startupData, crunchbase, how='inner',on='startupName')

for index,row in commonData.iterrows():
    if (row['founderName_x']!=np.nan):
        commonData.loc[index,'founderName'] = row['founderName_x']
    else:
        commonData.loc[index,'founderName'] = row['founderName_y']

    if (row['city_x']!=np.nan):
        commonData.loc[index,'city'] = row['city_x']
    else:
        commonData.loc[index,'city'] = row['city_y']


commonData.drop(['founderName_x','founderName_y','city_x','city_y'],axis=1,inplace=True)
startupData.drop(['founderName','city'],axis=1,inplace=True)
startupData = pd.merge(startupData,commonData[['startupName','founderName','website','city']],how='outer',on='startupName')
print startupData.columns
startupData.to_csv('../metaOutput/internCrunchbaseMerge.csv', index=False)