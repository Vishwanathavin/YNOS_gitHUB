import pymongo
import pandas as pd
import json
import codecs
import ast

def adjustStartup(db):
    print 'hi'
    # sampleData = pd.read_csv(codecs.open('./data/sampleData.csv', "r", encoding='utf-8',errors='ignore'))
    #
    # sampleData['roundInvestmentAmountINR'] =sampleData['roundInvestmentAmountINR'].apply(ast.literal_eval)
    # sampleData['investorID'] =sampleData['investorID'].apply(ast.literal_eval)
    # sampleData['founderID'] =sampleData['founderID'].apply(ast.literal_eval)
    # sampleData['startupClassification'] =sampleData['startupClassification'].apply(ast.literal_eval)
    # # sampleData['dealDate'] =sampleData['dealDate'].apply(ast.literal_eval)
    # sampleData['groupClassification'] =sampleData['groupClassification'].apply(ast.literal_eval)
    #
    # for index,row in sampleData.iterrows():
    #     for column in sampleData:
    #         # print type(sampleData.iloc[0][column]),sampleData.iloc[0][column]
    #
    #         if isinstance(sampleData.iloc[0][column], list):
    #             for x in range(len(sampleData.iloc[0][column])):
    #                 print column,': ',x,': ',sampleData.iloc[0][column][x], type(sampleData.iloc[0][column][x])
    #         else:
    #             print column,': ',(sampleData.iloc[0][column]), type(sampleData.iloc[0][column])

    # get the city in the right format

    # Do the checks for format locally
    # Push
    # print "Do nothing"
def adjustPerson():
    # remove unicodes
    # Validators
    # Push to database
    print "DO nothing"

def main():
    # try:
    #     conn = pymongo.MongoClient()
    #     print "Connected successfully!!!"
    # except pymongo.errors.ConnectionFailure, e:
    #     print "Could not connect to MongoDB: %s" % e
    #
    # db = conn.YNOS

    # takes input as a startupData and person Data with the investor Founder mapping
    startupData = pd.read_csv('../dataGeneration/output/startupData.csv')
    personData = pd.read_csv('../dataGeneration/output/personData.csv')

    col = ['description',
	'ICB_industry',
	'ICB_sector',
	'accelaratorResult',
	'accelerator',
	'accleratorDate',
	'businessModel',
	'city',
	'companyWebsite	',
	'investmentDetails : True or False',
	'foundedDate',
	'groupClassification',
	'incubatorincubatorDate',
	'incubatorResult',
	'keyword',
	'source',
	'stageClassification',
	'startupClassification',
	'startupName',
	'startupID',
	'startupStatus',
	'state',
	'founderID ',
	'website',
	'Lat',
	'Lon',
	'validated : True or False ']
    startupInfo = startupData.ix[:,col]
    # startupInfo['investmentDetails'] = startupData['roundDate'].isnull()
    print startupData['roundDate']
    print startupInfo['investmentDetails']
    # print personData.shape


    # split into the three collections

    # Validate

    # push into database

    # adjustStartup(db=None)
    # adjustPerson(db)
if __name__=="__main__":
    main()


