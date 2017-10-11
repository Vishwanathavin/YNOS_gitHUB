import pandas as pd
import numpy as np
startupData = pd.read_csv('../metaOutput/internKeyurMerge.csv')
crunchbase = pd.read_csv('../metaOutput/crunchbaseData.csv')

# Get the union of rows where no information is present

# startupData['founderName'] = crunchbase[startupData.startupName.isin(crunchbase.startupName)]['founderName']
commonData = crunchbase[crunchbase.startupName.isin(startupData.startupName)]

startupData= pd.merge(startupData,commonData,how='outer',on='startupName')

nullcolumns = startupData[startupData['founderName_x']=='[]']

for index,row in nullcolumns.iterrows():
    startupData.loc[index,'founderName_x'] = startupData.loc[index,'founderName_y']



nullcolumns = startupData[startupData['city_x'].isnull()]
for index,row in nullcolumns.iterrows():
    startupData.loc[index,'city_x'] = startupData.loc[index,'city_y']

nullcolumns = startupData[startupData['website_x'].isnull()]
for index,row in nullcolumns.iterrows():
    startupData.loc[index,'website_x'] = startupData.loc[index,'website_y']
#
startupData["founderName"] = startupData["founderName_x"]
startupData["city"] = startupData["city_x"]
startupData["website"] = startupData["website_x"]
# # for index,row in commonData.iterrows():
# #     print type(row['founderName_x'])
# #     if (row['founderName_x']!=np.nan):
# #         commonData.loc[index,'founderName'] = row['founderName_x']
# #     else:
# #         commonData.loc[index,'founderName'] = row['founderName_y']
# #
# #     if (row['city_x']!=np.nan):
# #         commonData.loc[index,'city'] = row['city_x']
# #     else:
# #         commonData.loc[index,'city'] = row['city_y']
# #
#
startupData.drop(['founderName_x','founderName_y','city_x','city_y','website_x','website_y'],axis=1,inplace=True)
#
# startupData = pd.merge(startupData.drop(['founderName','city','website'],axis=1),commonData[['startupName','founderName','website','city']],how='outer',on='startupName')

startupData.loc[startupData['founderName'].isnull(),'founderName'] = '[]'
# print startupData.columns
startupData.to_csv('../metaOutput/internCrunchbaseMerge.csv', index=False)