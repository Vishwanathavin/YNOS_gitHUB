import pandas as pd

internData = pd.read_csv('../metaOutput/internData.csv')
viData = pd.read_csv('../metaOutput/viData.csv')

commonData = pd.merge(internData, viData, how='inner',on='startupName')

internData = pd.merge(internData,commonData[['startupName','investorName']],how='outer',on='startupName')

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
         'roundValuation': 'first',
         'incubator':'first',
         'incubatorDate':'first',
         'incubatorResult':'first',
         'accelerator':'first',
         'accleratorDate':'first',
         'accelaratorResult':'first',
         'founderName': 'first',
         'website': 'first'
         }).reset_index()
internData.to_csv('../metaOutput/internVImerge.csv',index=False)