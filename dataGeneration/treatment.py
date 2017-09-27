import pandas as pd

from inspect import getsourcefile
import codecs #to handle errors while loading file.
import numpy as np
import os
import json
def treatment():



    path =  os.path.dirname(os.path.abspath(getsourcefile(lambda:0))) # .replace("\\","/")
    # path = path.replace("\\","/")
    # Assign the columns to pick from each of the data sources
    inpColumn = pd.read_csv(path +'/data/dataFromEachSource.csv')
    keyurdata=0.0
    internDataFunded=0.0
    internDataNonFunded=0.0
    viData=0.0
    personData=0.0
    crunchbaseData=0.0

    keyurdata = treatKeyurData(inpColumn,path)
    internData= treatInternData(inpColumn,path)
    # internDataFunded,internDataNonFunded = treatInternData(inpColumn,path)
    viData = treatVIData(inpColumn,path)
    personData = treatPersonData(inpColumn,path)
    crunchbaseData = treatCrunchbaseData(inpColumn,path)




    return keyurdata,internData,viData,crunchbaseData

def treatKeyurData(inpColumn,path):

    keyurColumns = inpColumn['keyurColumns'].dropna().tolist()
    # loading file using codecs to handle errors
    with codecs.open(path + '/data/keyur.csv', "r", encoding='utf-8',errors='ignore') as keyur_temp:
        keyurData = pd.read_csv(keyur_temp)




    keyurData.rename(columns={'Source' 	:	'source',
            'Company Name' 	:	'startupName',
            'ICB Industry' 	:	'ICB_industry',
            'ICB Sector' 	:	'ICB_sector',
            'Start up Classification' 	:	'startupClassification',
            'DOI' 	:	'foundedDate',
            'Investor Name' 	:	'investorName',
            'links' 	:	'linkedinURL',
            'Investor Type 1 (Angel / Institutional Investor/ Boutique / Corporate / Network)' 	:	'investorType',
            'Deal Investment Amount ( INR M)' 	:	'dealInvestmentAmount',
            'Round Investment Amount (INR M)' 	:	'roundInvestmentAmount',
            'Stage of Investment ( Seed / Early)' 	:	'investmentStage',
            'New Stage Classification' 	:	'stageClassification',
            'Announcement Date' 	:	'roundDate',
            'Equity Valuation (INR M)' 	:	'equityValuation',
            'City' 	:	'city',
            'State' 	:	'state',
            'Website' 	:	'companyWebsite'
                              }, inplace=True)

    keyurData = keyurData[keyurColumns]

    keyurData['roundDate'] = pd.to_datetime(keyurData['roundDate'], format="%m/%d/%Y")

    # keyurData['DOI'].replace('', np.nan, inplace=True)
    # keyurData = keyurData[(keyurData['DOI'] >= 2014) | (keyurData['DOI'].isnull())]
    keyurData = keyurData[(keyurData['roundDate'] > '2014-01-01')]

    keyurData = keyurData.groupby(["startupName"]).agg(
        {
            'ICB_industry':'first',
           'ICB_sector':'first',
         'foundedDate':'first',
         'startupClassification':'first',
        'investorName': lambda x: list(x),
         'linkedinURL': lambda x: list(x),
         'roundInvestmentAmount': lambda x: list(x),
         'investorType': lambda x: list(x),
         'dealInvestmentAmount': lambda x: list(x),
         'investmentStage': lambda x: list(x),
         'stageClassification': lambda x: list(x),
         'equityValuation': lambda x: list(x),
         'roundDate': lambda x: list(x),
         'city':'first',
         'state':'first',
         'companyWebsite':'first',
         'source':'first'

         }).reset_index()

    keyurData.startupName = keyurData.startupName.str.strip()


    for index, row in keyurData.iterrows():
        outTuple = [(x1, x2,x3,x4,x5,x6,x7,x8)
                    for y, x1, x2,x3,x4,x5,x6,x7,x8 in
                    sorted(zip(row['roundDate'],row['investorName'],
                          row['linkedinURL'],row['roundInvestmentAmount'],
                          row['investorType'],row['dealInvestmentAmount'],
                          row['investmentStage'],row['stageClassification'],
                          row['equityValuation']))]
        row['roundDate'] = sorted(row['roundDate'])

        row['investorName'] = [x[0] for x in outTuple]
        row['linkedinURL'] = [x[1] for x in outTuple]
        row['roundInvestmentAmount'] = [x[2] for x in outTuple]
        row['investorType'] = [x[3] for x in outTuple]
        row['dealInvestmentAmount'] = [x[4] for x in outTuple]
        row['investmentStage'] = [x[5] for x in outTuple]
        row['stageClassification'] = [x[6] for x in outTuple]
        row['equityValuation'] = [x[7] for x in outTuple]

        keyurData.iloc[index] = row
    # Get the investor name as a list of lists
    keyurData.startupName = keyurData.startupName.astype(str).apply(lambda x: x.upper())
    keyurData.startupName = keyurData.startupName.str.replace('PVT.', '').str.replace('LTD.', '').str.replace('PRIVATE','').str.replace('LIMITED', '').str.strip()
    keyurData.investorName = keyurData.investorName.astype(str).apply(lambda x: x.upper())
    keyurData.to_csv(path+'/metaOutput/keyurData.csv', index=False)
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

    internData.rename(columns={'Source': 	'source',
        'Start-up Name': 	'startupName',
        'Date of Inc': 	'foundedDate',
        '140 character description': 	'description',
        'Industry': 	'ICB_industry',
        'Sector': 	'ICB_sector',
        'Start up clissification': 	'startupClassification',
        'Start up clissification 2': 	'startupClassification2',
        'Business model Classification': 	'businessModel',
        'Keyword1': 	'keyword1',
        'Keyword2': 	'keyword2',
        'Keyword3': 	'keyword3',
        'City': 	'city',
        'State': 	'state',
        'Status': 	'startupStatus',
        'Gorup Classification 1': 	'groupClassification1',
        'Gorup Classification 2': 	'groupClassification2',
        'Gorup Classification 3': 	'groupClassification3',
        'Round1 date': 	'round1Date',
        'Round1 Total investors': 	'round1InvestorCount',
        'Round1 Lead Investor type': 	'round1LeadInvestorType',
        'Round1 Investment amount (Rupees Crores)': 	'round1InvestmentAmount',
        'Round1 Valuation (Rupees, Crores)': 	'round1Valuation',
        'Round2 date': 	'round2Date',
        'Round2 Total investors': 	'round2InvestorCount',
        'Round2 Lead Investor type': 	'round2LeadInvestorType',
        'Round2 Investment amount (Rupees Crores)': 	'round2InvestmentAmount',
        'Round2 Valuation (Rupees Crores)': 	'round2Valuation',
        'Round3 date': 	'round3Date',
        'Round3 Total investors': 	'round3InvestorCount',
        'Round3 Lead Investor type': 	'round3LeadInvestorType',
        'Round3 Investment amount (Rupees, Crores)': 	'round3InvestmentAmount',
        'Round3 Valuation (Rupees Crores)':	'round3Valuation'
                               }, inplace=True)
    internData = internData[internColumns]

    internData.startupName = internData.startupName.astype(str).apply(lambda x: x.upper())
    internData.startupName = internData.startupName.str.strip()

    internData.startupName = internData.startupName.str.replace('PVT', '').str.replace('LTD.', '').str.replace('PRIVATE','').str.replace('LIMITED', '')

    # Do all the merging of the columns. Convert into array whereever possible
    internData['round1Date'] = pd.to_datetime(internData['round1Date'], format="%m/%y")
    internData['round2Date'] = pd.to_datetime(internData['round2Date'], format="%m/%y")
    internData['round3Date'] = pd.to_datetime(internData['round3Date'], format="%m/%y")
    internData['foundedDate'] = pd.to_datetime(internData['foundedDate'], format='%Y.0')

    internData.fillna('',inplace=True)
    internData['startupClassification'] = [list(val) for val in(zip(internData['startupClassification'],internData['startupClassification2']))]
    internData['keyword'] = [list(val) for val in(zip(internData['keyword1'],internData['keyword2'],internData['keyword3']))]
    internData['groupClassification'] = [list(val) for val in (zip(internData['groupClassification1'],internData['groupClassification2'],internData['groupClassification3']))]
    internData['roundDate'] = [list(val) for val in(zip(internData['round1Date'],internData['round2Date'],internData['round3Date']))]
    internData['roundInvestorCount'] = [list(val) for val in(zip(internData['round1InvestorCount'],internData['round2InvestorCount'],internData['round3InvestorCount']))]
    internData['roundLeadInvestorType'] = [list(val) for val in(zip(internData['round1LeadInvestorType'],internData['round2LeadInvestorType'],internData['round3LeadInvestorType']))]
    internData['roundInvestmentAmount'] = [list(val) for val in(zip(internData['round1InvestmentAmount'],internData['round2InvestmentAmount'],internData['round2InvestmentAmount']))]
    internData['roundValuation'] = [list(val) for val in(zip(internData['round1Valuation'],internData['round2Valuation'],internData['round3Valuation']))]


    dropColumns = ['startupClassification2',
                    'keyword1',
                    'keyword2',
                    'keyword3',
                    'groupClassification1',
                    'groupClassification2',
                    'groupClassification3',
                    'round1Date',
                    'round1InvestorCount',
                    'round1LeadInvestorType',
                    'round1InvestmentAmount',
                    'round1Valuation',
                    'round2Date',
                    'round2InvestorCount',
                    'round2LeadInvestorType',
                    'round2InvestmentAmount',
                    'round2Valuation',
                    'round3Date',
                    'round3InvestorCount',
                    'round3LeadInvestorType',
                    'round3InvestmentAmount',
                    'round3Valuation']
    internData.drop( dropColumns,axis=1,inplace=True)
    # internDataNonFunded.drop(dropColumns,axis=1,inplace=True)
    #
    # # internDataNonFunded = internData.loc[:,"roundDate"][0]
    # # internDataFunded = internData.loc[:,"roundDate"][0].notnull()
    # internDataFunded.to_csv(path+'/metaOutput/internDataFunded.csv', index=False)
    # internDataNonFunded.to_csv(path+'/metaOutput/internDataNonFunded.csv', index=False)
    internData.to_csv(path+'/metaOutput/internData.csv', index=False)
    return internData

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

    viData.rename(columns={'Company': 'startupName', 'Investors': 'investorName'}, inplace=True)
    viData = viData[VIColumns]
    # viData = viData.drop_duplicates('startupName')
    viData.startupName = viData.startupName.astype(str).apply(lambda x: x.upper())
    viData.investorName = viData.investorName.astype(str).apply(lambda x: x.upper())
    viData.startupName = viData.startupName.str.replace('(', '').str.replace(')', '')

    # viData['roundDate'] = pd.to_datetime(viData['roundDate'], format="%B-%Y")

    # Get the date in the same format as keyur Data

    viData.to_csv(path+'/metaOutput/viData.csv', index=False)
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
    #
    #
    founderFile = founderFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    founderData = pd.read_json(founderFile, lines=True)
    founderData.name = founderData.name.apply(lambda x: x.upper())


    founderData['F_or_I'] = 'F'
    invData['F_or_I'] = 'I'
    personData = founderData.append(invData)



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
    # educationData['college']=educationData['college'].apply(lambda x: x.upper())
    # educationData['degree']=educationData['degree'].apply(lambda x: x.upper())
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
    # personData[['name']+['F_or_I']+['file_id']].to_csv(path+'/metaOutput/personData.csv', index=False, encoding='utf-8')
    # expData.to_csv(path+'/metaOutput/expData.csv', index=False, encoding='utf-8')
    # educationData.to_csv(path+'/metaOutput/educationData.csv', index=False, encoding='UTF8')
    f = open(path+'/metaOutput/personData.json', "w")
    for index,row in personData.iterrows():
        row.to_json(f)
        f.write("\n")
        row.to_json(f)
    return personData

def treatCrunchbaseData(inpColumn,path):
    crunchbaseColumns = inpColumn['crunchbaseColumns'].dropna().tolist()
    crunchbaseFile = codecs.open(path + '/data/startupProfiles.json', "r", encoding='utf-8', errors='ignore').read()
    # ---------------------------------------------------------------------

    # Crunchbase file
    # 1. Replace newline, braces, etc
    # 2. Fix unicode
    # 3. Convert to pandas

    crunchbaseFile = crunchbaseFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    crunchbaseData = pd.read_json(crunchbaseFile, lines=True)
    crunchbaseData.rename(columns={'company': 'startupName',
                                   'headquarters': 'city',
                                   'founders': 'founderName'
                                   }, inplace=True)
    crunchbaseData = crunchbaseData[crunchbaseColumns]
    crunchbaseData.startupName = crunchbaseData.startupName.astype(str).apply(lambda x: x.upper())
    crunchbaseData.city = crunchbaseData.city.str.split(',').tolist()
    crunchbaseData.city = crunchbaseData.city.apply(lambda x: x[0])
    crunchbaseData.startupName = crunchbaseData.startupName.str.replace('PVT', '').replace('LTD.', '').replace(
        'PRIVATE', '').replace('LIMITED', '')
    crunchbaseData.startupName = crunchbaseData.startupName.str.strip()
    crunchbaseData = crunchbaseData.drop_duplicates(['startupName']).reset_index(drop=True)
    crunchbaseData = crunchbaseData[crunchbaseData['founderName'] != '[]'].reset_index(drop=True)
    for index in range(crunchbaseData.shape[0]):
        # print index,crunchbaseData.iloc[index].startupName,len(crunchbaseData.iloc[index].founders),crunchbaseData.iloc[index].founders
        val = [crunchbaseData.iloc[index]['founderName'][x].encode('ascii', 'ignore') for x in
               range(len(crunchbaseData.iloc[index].founderName))]
        crunchbaseData.founderName.iloc[index] = val
    crunchbaseData.founderName = crunchbaseData.founderName.astype(str).apply(lambda x: x.upper())

    crunchbaseData.to_csv(path+'/metaOutput/crunchbaseData.csv', index=False, encoding='UTF8')

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
    # internData.startupName = internData.startupName.astype(str).fillna('').apply(lambda x: x.upper())
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
    # keyurData.startupName = keyurData.startupName.astype(str).fillna('').apply(lambda x: x.upper())
    # keyurData.investorName = keyurData.investorName.astype(str).fillna('').apply(lambda x: x.upper())
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
    # crunchbaseData.startupName = crunchbaseData.startupName.astype(str).fillna('').apply(lambda x: x.upper())
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
    # viData.startupName = viData.startupName.astype(str).fillna('').apply(lambda x: x.upper())
    # viData.investorName = viData.investorName.astype(str).fillna('').apply(lambda x: x.upper())
    #----------------------------------------------------------------------

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
    #                            'round Investment amount (Rupees Crores)': 'investmentAmount',
    #                            'round date': 'dealDate'
    #                            }, inplace=True)
    # internData = internData[internColumns]
    # internData.startupName = internData.startupName.astype(str).fillna('').apply(lambda x: x.upper())
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
    # # keyurData.DOI = keyurData.DOI.astype(str).fillna('')
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
    # keyurData.startupName = keyurData.startupName.astype(str).fillna('').apply(lambda x: x.upper())
    # keyurData.startupName = keyurData.startupName.str.replace('PVT', '').replace('LTD.', '').replace('PRIVATE', '').replace('LIMITED', '')
    # keyurData.InvestorName = keyurData.InvestorName.astype(str).fillna('').apply(lambda x: x.upper())
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
    # crunchbaseData.startupName = crunchbaseData.startupName.astype(str).fillna('').apply(lambda x: x.upper())
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
    # crunchbaseData.founders = crunchbaseData.founders.astype(str).fillna('').apply(lambda x: x.upper())
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
    # viData.startupName = viData.startupName.astype(str).fillna('').apply(lambda x: x.upper())
    # viData.InvestorName = viData.InvestorName.astype(str).fillna('').apply(lambda x: x.upper())
    # viData.startupName = viData.startupName.str.replace('(', '').str.replace(')','')
    # # Convertthe date of investment
    #
    # #personFile
    # # 1. Replace newline, braces, etc
    # # 2. Fix unicode
    # # 3. Convert to pandas
    # invFile = invFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    # invData = pd.read_json(invFile, lines=True)
    # invData.name = invData.name.fillna('').apply(lambda x: x.upper())
    # # invData = invData.drop_duplicates('name')
    # founderFile = founderFile.replace('\n', '').replace('\r', '').replace('}{', '},{')
    # founderData = pd.read_json(founderFile, lines=True)
    # founderData.name = founderData.name.fillna('').apply(lambda x: x.upper())
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