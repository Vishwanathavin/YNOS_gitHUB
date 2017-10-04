import pandas as pd
import ast
startupData = pd.read_csv('../output/startupData.csv')
personFile = open('../metaOutput/personData.json').read()

personFile = personFile.replace('\n', '').replace('\r', '').replace('}{', '},{').replace('file_id', 'personID')
personData = pd.read_json(personFile, lines=True)

for index, row in startupData.iterrows():

    if (startupData.iloc[index]['founderName'] != []):
        startupData.iloc[index]['founderName'] = ast.literal_eval(startupData.iloc[index]['founderName'])

        # if (startupData.iloc[index]['investorName']!=['']):
        #     startupData.iloc[index]['investorName'] = ast.literal_eval(startupData.iloc[index]['investorName'])

personList = []
[personList.append(x) for names in startupData["founderName"] for x in names]
[personList.append(x) for names in startupData["investorName"] for x in names]

personData = personData[personData["name"].isin(personList)]

seriesList = []
for index, row in personData.iterrows():
    for schoolIndex in range(len(row["schools"])):
        schseries = pd.Series(
            [row["name"], row["schools"][schoolIndex]["duration"],
             row["schools"][schoolIndex]["college"],
             row["schools"][schoolIndex]["degree"], row["personType"], index],
            index=['name', 'duration', 'college', 'degree', 'personType', 'personID'])
        seriesList.append(schseries)
educationData = pd.DataFrame(seriesList)
educationData['college'] = educationData['college'].apply(lambda x: x.upper())
educationData['degree'] = educationData['degree'].apply(lambda x: x.upper())
seriesList = []

for index, row in personData.iterrows():
    for expIndex in range(len(row["experience"])):
        expseries = pd.Series(
            [row["name"], row["experience"][expIndex]["position"],
             row["experience"][expIndex]["company"],
             row["experience"][expIndex]["duration"], row["personType"], index],
            index=['name', 'position', 'company', 'duration', 'personType', 'personID'])
        seriesList.append(expseries)
expData = pd.DataFrame(seriesList)
#
educationData.to_json('../output/educationData.json', orient='index')
expData.to_json('../output/experienceData.json', orient='index')
personData.to_json('../output/experienceData.json', orient='index')