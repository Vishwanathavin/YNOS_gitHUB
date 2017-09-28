import os
from inspect import getsourcefile
import pandas as pd
import json
import ast

from mergingRoutines import internVIMerge, internKeyurMerge, startupCrunchbaseMerge, \
    getFounderNames, getInvestorNames
from treatment import treatment


def getStartupData(crunchbaseData, internData, keyurData,viData):
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))

    # path = path.replace("\\","/")
    # # Assign the columns to pick from each of the data sources
    # inpColumn = pd.read_csv(path + '/data/dataFromEachSource.csv')

    startupData = internVIMerge(internData, viData)

    startupData = internKeyurMerge(startupData, keyurData)

    # Common Companies between Keyur-Intern

    startupData = startupCrunchbaseMerge(startupData, crunchbaseData)

    return startupData

def getPersonData(startupData,personData):

    for index,row in startupData.iterrows():

        if (startupData.iloc[index]['founderName']!=[]):
            startupData.iloc[index]['founderName'] = ast.literal_eval(startupData.iloc[index]['founderName'])

        # if (startupData.iloc[index]['investorName']!=['']):
        #     startupData.iloc[index]['investorName'] = ast.literal_eval(startupData.iloc[index]['investorName'])

    personList=[]
    [personList.append(x) for names in startupData["founderName"] for x in names   ]
    [personList.append(x) for names in startupData["investorName"] for x in names   ]


    personData = personData[personData["name"].isin(personList)]

    # print [x.isin(personData["name"]) for names in startupData["founderName"] for x in names  ]
    # founderNamesInDataset = getFounderNames(startupData)
    # investorNamesInDataset,startupData = getInvestorNames(startupData)
    #
    # #Purge person Data to the ones that matter
    # personData=personData[personData.name.isin(founderNamesInDataset.name) | personData.name.isin(investorNamesInDataset.name) ].reset_index(drop=True)


    return personData

    # for index,rows in eduData.iterrows():
    #     # line = lines.split(',')
    #     # if (rows['Name'] == '') or (rows['duration'] == '') or (rows['degree'] == ''):
    #     #     continue
    #
    #     if last == '':
    #         last = rows[1]
    #         rows[2] = rows[2].split('-')[1].strip(' ')
    #         educations[rows[4].strip('\n').lower()] = int(rows[2])
    #     elif last == rows[1]:
    #         if not ('' in rows):
    #             rows[2] = rows[2].strip(' ').split('-')
    #             if len(rows[2]) == 2:
    #                 rows[2] = rows[2][1].strip(' ')
    #             else:
    #                 rows[2] = rows[2][0].split(' ')
    #                 if len(rows[2]) == 2:
    #                     rows[2] = rows[2][1]
    #                 else:
    #                     rows[2] = rows[2][0]
    #             educations[rows[4].strip('\n').lower()] = int(rows[2])
    #     else:
    #         rand = 1
    #         while rand:
    #             if len(educations) == 0:
    #                 break
    #             v = list(educations.values())
    #             k = list(educations.keys())
    #             degree = k[v.index(min(v))].lower()
    #             year = educations[degree]
    #             age = 2017 - year + 21
    #             # print('degree: %s; Age: %d'%(degree,age))
    #             if (degree.find('class 12')) != -1 or (degree.find('secondary') != -1):
    #                 print(last)
    #                 educations.pop(degree, None)
    #             else:
    #                 out.write('%s,%d\n' % (last, age))
    #                 rand = 0
    #
    #         last = rows[1]
    #         educations = {}
    #         rows[2] = rows[2].strip(' ').split('-')
    #         if len(rows[2]) == 2:
    #             rows[2] = rows[2][1].strip(' ')
    #         else:
    #             rows[2] = rows[2][0].split(' ')
    #             if len(rows[2]) == 2:
    #                 rows[2] = rows[2][1]
    #             else:
    #                 rows[2] = rows[2][0]
    #         educations[rows[4].strip('\n').lower()] = int(rows[2])
    #
    # out.close()
    # ageFile =pd.read_csv('./metaOutput/age.csv')
    # return ageFile


def dataConsolidate():
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    if (os.path.exists(path+'/metaOutput/internData.csv')):
        # expData = pd.read_csv('./metaOutput/expData.csv')
        viData = pd.read_csv(path+'/metaOutput/viData.csv')
        crunchbaseData = pd.read_csv(path+'/metaOutput/crunchbaseData.csv')
        internData = pd.read_csv(path+'/metaOutput/internData.csv')
        # internDataFunded = pd.read_csv(path+'/metaOutput/internData.csv')
        # internDataNonFunded = pd.read_csv('./metaOutput/internDataNonFunded.csv')
        keyurData = pd.read_csv(path+'/metaOutput/keyurData.csv')

        personData = pd.read_json(open(path + '/metaOutput/personData.json').read().replace('\n', '').replace('\r', '').replace('}{', '},{'), lines=True)

    else:
        keyurData,internData, viData,crunchbaseData,personData  = treatment()

    startupData = getStartupData(crunchbaseData, internData, keyurData,viData)
    startupData.to_csv(path + '/output/startupData.csv', index=False)
    personData = getPersonData(startupData[['investorName']+['founderName']],personData)

    personData.to_csv(path+'/output/personData.csv', index=False)

    return startupData



if __name__=='__main__':
    dataConsolidate()







#
# def startupDataConsolidation():
#     debug = True
#
#     # Start year of Keyur data
#     year = 2014
#
#     # Read the column list to be taken from each source
#
#     inpColumn = pd.read_csv('./data/dataFromEachSource.csv')
#
#     internColumns = inpColumn['internColumns'].dropna().tolist()
#     keyurColumns = inpColumn['keyurColumns'].dropna().tolist()
#     crunchbaseColumns = inpColumn['crunchbaseColumns'].dropna().tolist()
#     VIColumns = inpColumn['VIColumns'].dropna().tolist()
#
#
#
#     #Read InternData
#     internData = pd.read_csv('./Data/InternData.csv')[internColumns]
#     internData.Start_up_name = internData.Start_up_name.astype(str)
#     internData.Start_up_name = internData.Start_up_name.fillna('').apply(lambda x: x.upper())
#     if(debug): internDataShape = internData.shape
#
#     # Get Keyur Data
#     keyurData = pd.read_csv('./Data/KeyurData.csv')[keyurColumns]
#     keyurData.Start_up_name = keyurData.Start_up_name.astype(str)
#     keyurData.Start_up_name = keyurData.Start_up_name.fillna('').apply(lambda x: x.upper())
#
#     #Filter out the year in keyur data
#     keyurData = keyurData[keyurData["DOI"] >= year]
#
#     if (debug): keyurDataShape = keyurData.shape
#     # Data Merging:
#     # 1. Merge the common data
#     # 2. Concatenate the uncommon data
#
#     commonData = keyurData[keyurData.Start_up_name.isin(internData.Start_up_name)]
#     startupData = internData.merge(
#         commonData[['Start_up_name'] + ['Investor_Name'] + ['DOI'] + ['Deal_Investment_Amount_INR_M']],
#         on='Start_up_name',
#         how='outer')
#     if (debug): keyurInternCommon = commonData.shape
#     uncommonData = keyurData[~keyurData.Start_up_name.isin(internData.Start_up_name)]
#     startupData = pd.concat([startupData, uncommonData[keyurColumns]], axis=0, ignore_index=True)
#     if (debug): keyurInternMerge = startupData.shape
#
#     # get Crunchbase data
#     # crunchbaseData = pd.read_json(fix_unicode('[' + open('./Data/Startup_profiles.json').read().replace('\n', '').replace('\r', '').replace('}{','},{') + ']'))
#     crunchbaseData = pd.read_json(fix_unicode(open('./Data/Startup_profiles.json').read().replace('\n', '').replace('\r', '').replace('}{','},{')),lines=True)
#
#     # inpFile = inpFile.replace('\n', '').replace('\r', '').replace('}{','},{')
#
#     # print inpFile
#     # inpFile = '['+inpFile+']'
#     # deal_data = pd.read_json(inpFile)
#     # print deal_data.shape
#
#     crunchbaseData = crunchbaseData[crunchbaseColumns]
#     crunchbaseData.rename(columns={'company': 'Start_up_name'}, inplace=True)
#     crunchbaseData.Start_up_name = crunchbaseData.Start_up_name.astype(str)
#     crunchbaseData.Start_up_name = crunchbaseData.Start_up_name.fillna('').apply(lambda x: x.upper())
#     if (debug): crunchbaseDataShape = crunchbaseData.shape
#
#     # Data Mergin
#     #1. Merge common data
#     commonData = crunchbaseData[crunchbaseData.Start_up_name.isin(startupData.Start_up_name)]
#     if (debug): Crunchabase_keyurInternCommon = commonData.shape
#
#     startupData = startupData.merge(commonData, on='Start_up_name', how='outer')
#     if (debug): Crunchabase_keyurInternMerge = startupData.shape
#
#     # Write out a file to gather the list of startupNames
#     infoNeeded=startupData[~startupData.Start_up_name.isin(crunchbaseData.Start_up_name)].Start_up_name
#     infoNeeded.to_csv('./Data/StartupInfoNeeded.csv')
#
#     if (debug): crunchbaseTOScrape = infoNeeded.shape
#
#     startupData.Investor_Name = startupData.Investor_Name.astype(str)
#     startupData.Investor_Name = startupData.Investor_Name.fillna('NaN').apply(lambda x: x.upper())
#     startupData['ID'] = range(1, startupData.shape[0] + 1)
#     startupData.to_csv('./Data/startupData.csv')
#     # # Get VI data
#     # VIData = pd.read_csv('./Data/temp_debug/VentureIntelligenceData.csv')[VIColumns]
#     # VIData.rename(columns={'Company': 'Start_up_name'}, inplace=True)
#     # VIData.Start_up_name = VIData.Start_up_name.astype(str)
#     # VIData.Start_up_name = VIData.Start_up_name.fillna('').apply(lambda x: x.upper())
#     # if (debug): VIDataShape = VIData.shape
#     #
#     #
#     #
#     # commonData = VIData[VIData.Start_up_name.isin(startupData.Start_up_name)]
#     # startupData['union'] = startupData.apply(lambda x: (x['col1'] | x['col2']), axis=1)
#     # # print zip(startupData.Investor_Name, commonData.Investor_Name)
#     # # print startupData.Investor_Name
#     # # startupData.Investor_Name = startupData.apply(lambda x: startupData['Investor_Name'].union(commonData['Investor_Name']),
#     # #                                               axis=1)
#     # # startupData.Investor_Name = ([set1.union(set2) for set1, set2 in zip(commonData.Investor_Name, startupData.Investor_Name)])
#     # # startupData.Investor_Name = startupData.Investor_Name.union(commonData.Investor_Name)
#     # # if (debug): VI_keyurInternCommon = commonData.shape
#     # if (debug): commondataName = commonData.Start_up_name
#     #
#     # # pd.merge(startupData,commonData,on='Start_up_name',how='outer')
#     # # if (debug): VI_keyurInternMerge = startupData.shape
#     #
#     # startupData.to_csv('./Data/startupData2.csv')
#
#     # startupData = pd.read_csv('./Data/startupData.csv')
#     #
#     # print startupData.columns
#
#     startupData.Investor_Name = startupData.Investor_Name.astype(str)
#     startupData.Investor_Name = startupData.Investor_Name.fillna('NaN').apply(lambda x: x.upper())
#
#
#     #
#     #Get person Details
#     investorData = pd.read_json(fix_unicode(open('./Data/Investor_profiles.json').read().replace('\n', '').replace('\r', '').replace('}{',
#                                                                                                       '},{')),lines=True)
#     # json.loads('\u0096')
#     # investorData= fix_unicode(investorData)
#     investorData.rename(columns={'name': 'Investor_Name'}, inplace=True)
#
#     investorData.Investor_Name = investorData.Investor_Name.astype(str)
#     investorData.Investor_Name = investorData.Investor_Name.fillna('NaN').apply(lambda x: x.upper())
#
#     commonData = investorData[investorData.Investor_Name.isin(startupData.Investor_Name)]
#     if (debug): StartupLinkedinCommonData = commonData.shape
#
#
#
#     if(debug):
#         print '---------------------Report-----------------'
#         print 'Intern Data size: ',internDataShape[0]
#         print 'Keyur Data size: ',keyurDataShape[0]
#         print 'Common companies between intern and keyur Data size: ',keyurInternCommon[0]
#         print 'Intern and keyur Data Merged size: ',keyurInternMerge[0]
#         print 'CrunchBase size: ',crunchbaseDataShape[0]
#         print 'Common companies between crunchbase and keyur-Intern data: ',Crunchabase_keyurInternCommon[0]
#         print 'Merged data crunchbase and keyur-Intern size: ',Crunchabase_keyurInternMerge[0]
#         print 'Companies to scrape from crunch base: ',crunchbaseTOScrape[0]
#         # print 'VI Data Size: ',VIDataShape[0]
#         # print 'Common companies between VI and keyur-Intern data: ',VI_keyurInternCommon[0]
#         # print 'Names of the common companies: ',commondataName
#         # print 'Merged data VI and keyur-Intern size: ', VI_keyurInternMerge[0]
#         print 'Startup Investors Common data: ', StartupLinkedinCommonData[0]
#
#

#     print 'Experience Duration: '
#     # temp = experienceData.Duration.dropna()
#     # temp.to_csv('UniqueEx.csv')
#
#     educationData = create_education_table(commonData)
#     educationData['ID'] = range(1, educationData.shape[0] + 1)
#     print 'Education Duration: '
#     educationData.Duration.dropna().to_csv('uniqueEdu.csv')
#
#     personData = create_person_table(commonData)
#     personData['ID'] = range(1, personData.shape[0] + 1)
#     return startupData,experienceData,educationData,personData
#
#
#
  # # Merge Intern and Keyur Data
    # commonData = keyurData[keyurData.startupName.isin(internData.startupName)]
    #
    # commonData=commonData[['startupName'] + ['investorName'] + ['DOI'] + ['Deal_Investment_Amount_INR_M']]
    # startupData = internData.merge(
    #         commonData,
    #         on='startupName',
    #         how='outer')
    #
    #
    #
    # # # Get a list of companies that needs to be fetched
    # uncommonData = keyurData[~keyurData.startupName.isin(internData.startupName)]
    # # # Get a list of companies that needs to be fetched
    # uncommonData.to_csv('./output/keyurDataInfoNeeded.csv')
    #
    #
    # startupData = pd.concat([startupData, uncommonData], axis=0, ignore_index=True)
    #
    #
    # # Adding crunchbase details
    # commonData = crunchbaseData[crunchbaseData.startupName.isin(startupData.startupName)]
    # startupData = startupData.merge(commonData, on='startupName', how='outer')
    #
    # uncommonData= crunchbaseData[~crunchbaseData.startupName.isin(startupData.startupName)]
    # uncommonData.to_csv('./output/crunchbaseDataInfoNeeded.csv')
    #
    # # Adding VI details
    # commonData = viData[viData.startupName.isin(startupData.startupName)]
    # startupData = startupData.merge(commonData, on='startupName', how='outer')
    #
    # Investor Details

    # Get the founder names and investor names as separate
    # items from the start-upData

    #Get a list of Names that are present.
        # Get the experience, education and personal data of investor and founder separately

    # Get a list of names that are not present
        # Write them to a file along with the name of the company
    # experienceData = create_experience_table(commonData)
    # experienceData['ID'] = range(1,experienceData.shape[0]+1)
    #
    # educationData = create_education_table(commonData)
    # educationData['ID'] = range(1, educationData.shape[0] + 1)
    # personData = create_person_table(commonData)
    # personData['ID'] = range(1, personData.shape[0] + 1)

#
# def create_experience_table(person_data):
#
#     seriesList = []
#     for row in range(person_data.shape[0]):
#         for exp in range(len(person_data.iloc[row]["experience"])):
#             exp_Series = pd.Series([person_data.iloc[row]['Investor_Name'],person_data.iloc[row]["experience"][exp]['position'],person_data.iloc[row]["experience"][exp]['company'],person_data.iloc[row]["experience"][exp]['duration']],index=['Name','Position','Company','Duration'])
#             seriesList.append((exp_Series))
#     experience_table = pd.DataFrame(seriesList)
#
#     return experience_table
#
# def create_education_table(person_data):
#
#     seriesList = []
#     for row in range(person_data.shape[0]):
#         for exp in range(len(person_data.iloc[row]["schools"])):
#             exp_Series = pd.Series([person_data.iloc[row]['Investor_Name'],person_data.iloc[row]["schools"][exp]['duration'],person_data.iloc[row]["schools"][exp]['college'],person_data.iloc[row]["schools"][exp]['degree'],person_data.iloc[row]["schools"][exp]['field']],index=['Name','Duration','College','Degree','Field'])
#             seriesList.append((exp_Series))
#
#     education_table = pd.DataFrame(seriesList)
#     return education_table
#
#
# def create_person_table(person_data):
#
#     seriesList = []
#     for row in range(person_data.shape[0]):
#         person_Series = pd.Series([person_data.iloc[row]['Investor_Name'],
#                                 person_data.iloc[row]['location'],
#                                 person_data.iloc[row]["job"]],
#                                index=['Investor_Name', 'location', 'job'])
#         seriesList.append(person_Series)
#
#     person_table = pd.DataFrame(seriesList)
#     return person_table
#
#
#
#

