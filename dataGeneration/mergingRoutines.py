import pandas as pd

def internVIMerge(internData, viData):


    # Get the intersection of common data from Vi and intern funded
    commonData = pd.merge(internData, viData, how='inner',on='startupName')

    internColumns = ['source', 'startupName', 'foundedDate' ,'description', 'ICB_industry',
                     'ICB_sector' ,'startupClassification', 'businessModel', 'city', 'state',
                     'startupStatus' ,'keyword' ,'groupClassification', 'roundDate',
                     'roundInvestorCount' ,'roundLeadInvestorType', 'roundInvestmentAmount',
                     'roundValuation']
    # # Get the union of the data between the commond data and intern funded. This way we get to add teh investor name column to the list of the intern data
    internData = pd.merge(internData,commonData,how='outer',on=internColumns)

    # for column in internDataFunded:
    #     print column,type(internDataFunded.iloc[0][column])

    # Merge the round and other information

    # Commenting the earlier instance of grouping since it is not longer happening
    internData = internData.groupby(["startupName"]).agg(
        {'investorName': lambda x: list(x),
         'source': 'first',
         'foundedDate': 'first',
         'description': 'first',
         'ICB_industry': 'first',
         'ICB_sector': 'first',
         'startupClassification': 'first',
         'businessModel': 'first',
         'city': 'first',
         'state': 'first',
         'startupStatus': 'first',
         'keyword': 'first',
         'groupClassification': 'first',
         'roundDate': 'first',
         'roundInvestorCount': 'first',
         'roundLeadInvestorType': 'first',
         'roundInvestmentAmount': 'first',
         'roundValuation': 'first'
         }).reset_index()

    # for index, row in internDataFunded.iterrows():
    #     row['InvestorName'] = [x for y, x in sorted(zip(row['dealDate'], row['InvestorName']))]
    #     row['Round_Investment_Amount_INR'] = [x for y, x in sorted(
    #         zip(row['dealDate'], row['Round_Investment_Amount_INR']))]
    #     row['dealDate'] = sorted(row['dealDate'])
    #     internDataFunded.iloc[index] = row

    return internData

def internKeyurMerge(internDataFunded,keyurData):

    # Dom a merge instead of Isin
    commonData1 = internDataFunded[~internDataFunded.startupName.isin(keyurData.startupName)]
    commonData2 = keyurData[~keyurData.startupName.isin(internDataFunded.startupName)]
    commonData3 = keyurData[keyurData.startupName.isin(internDataFunded.startupName)]
    startupData = pd.concat([commonData1, commonData2, commonData3], axis=0, ignore_index=True)
    return startupData

def startupCrunchbaseMerge(startupData,crunchbaseData):

    # Do a merge instead of isin
    commonData1 = crunchbaseData[crunchbaseData.startupName.isin(startupData.startupName)]
    startupData = startupData.merge(
    commonData1[['startupName'] + ['founderName']],
    on='startupName',
    how='outer')
    # startupData.founders = startupData.founders.astype(str)
    return  startupData

def getFounderNames(startupData,personData):
    # Get the relevant founders and Investors
    founderList=[]

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