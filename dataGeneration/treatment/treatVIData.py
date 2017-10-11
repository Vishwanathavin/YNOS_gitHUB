import pandas as pd
def treatVIData():

    inpColumn = pd.read_csv('../data/dataFromEachSource.csv')
    VIColumns = inpColumn['VIColumns'].dropna().tolist()
    viData = pd.read_csv('../data/ventureIntelligence.csv',na_filter=False)[VIColumns]


    viData.startupName = viData.startupName.astype(str).apply(lambda x: x.upper()).str.replace('(', '').str.replace(')', '')
    viData.investorName = viData.investorName.astype(str).apply(lambda x: x.upper())


    viData.to_csv('../metaOutput/viData.csv', index=False)
    return viData
treatVIData()