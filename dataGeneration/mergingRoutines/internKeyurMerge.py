import pandas as pd

internData = pd.read_csv('../metaOutput/internVImerge.csv')
keyurData = pd.read_csv('../metaOutput/keyurData.csv')

# Dom a merge instead of Isin
commonData1 = internData[~internData.startupName.isin(keyurData.startupName)]
commonData2 = keyurData[~keyurData.startupName.isin(internData.startupName)]
commonData3 = keyurData[keyurData.startupName.isin(internData.startupName)]
startupData = pd.concat([commonData1, commonData2, commonData3], axis=0, ignore_index=True)

startupData.to_csv('../metaOutput/internKeyurMerge.csv', index=False)
