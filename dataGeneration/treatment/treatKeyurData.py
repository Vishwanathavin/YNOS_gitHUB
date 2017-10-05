import pandas as pd
def treatKeyurData():
    inpColumn = pd.read_csv('../data/dataFromEachSource.csv')
    keyurColumns = inpColumn['keyurColumns'].dropna().tolist()  # Since other columns have more elements, we need to drop the Not a number elements
    keyurData = pd.read_csv('../data/keyur.csv')[keyurColumns]

    keyurData.startupName = keyurData.startupName.str.strip().astype(str).apply(lambda x: x.upper()).str.replace('PVT.', '').str.replace('LTD.', '').str.replace('PRIVATE','').str.replace('LIMITED', '').str.strip()
    keyurData.investorName = keyurData.investorName.astype(str).apply(lambda x: x.upper())

    # keyurData['roundDate'] = pd.to_datetime(keyurData['roundDate'], format="%m/%d/%Y")
    keyurData['roundDate'] = pd.to_datetime(keyurData['roundDate'])

    keyurData = keyurData[(keyurData['roundDate'] > '2014-01-01')]

    keyurData = keyurData.groupby(["startupName"]).agg(
        {
            'foundedDate': 'first',
            'investorName': lambda x: list(x),
            'linkedinURL': lambda x: list(x),
            'roundInvestmentAmount': lambda x: list(x),
            'investorType': lambda x: list(x),
            'dealInvestmentAmount': lambda x: list(x),
            'investmentStage': lambda x: list(x),
            'stageClassification': lambda x: list(x),
            'equityValuation': lambda x: list(x),
            'roundDate': lambda x: list(x),
            'companyWebsite': 'first',
            'source': 'first'
         }).reset_index()

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



    keyurColumns = ['startupName',
                    'description',
                    'ICB_industry',
                    'ICB_sector',
                    'startupClassification',
                    'groupClassification1',
                    'startupClassification2',
                    'groupClassification3',
                    'groupClassification2',
                    'keyword1',
                    'keyword2',
                    'keyword3',
                    'city',
                    'state',
                    'startupStatus',
                    'founder1Name',
                    'founder2Name',
                    'founder3Name'
    ]
    keyurDataAdditional = pd.read_csv('../data/keyurAdditionalDetailsAddedByInterns.csv')[keyurColumns]
    keyurDataAdditional.startupName = keyurDataAdditional.startupName.str.strip().astype(str).apply(lambda x: x.upper()).str.replace('PVT.','').str.replace('LTD.', '').str.replace('PRIVATE', '').str.replace('LIMITED', '').str.strip()



    keyurDataAdditional['startupClassification'] = [list(val) for val in (
    zip(keyurDataAdditional['startupClassification'], keyurDataAdditional['startupClassification2']))]
    keyurDataAdditional['keyword'] = [list(val) for val in
                             (zip(keyurDataAdditional['keyword1'], keyurDataAdditional['keyword2'], keyurDataAdditional['keyword3']))]
    keyurDataAdditional['groupClassification'] = [list(val) for val in (
    zip(keyurDataAdditional['groupClassification1'], keyurDataAdditional['groupClassification2'], keyurDataAdditional['groupClassification3']))]
    keyurDataAdditional['founderName'] = [list(val) for val in (
    zip(keyurDataAdditional['founder1Name'], keyurDataAdditional['founder2Name'], keyurDataAdditional['founder3Name']))]

    dropColumns = ['startupClassification2',
                   'keyword1',
                   'keyword2',
                   'keyword3',
                   'groupClassification1',
                   'groupClassification2',
                   'groupClassification3',
                   'founder1Name',
                   'founder2Name',
                   'founder3Name'
                ]
    keyurDataAdditional.drop(dropColumns, axis=1, inplace=True)

    keyurData = pd.merge(keyurData, keyurDataAdditional, how='outer', on='startupName')

    keyurData.to_csv('../metaOutput/keyurData.csv', index=False)

treatKeyurData()
    # keyurData.rename(columns={'Source' 	:	'source',
    #         'Company Name' 	:	'startupName',
    #         'ICB Industry' 	:	'ICB_industry',
    #         'ICB Sector' 	:	'ICB_sector',
    #         'Start up Classification' 	:	'startupClassification',
    #         'DOI' 	:	'foundedDate',
    #         'Investor Name' 	:	'investorName',
    #         'links' 	:	'linkedinURL',
    #         'Investor Type 1 (Angel / Institutional Investor/ Boutique / Corporate / Network)' 	:	'investorType',
    #         'Deal Investment Amount ( INR M)' 	:	'dealInvestmentAmount',
    #         'Round Investment Amount (INR M)' 	:	'roundInvestmentAmount',
    #         'Stage of Investment ( Seed / Early)' 	:	'investmentStage',
    #         'New Stage Classification' 	:	'stageClassification',
    #         'Announcement Date' 	:	'roundDate',
    #         'Equity Valuation (INR M)' 	:	'equityValuation',
    #         'City' 	:	'city',
    #         'State' 	:	'state',
    #         'Website' 	:	'companyWebsite'
    #                           }, inplace=True)