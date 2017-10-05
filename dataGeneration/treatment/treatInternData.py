import pandas as pd
def treatInternData():
    inpColumn = pd.read_csv('../data/dataFromEachSource.csv')
    internColumns = inpColumn['internColumns'].dropna().tolist()

    internData = pd.read_csv('../data/interns.csv')[internColumns]
    nullstartUP = internData[internData['startupName'].isnull()]
    for index,rows in nullstartUP.iterrows():
        internData.loc[index, 'startupName'] = 'tempName_' + str(index)

    internData.startupName = internData.startupName.astype(str).apply(lambda x: x.upper()).str.strip().str.replace('LTD.', '').str.replace('PVT', '').str.replace('LTD', '').str.replace('PRIVATE', '').str.replace('LIMITED', '')

    # merge intern old and intern New
    internnew = pd.read_csv('../data/internNew.csv')[internColumns+['website']]
    internnew.startupName = internnew.startupName.astype(str).apply(lambda x: x.upper()).str.strip().str.replace('LTD.', '').str.replace('PVT', '').str.replace('LTD', '').str.replace('PRIVATE', '').str.replace('LIMITED', '')

    commondata1 = internData[internData.startupName.isin(internnew.startupName)]

    commondata2 = internnew[internnew.startupName.isin(internData.startupName)][['startupName','incubator','incubatorDate','website']]


    uncommondata1 = internData[~internData.startupName.isin(internnew.startupName)]

    uncommondata2 = internnew[~internnew.startupName.isin(internData.startupName)]



    commonData = pd.merge(commondata1.drop(['incubator','incubatorDate'],axis=1),commondata2,how="outer",on='startupName')

    internData = pd.concat([uncommondata1, uncommondata2,commonData], axis=0, ignore_index=True)




    dealCurryColumns = ['source',
                        'startupName',
                        'foundedDate',
                        'description',
                        'ICB_industry',
                        'ICB_sector',
                        'startupClassification',
                        'groupClassification1',
                        'groupClassification2',
                        'startupClassification2',
                        'groupClassification3',
                        'keyword1',
                        'keyword2',
                        'keyword3',
                        'city',
                        'state',
                        'startupStatus',
                        'founder1Name',
                        'founder2Name',
                        'founder3Name',
]
    dealCurryData = pd.read_csv('../data/dealCurry.csv')[dealCurryColumns]
    dealCurryData.startupName = dealCurryData.startupName.astype(str).apply(lambda x: x.upper()).str.strip().str.replace('LTD.', '').str.replace('PVT', '').str.replace('LTD', '').str.replace('PRIVATE', '').str.replace('LIMITED', '')
    dealCurryData = dealCurryData[~dealCurryData.startupName.isin(internData.startupName)]
#
    internData = pd.concat([internData, dealCurryData], axis=0, ignore_index=True)

    # Do all the merging of the columns. Convert into array whereever possible
    internData['round1Date'] = pd.to_datetime(internData['round1Date'])
    internData['round2Date'] = pd.to_datetime(internData['round2Date'])
    internData['round3Date'] = pd.to_datetime(internData['round3Date'])
    internData['foundedDate'] = pd.to_datetime(internData['foundedDate'])

    internData['startupClassification'] = [list(val) for val in(zip(internData['startupClassification'],internData['startupClassification2']))]
    internData['founderName'] = [list(val) for val in(zip(internData['founder1Name'],internData['founder1Name'],internData['founder3Name']))]
    internData['keyword'] = [list(val) for val in(zip(internData['keyword1'],internData['keyword2'],internData['keyword3']))]
    internData['groupClassification'] = [list(val) for val in (zip(internData['groupClassification1'],internData['groupClassification2'],internData['groupClassification3']))]
    internData['roundDate'] = [list(val) for val in(zip(internData['round1Date'],internData['round2Date'],internData['round3Date']))]
    internData['roundInvestorCount'] = [list(val) for val in(zip(internData['round1InvestorCount'],internData['round2InvestorCount'],internData['round3InvestorCount']))]
    internData['roundLeadInvestorType'] = [list(val) for val in(zip(internData['round1LeadInvestorType'],internData['round2LeadInvestorType'],internData['round3LeadInvestorType']))]
    internData['roundInvestmentAmount'] = [list(val) for val in(zip(internData['round1InvestmentAmount'],internData['round2InvestmentAmount'],internData['round3InvestmentAmount']))]
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
                    'round3Valuation',
                    'founder1Name',
                    'founder2Name',
                    'founder3Name']
    internData.drop( dropColumns,axis=1,inplace=True)


#
#
    internData.to_csv('../metaOutput/internData.csv', index=False)

treatInternData()