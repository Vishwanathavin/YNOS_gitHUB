import pandas as pd

def internVIMerge(internDataFunded, viData):
    commonData = pd.merge(internDataFunded, viData, how='inner',left_on=['startupName', 'dealDate'],right_on=['startupName', 'dealDate'])
    internDataFunded = pd.merge(internDataFunded,commonData,how='outer',on=['startupName','dealDate','City','startupClassification','Round_Investment_Amount_INR'])

    internDataFunded = internDataFunded.groupby(["startupName"]).agg(
        {'InvestorName': lambda x: list(x),
         'City': 'first', 'startupClassification': 'first',
         'Round_Investment_Amount_INR': lambda x: list(x),
         'dealDate': lambda x: list(x)}).reset_index()
    for index, row in internDataFunded.iterrows():
        row['InvestorName'] = [x for y, x in sorted(zip(row['dealDate'], row['InvestorName']))]
        row['Round_Investment_Amount_INR'] = [x for y, x in sorted(
            zip(row['dealDate'], row['Round_Investment_Amount_INR']))]
        row['dealDate'] = sorted(row['dealDate'])
        internDataFunded.iloc[index] = row

    return internDataFunded

def internKeyurMerge(internDataFunded,keyurData):

    # Dom a merge instead of Isin
    commonData1 = internDataFunded[~internDataFunded.startupName.isin(keyurData.startupName)]
    commonData2 = keyurData[~keyurData.startupName.isin(internDataFunded.startupName)]
    commonData3 = keyurData[keyurData.startupName.isin(internDataFunded.startupName)]
    startupData = pd.concat([commonData1, commonData2, commonData3], axis=0, ignore_index=True)
    startupData.InvestorName = startupData.InvestorName.astype(str)
    return startupData

def startupCrunchbaseMerge(startupData,crunchbaseData):

    # Do a merge instead of isin
    commonData1 = crunchbaseData[crunchbaseData.startupName.isin(startupData.startupName)]
    startupData = startupData.merge(
    commonData1[['startupName'] + ['founders']],
    on='startupName',
    how='outer')
    startupData.founders = startupData.founders.astype(str)
    return  startupData

def getFounderNames(startupData,personData):
    # Get the relevant founders and Investors
    founderList=[]
    startupData.founders = startupData.founders.astype(str)

    startupData["founders"] = startupData["founders"].str.replace('u\'', '').str.replace('\'', '').str.replace(
        '[', '').str.replace(']', '')
    startupData['founders'] = [x['founders'].split(',') for index, x in startupData.iterrows()]

    for index, row in startupData.iterrows():
        for num in range(len(row['founders'])):
            startupData.iloc[index]['founders'][num] = row['founders'][num].strip()
    founderCount=0
    for index,row in startupData.iterrows():
        for foundername in range(len(row['founders'])):
            founderCount+=1
            Name = personData[personData.name == row.founders[foundername]]["name"].values
            if len(Name):
                founderList.append(Name[0])
    return(pd.DataFrame(founderList,columns=['name']))

def getInvestorNames(startupData,personData):
    invList = []
    invCount = 0
    startupData['InvestorID']=""
    for index, row in startupData.iterrows():
        row["InvestorName"] = row["InvestorName"].replace('u\'', '').replace('\'', '').replace('[', '').replace(']', '')
        row["InvestorName"] = row["InvestorName"].split(',')
        invIDList=[]
        for invName in range(len(row['InvestorName'])):
            row.InvestorName[invName] = row.InvestorName[invName].strip()

            Name = personData[personData.name.values == row.InvestorName[invName]]["name"].values
            ID = personData[personData.name.values == row.InvestorName[invName]]["file_id"].values
            invCount +=1
            if len(Name):
                invList.append(Name[0])
                invIDList.append(ID[0])
        startupData['InvestorID'].iloc[index]=invIDList
    return(pd.DataFrame(invList,columns=['name']),startupData)