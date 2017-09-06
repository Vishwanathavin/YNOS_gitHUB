import pandas as pd
import numpy as np
from inspect import getsourcefile
import codecs #to handle errors while loading file.
import datetime
import os
def treatment():



    path =  os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))
    # Assign the columns to pick from each of the data sources
    inpColumn = pd.read_csv(path +'/data/dataFromEachSource.csv')

    keyurdata = treatKeyurData(inpColumn,path)
    internDataFunded,internDataNonFunded = treatInternData(inpColumn,path)
    viData = treatVIData(inpColumn,path)
    personData = treatPersonData(inpColumn,path)
    crunchbaseData = treatCrunchbaseData(inpColumn,path)


    # # ---------------------------------------------------------------------
    #
    # # InternData
    # # 1. Fill Nan as '/'''
    # # 2. Convert startup Name to upper case
    # # 3. Remove pvt Ltd from the name
    # # 4. Edit Column Names
    # internData.rename(columns={'Start-up Name': 'startupName',
    #                            'Start up clissification': 'startupClassification',
    #                            'Start up clissification 2': 'startupClassification2',
    #                            'Gorup Classification 1': 'groupClassification1',
    #                            'Gorup Classification 2': 'groupClassification2',
    #                            'Gorup Classification 3': 'groupClassification3',
    #                            '140 character description': 'description',
    #                            'Business model Classification': 'businessModel',
    #                            'Round1 Investment amount (Rupees Crores)': 'investmentAmount',
    #                            'Round1 date': 'dealDate'
    #                            }, inplace=True)
    # internData = internData[internColumns]
    # internData.startupName = internData.startupName.astype(str).apply(lambda x: x.upper())
    # internData.startupName = internData.startupName.str.strip()
    # #internData = internData.drop_duplicates(['startupName'])
    # internData.startupName = internData.startupName.str.replace('PVT','').replace('LTD.','').replace('PRIVATE','').replace('LIMITED','')
    # internData.City.replace(' ', np.nan, inplace=True)
    # internDataNonFunded = internData[internData["dealDate"].isnull()]
    # internDataFunded = internData[internData["dealDate"].notnull()]
    #
    # # internData = internData.dropna(subset=['City'], how='any')
    # # internData = internData.dropna(subset=['startupClassification'], how='any')
    # # ---------------------------------------------------------------------
    #
    # # Keyur Data
    # # 1. Fill Nan as '/'''
    # # 2. Convert startup Name to upper case
    # # 3. Remove pvt Ltd from the name
    # # 4. Rename columns
    # # 5. Merge Investor names, investment amount
    #
    # # keyurData.DOI = keyurData.DOI.astype(str)
    #
    # keyurData['DOI'].replace('', np.nan, inplace=True)
    # keyurData = keyurData[(keyurData['DOI'] >= 2014) | (keyurData['DOI'].isnull())]
    #
    # keyurData.rename(columns={'Company Name': 'startupName',
    #                           'ICB Industry': 'Industry',
    #                           'ICB Sector': 'Sector',
    #                           'Start up Classification': 'startupClassification',
    #                           'Investor Name': 'InvestorName',
    #                           'Round Investment Amount (INR M)': 'Round_Investment_Amount_INR_M',
    #                           # 'Deal Investment Amount ( INR M)': 'Deal_Investment_Amount_INR_M',
    #                           'Announcement Date': 'dealDate'
    #                           }, inplace=True)
    # keyurData = keyurData[keyurColumns]
    # keyurData = keyurData.groupby(["startupName"]).agg(
    #     {'InvestorName': lambda x: list(x),
    #      'Round_Investment_Amount_INR_M': lambda x: list(x),
    #      'dealDate': lambda x: list(x)}).reset_index()
    # keyurData.startupName = keyurData.startupName.str.strip()
    # for index, row in keyurData.iterrows():
    #     row['InvestorName'] = [x for y, x in sorted(zip(row['dealDate'], row['InvestorName']))]
    #     row['Round_Investment_Amount_INR_M'] = [x for y, x in sorted(
    #         zip(row['dealDate'], row['Round_Investment_Amount_INR_M']))]
    #     row['dealDate'] = sorted(row['dealDate'])
    #     keyurData.iloc[index] = row
    # # keyurData = keyurData.groupby(["startupName"]).agg(
    # #     {'InvestorName': lambda x: list(sorted(set(list(x))))}).reset_index()
    #
    # #                              NOTE
    # ##                             NOTE
    # ##                 The sorting of the date, round investment amount has an issue. It is not ordered. Take care
    # #
    # keyurData.startupName = keyurData.startupName.astype(str).apply(lambda x: x.upper())
    # keyurData.startupName = keyurData.startupName.str.replace('PVT', '').replace('LTD.', '').replace('PRIVATE', '').replace('LIMITED', '')
    # keyurData.InvestorName = keyurData.InvestorName.astype(str).apply(lambda x: x.upper())
    #
    # # ---------------------------------------------------------------------
    #
    # # Crunchbase file
    # # 1. Replace newline, braces, etc
    # # 2. Fix unicode
    # # 3. Convert to pandas
    #
    # crunchbaseFile = crunchbaseFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    # crunchbaseData = pd.read_json(crunchbaseFile, lines=True)
    # crunchbaseData.rename(columns={'company': 'startupName'}, inplace=True)
    # crunchbaseData = crunchbaseData[crunchbaseColumns]
    # crunchbaseData.startupName = crunchbaseData.startupName.astype(str).apply(lambda x: x.upper())
    #
    # crunchbaseData.startupName = crunchbaseData.startupName.str.replace('PVT', '').replace('LTD.', '').replace('PRIVATE','').replace('LIMITED', '')
    # crunchbaseData.startupName = crunchbaseData.startupName.str.strip()
    # crunchbaseData.to_csv('./Crunchbase_asis.csv')
    # crunchbaseData = crunchbaseData.drop_duplicates(['startupName'])
    # crunchbaseData = crunchbaseData [crunchbaseData.astype(str)['founders'] != '[]']
    # for index in range(crunchbaseData.shape[0]):
    #     # print index,crunchbaseData.iloc[index].startupName,len(crunchbaseData.iloc[index].founders),crunchbaseData.iloc[index].founders
    #     val = [crunchbaseData.iloc[index]['founders'][x].encode('ascii', 'ignore') for x in
    #            range(len(crunchbaseData.iloc[index].founders))]
    #     crunchbaseData.founders.iloc[index] = val
    # crunchbaseData.founders = crunchbaseData.founders.astype(str).apply(lambda x: x.upper())
    # #
    # # crunchbaseData["founders"].str.split(',').tolist()
    # # crunchbaseData["founders"] = crunchbaseData["founders"].astype(str).replace('u\'', '').replace('\'', '').replace('[','').replace(']', '')
    #
    # # ----------------------------------------------------------------------
    #
    # # Venture Intelligence data
    # # 1. Fill Nan as '/'''
    # # 2. Convert startup Name to upper case
    # # Change column name
    #
    # viData.rename(columns={'Company': 'startupName', 'Investors': 'InvestorName'}, inplace=True)
    # viData = viData[VIColumns]
    # # viData = viData.drop_duplicates('startupName')
    # viData.startupName = viData.startupName.astype(str).apply(lambda x: x.upper())
    # viData.InvestorName = viData.InvestorName.astype(str).apply(lambda x: x.upper())
    # viData.startupName = viData.startupName.str.replace('(', '').str.replace(')','')
    # # Convertthe date of investment
    #
    # #personFile
    # # 1. Replace newline, braces, etc
    # # 2. Fix unicode
    # # 3. Convert to pandas
    # invFile = invFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    # invData = pd.read_json(invFile, lines=True)
    # invData.name = invData.name.apply(lambda x: x.upper())
    # # invData = invData.drop_duplicates('name')
    # founderFile = founderFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    # founderData = pd.read_json(founderFile, lines=True)
    # founderData.name = founderData.name.apply(lambda x: x.upper())
    # # founderData = founderData.drop_duplicates('name')
    # founderData['F_or_I'] = 'F'
    # invData['F_or_I'] = 'I'
    # personData = founderData.append(invData)
    #
    # seriesList = []
    # for row in range(personData.shape[0]):
    #     for schoolIndex in range(len(personData.iloc[row]["schools"])):
    #         schseries = pd.Series(
    #             [personData.iloc[row]["name"], personData.iloc[row]["schools"][schoolIndex]["duration"],
    #              personData.iloc[row]["schools"][schoolIndex]["college"],
    #              personData.iloc[row]["schools"][schoolIndex]["degree"], personData.iloc[row]["F_or_I"]],
    #             index=['name', 'duration', 'college', 'degree', 'F_or_I'])
    #         seriesList.append(schseries)
    # educationData = pd.DataFrame(seriesList)
    #
    # seriesList = []
    #
    # for row in range(personData.shape[0]):
    #     for expIndex in range(len(personData.iloc[row]["experience"])):
    #         expseries = pd.Series(
    #             [personData.iloc[row]["name"], personData.iloc[row]["experience"][expIndex]["position"],
    #              personData.iloc[row]["experience"][expIndex]["company"],
    #              personData.iloc[row]["experience"][expIndex]["duration"], personData.iloc[row]["F_or_I"]],
    #             index=['name', 'position', 'company', 'duration', 'F_or_I'])
    #         seriesList.append(expseries)
    # expData = pd.DataFrame(seriesList)

    return keyurdata,internDataFunded,internDataNonFunded,viData,personData,crunchbaseData

def treatKeyurData(inpColumn,path):

    keyurColumns = inpColumn['keyurColumns'].dropna().tolist()
    # loading file using codecs to handle errors
    with codecs.open(path + '/data/keyur.csv', "r", encoding='utf-8',errors='ignore') as keyur_temp:
        keyurData = pd.read_csv(keyur_temp)




    keyurData.rename(columns={'Company Name': 'startupName',
                              'ICB Industry': 'Industry',
                              'ICB Sector': 'Sector',
                              'Start up Classification': 'startupClassification',
                              'Investor Name': 'InvestorName',
                              'Round Investment Amount (INR M)': 'Round_Investment_Amount_INR',
                              # 'Deal Investment Amount ( INR M)': 'Deal_Investment_Amount_INR_M',
                              'Announcement Date': 'dealDate'
                              }, inplace=True)

    keyurData = keyurData[keyurColumns]

    keyurData['dealDate'] = pd.to_datetime(keyurData['dealDate'], format="%m/%d/%Y")

    # keyurData['DOI'].replace('', np.nan, inplace=True)
    # keyurData = keyurData[(keyurData['DOI'] >= 2014) | (keyurData['DOI'].isnull())]
    keyurData = keyurData[(keyurData['dealDate'] > '2014-01-01')]

    keyurData = keyurData.groupby(["startupName"]).agg(
        {'InvestorName': lambda x: list(x),
         'Round_Investment_Amount_INR': lambda x: list(x),
         'dealDate': lambda x: list(x),
         'City':'first'}).reset_index()

    keyurData.startupName = keyurData.startupName.str.strip()


    for index, row in keyurData.iterrows():
        row['InvestorName'] = [x for y, x in sorted(zip(row['dealDate'], row['InvestorName']))]
        row['Round_Investment_Amount_INR'] = [x for y, x in sorted(
            zip(row['dealDate'], row['Round_Investment_Amount_INR']))]
        row['dealDate'] = sorted(row['dealDate'])
        keyurData.iloc[index] = row
    # Get the investor name as a list of lists
    keyurData.startupName = keyurData.startupName.astype(str).apply(lambda x: x.upper())
    keyurData.startupName = keyurData.startupName.str.replace('PVT.', '').str.replace('LTD.', '').str.replace('PRIVATE','').str.replace('LIMITED', '').str.strip()
    keyurData.InvestorName = keyurData.InvestorName.astype(str).apply(lambda x: x.upper())
    keyurData.to_csv(path.replace("\\","/")+'/metaOutput/keyurData.csv', index=False)
    return keyurData



#-------------------------------------------------------------------------
#
#
def treatInternData(inpColumn,path):
    internColumns = inpColumn['internColumns'].dropna().tolist()
    # loading file using codecs to handle errors
    with codecs.open(path + '/data/interns.csv', "r", encoding='utf-8', errors='ignore') as intern_temp:
        internData = pd.read_csv(intern_temp)
    # internData = pd.read_csv(path + '/data/interns.csv')
    # ---------------------------------------------------------------------

    # InternData
    # 1. Fill Nan as '/'''
    # 2. Convert startup Name to upper case
    # 3. Remove pvt Ltd from the name
    # 4. Edit Column Names
    internData.rename(columns={'Start-up Name': 'startupName',
                               'Start up clissification': 'startupClassification',
                               'Start up clissification 2': 'startupClassification2',
                               'Gorup Classification 1': 'groupClassification1',
                               'Gorup Classification 2': 'groupClassification2',
                               'Gorup Classification 3': 'groupClassification3',
                               '140 character description': 'description',
                               'Business model Classification': 'businessModel',
                               'Round1 Investment amount (Rupees Crores)': 'Round_Investment_Amount_INR',
                               'Round1 date': 'dealDate'
                               }, inplace=True)
    internData = internData[internColumns]
    internData.startupName = internData.startupName.astype(str).apply(lambda x: x.upper())
    internData.startupName = internData.startupName.str.strip()
    # internData = internData.drop_duplicates(['startupName'])
    internData.startupName = internData.startupName.str.replace('PVT', '').replace('LTD.', '').replace('PRIVATE','').replace('LIMITED', '')



    internData['dealDate'] = pd.to_datetime(internData['dealDate'], format="%m/%y")
    internDataNonFunded = internData[internData["dealDate"].isnull()]
    internDataFunded = internData[internData["dealDate"].notnull()]
    # internDataFunded.dealDate = internDataFunded.dealDate.str.replace('January', 'Jan').str.replace \
    #     ('February', 'Feb').str.replace('March', 'Mar').str.replace('April', 'Apr') \
    #     .str.replace('June', 'Jun').str.replace('July', 'Jul').str.replace \
    #     ('August', 'Aug').str.replace('September', 'Sep').str.replace('October', 'Oct') \
    #     .str.replace('November', 'Nov').str.replace('December', 'Dec').str.replace('20', '')
    #
    # # Get the deal date in the same format as keyur Data
    # internDataFunded.dealDate = internDataFunded.dealDate.str.replace('Jan', '01').str.replace \
    #     ('Feb', '02').str.replace('Mar', '03').str.replace('Apr', '04').str.replace('May', '05') \
    #     .str.replace('Jun', '06').str.replace('Jul', '07').str.replace \
    #     ('Aug', '08').str.replace('Sep', '09').str.replace('Oct', '10') \
    #     .str.replace('Nov', '11').str.replace('Dec', '12').str.replace('-', '/')
    # internDataFunded.dealDate = internDataFunded.dealDate.astype(str).apply(lambda x: x.upper())

    # internDataFunded.dealDate = internDataFunded.dealDate.str.split('-').tolist()
    #
    # for index, row in internDataFunded.iterrows():
    #     datetime_object = datetime.strptime(row.dealDate[0],row.dealDate[1], '%b %Y')
    #     print datetime_object
    internDataFunded.to_csv(path.replace("\\","/")+'/metaOutput/internDataFunded.csv', index=False)
    internDataNonFunded.to_csv(path.replace("\\","/")+'/metaOutput/internDataNonFunded.csv', index=False)
    return internDataFunded,internDataNonFunded

def treatVIData(inpColumn,path):
    VIColumns = inpColumn['VIColumns'].dropna().tolist()
    # loading file using codecs to handle errors
    with codecs.open(path + '/data/ventureIntelligence.csv', "r", encoding='utf-8', errors='ignore') as vi_temp:
        viData = pd.read_csv(vi_temp)
    # ----------------------------------------------------------------------

    # Venture Intelligence data
    # 1. Fill Nan as '/'''
    # 2. Convert startup Name to upper case
    # Change column name

    viData.rename(columns={'Company': 'startupName', 'Investors': 'InvestorName','Date':'dealDate'}, inplace=True)
    viData = viData[VIColumns]
    # viData = viData.drop_duplicates('startupName')
    viData.startupName = viData.startupName.astype(str).apply(lambda x: x.upper())
    viData.InvestorName = viData.InvestorName.astype(str).apply(lambda x: x.upper())
    viData.startupName = viData.startupName.str.replace('(', '').str.replace(')', '')

    viData['dealDate'] = pd.to_datetime(viData['dealDate'], format="%B-%Y")

    # Get the date in the same format as keyur Data

    viData.to_csv(path.replace("\\","/")+'/metaOutput/viData.csv', index=False)
    return viData

#--------------------------------------------------------------------
#
#
def treatPersonData(inpColumn,path):
    founderFile = open(path + '/data/founders_profiles_new.json').read()
    invFile = open(path + '/data/Investor_final.json').read()

    invFile = invFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    invData = pd.read_json(invFile, lines=True)
    invData.name = invData.name.apply(lambda x: x.upper())


    founderFile = founderFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    founderData = pd.read_json(founderFile, lines=True)
    founderData.name = founderData.name.apply(lambda x: x.upper())


    founderData['F_or_I'] = 'F'
    invData['F_or_I'] = 'I'
    personData = founderData.append(invData)

    seriesList = []
    for row in range(personData.shape[0]):
        for schoolIndex in range(len(personData.iloc[row]["schools"])):
            schseries = pd.Series(
                [personData.iloc[row]["name"], personData.iloc[row]["schools"][schoolIndex]["duration"],
                 personData.iloc[row]["schools"][schoolIndex]["college"],
                 personData.iloc[row]["schools"][schoolIndex]["degree"], personData.iloc[row]["F_or_I"]],
                index=['name', 'duration', 'college', 'degree', 'F_or_I'])
            seriesList.append(schseries)
    educationData = pd.DataFrame(seriesList)
    educationData['college']=educationData['college'].apply(lambda x: x.upper())
    educationData['degree']=educationData['degree'].apply(lambda x: x.upper())
    seriesList = []

    for row in range(personData.shape[0]):
        for expIndex in range(len(personData.iloc[row]["experience"])):
            expseries = pd.Series(
                [personData.iloc[row]["name"], personData.iloc[row]["experience"][expIndex]["position"],
                 personData.iloc[row]["experience"][expIndex]["company"],
                 personData.iloc[row]["experience"][expIndex]["duration"], personData.iloc[row]["F_or_I"]],
                index=['name', 'position', 'company', 'duration', 'F_or_I'])
            seriesList.append(expseries)
    expData = pd.DataFrame(seriesList)
    personData[['name']+['F_or_I']+['file_id']].to_csv(path+'/metaOutput/personData.csv', index=False, encoding='utf-8')
    expData.to_csv(path.replace("\\","/")+'/metaOutput/expData.csv', index=False, encoding='utf-8')
    educationData.to_csv(path.replace("\\","/")+'/metaOutput/educationData.csv', index=False, encoding='UTF8')
    return personData

def treatCrunchbaseData(inpColumn,path):
    crunchbaseColumns = inpColumn['crunchbaseColumns'].dropna().tolist()
    crunchbaseFile = open(path + '/data/startupProfiles.json').read()
    # ---------------------------------------------------------------------

    # Crunchbase file
    # 1. Replace newline, braces, etc
    # 2. Fix unicode
    # 3. Convert to pandas

    crunchbaseFile = crunchbaseFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    crunchbaseData = pd.read_json(crunchbaseFile, lines=True)
    crunchbaseData.rename(columns={'company': 'startupName'}, inplace=True)
    crunchbaseData = crunchbaseData[crunchbaseColumns]
    crunchbaseData.startupName = crunchbaseData.startupName.astype(str).apply(lambda x: x.upper())

    crunchbaseData.startupName = crunchbaseData.startupName.str.replace('PVT', '').replace('LTD.', '').replace(
        'PRIVATE', '').replace('LIMITED', '')
    crunchbaseData.startupName = crunchbaseData.startupName.str.strip()
    crunchbaseData = crunchbaseData.drop_duplicates(['startupName']).reset_index(drop=True)
    crunchbaseData = crunchbaseData[crunchbaseData.astype(str)['founders'] != '[]'].reset_index(drop=True)
    for index in range(crunchbaseData.shape[0]):
        # print index,crunchbaseData.iloc[index].startupName,len(crunchbaseData.iloc[index].founders),crunchbaseData.iloc[index].founders
        val = [crunchbaseData.iloc[index]['founders'][x].encode('ascii', 'ignore') for x in
               range(len(crunchbaseData.iloc[index].founders))]
        crunchbaseData.founders.iloc[index] = val
    crunchbaseData.founders = crunchbaseData.founders.astype(str).apply(lambda x: x.upper())

    crunchbaseData.to_csv(path.replace("\\","/")+'/metaOutput/crunchbaseData.csv', index=False, encoding='UTF8')

    return crunchbaseData
# ---------------------------------------------------------------------------------
#
#

if __name__=='__main__':
    treatment()




  #---------------------------------------------------------------------

    # InternData
    # 1. Fill Nan as '/'''
    # 2. Convert startup Name to upper case
    # 3. Remove pvt Ltd from the name
    # 4. Edit Column Names
    # internData.rename(columns={'Start-up Name':'startupName',
    #                           'Start up clissification':'startupClassification',
    #                           'Start up clissification 2':'startupClassification2',
    #                           'Gorup Classification 1':'groupClassification1',
    #                           'Gorup Classification 2':'groupClassification2',
    #                           'Gorup Classification 3':'groupClassification3',
    #                           '140 character description':'description',
    #                           'Business model Classification':'businessModel'}, inplace=True)
    # internData=internData[internColumns]
    # internData.startupName = internData.startupName.astype(str).apply(lambda x: x.upper())
    #
    # # ---------------------------------------------------------------------
    #
    # # Keyur Data
    # # 1. Fill Nan as '/'''
    # # 2. Convert startup Name to upper case
    # # 3. Remove pvt Ltd from the name
    # # 4. Rename columns
    # # 5. Merge Investor names, investment amount
    # keyurData.rename(columns={'Company Name':'startupName',
    #                           'ICB Industry': 'Industry',
    #                           'ICB Sector': 'Sector',
    #                           'Start up Classification': 'startupClassification',
    #                           'Investor Name': 'investorName',
    #                           'Deal Investment Amount ( INR M)': 'Deal_Investment_Amount_INR_M'
    #                           },inplace=True)
    # keyurData=keyurData[keyurColumns]
    # # keyurData
    # # keyurData.DOI = keyurData.DOI.astype(str)
    # # keyurData.Deal_Investment_Amount_INR_M = keyurData.Deal_Investment_Amount_INR_M.astype(str)
    # keyurData = keyurData.groupby(["startupName"]).agg(
    #     {'Industry': 'first', 'investorName': lambda x: list(x), 'Deal_Investment_Amount_INR_M': lambda x: list(x),
    #      'DOI': 'first','Source':'first','startupClassification':'first'}).reset_index()
    #
    # keyurData.startupName = keyurData.startupName.astype(str).apply(lambda x: x.upper())
    # keyurData.investorName = keyurData.investorName.astype(str).apply(lambda x: x.upper())
    # # print keyurData.columns
    # # keyurData.to_csv('./temp.csv')
    # # ---------------------------------------------------------------------
    #
    # # Crunchbase file
    # # 1. Replace newline, braces, etc
    # # 2. Fix unicode
    # # 3. Convert to pandas
    #
    # crunchbaseFile=crunchbaseFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    # crunchbaseData=pd.read_json(crunchbaseFile,lines=True)
    # crunchbaseData.rename(columns={'company': 'startupName'},inplace=True)
    # crunchbaseData=crunchbaseData[crunchbaseColumns]
    # crunchbaseData.startupName = crunchbaseData.startupName.astype(str).apply(lambda x: x.upper())
    # crunchbaseData=crunchbaseData.drop_duplicates(['startupName'])
    # # ----------------------------------------------------------------------
    #
    # # Venture Intelligence data
    # # 1. Fill Nan as '/'''
    # # 2. Convert startup Name to upper case
    # # Change column name
    #
    # viData.rename(columns={'Company': 'startupName','Investors':'investorName'}, inplace=True)
    # viData=viData[VIColumns]
    # viData = viData.drop_duplicates('startupName')
    # viData.startupName = viData.startupName.replace('(','').replace(')','')
    # viData.startupName = viData.startupName.astype(str).apply(lambda x: x.upper())
    # viData.investorName = viData.investorName.astype(str).apply(lambda x: x.upper())
    #----------------------------------------------------------------------

