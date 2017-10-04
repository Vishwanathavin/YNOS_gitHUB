import pandas as pd
def treatCrunchbaseData():
    inpColumn = pd.read_csv('../data/dataFromEachSource.csv')
    crunchbaseColumns = inpColumn['crunchbaseColumns'].dropna().tolist()
    crunchbaseFile = open( '../data/startupProfiles.json', "r").read()
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
    crunchbaseData.startupName = crunchbaseData.startupName.str.replace('PVT', '').str.replace('LTD.', '').str.replace(
        'PRIVATE', '').str.replace('LIMITED', '')
    crunchbaseData.startupName = crunchbaseData.startupName.str.strip()
    crunchbaseData = crunchbaseData.drop_duplicates(['startupName']).reset_index(drop=True)
    crunchbaseData = crunchbaseData[crunchbaseData['founderName'] != '[]'].reset_index(drop=True)
    for index in range(crunchbaseData.shape[0]):
        # print index,crunchbaseData.iloc[index].startupName,len(crunchbaseData.iloc[index].founders),crunchbaseData.iloc[index].founders
        val = [crunchbaseData.iloc[index]['founderName'][x].encode('ascii', 'ignore') for x in
               range(len(crunchbaseData.iloc[index].founderName))]
        crunchbaseData.founderName.iloc[index] = val
    crunchbaseData.founderName = crunchbaseData.founderName.astype(str).apply(lambda x: x.upper())

    crunchbaseData.to_csv('../metaOutput/crunchbaseData.csv', index=False, encoding='UTF8')

    return crunchbaseData

treatCrunchbaseData()