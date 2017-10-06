import pandas as pd
import numpy as np
startupData = pd.read_csv('../metaOutput/internKeyurMerge.csv')
crunchbase = pd.read_csv('../metaOutput/crunchbaseData.csv')

# Get the union of rows where no information is present

# startupData['founderName'] = crunchbase[startupData.startupName.isin(crunchbase.startupName)]['founderName']

commonData = pd.merge(startupData, crunchbase, how='inner',on='startupName')
nullcolumns = commonData[commonData['founderName_x'].isnull()]

for index,row in nullcolumns.iterrows():
    commonData.loc[index,'founderName_x'] = commonData.loc[index,'founderName_y']
#
nullcolumns = commonData[commonData['city_x'].isnull()]
for index,row in nullcolumns.iterrows():
    commonData.loc[index,'city_x'] = commonData.loc[index,'city_y']

nullcolumns = commonData[commonData['website_x'].isnull()]
for index,row in nullcolumns.iterrows():
    commonData.loc[index,'website_x'] = commonData.loc[index,'website_y']
#
commonData["founderName"] = commonData["founderName_x"]
commonData["city"] = commonData["city_x"]
commonData["website"] = commonData["website_x"]
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
commonData.drop(['founderName_x','founderName_y','city_x','city_y','website_x','website_y'],axis=1,inplace=True)
#
startupData = pd.merge(startupData.drop(['founderName','city','website'],axis=1),commonData[['startupName','founderName','website','city']],how='outer',on='startupName')
# print startupData.columns
startupData.to_csv('../metaOutput/internCrunchbaseMerge.csv', index=False)