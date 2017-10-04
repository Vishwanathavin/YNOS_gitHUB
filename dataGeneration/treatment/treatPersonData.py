import pandas as pd
from pprint import  pprint
def treatPersonData():
    founderFile = open('../data/founders_profiles_new.json').read()
    invFile = open('../data/Investor_final.json').read()

    invFile = invFile.replace('\n', '').replace('\r', '').replace('}{', '},{').replace('file_id','personID')
    invData = pd.read_json(invFile, lines=True)
    invData.name = invData.name.apply(lambda x: x.upper())
    #
    #
    founderFile = founderFile.replace('\n', '').replace('\r', '').replace('}{', '},{').replace('file_id','personID')
    founderData = pd.read_json(founderFile, lines=True)
    founderData.name = founderData.name.apply(lambda x: x.upper())


    founderData['personType'] = 'founder'
    invData['personType'] = 'investor'
    personData = founderData.append(invData)
    personData=personData.set_index("personID")
    # print personData['personID']

    personData.to_json('../metaOutput/personData.json',orient='index')

    # # Write to File
    # f = open('../metaOutput/personData.json', "w")
    # for index,row in personData.iterrows():
    #     row.to_json(f)
    #     f.write("\n")
    return personData
treatPersonData()