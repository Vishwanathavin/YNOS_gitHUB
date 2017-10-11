import pymongo
import pandas as pd
import json
import codecs
import numpy as np
import ast
def adjustStartup(db):

    startupData = pd.read_csv('./data/startupData.csv',na_filter=False)

    # Do not convert nan to empty string here

    # for column in startupData:
    #     print column, startupData.iloc[0][column],type(startupData.iloc[0][column])
    # use string split option

    # startupData['groupClassification'] = startupData['groupClassification'].str.replace('[',).str.replace(']','')
    # startupData['groupClassification'] = startupData['groupClassification'].str.split(',')
    print type(startupData.iloc[0]['groupClassification']),startupData.iloc[0]['groupClassification']

    # print [index for index,row in startupData.iterrows()]
    # print ([ast.literal_eval(startupData.loc[index,'groupClassification']) for index,row in startupData.iterrows()])
    # text =  startupData.iloc[0]['groupClassification'].replace('[','').replace(']','')\
    #     .split(',')
    # import re
    # mylist = re.split(',', text )
    # print mylist
    # startupData.groupClassification = startupData.groupClassification.map(lambda x: x.replace('[', '').replace(']','').split(','))
    # print type(startupData.iloc[0]['groupClassification']), startupData.iloc[0]['groupClassification']

    # use ast literal eval to convert string into lists
    # startupData['groupClassification'] = startupData['groupClassification'].apply(ast.literal_eval)
    # startupData['startupClassification'] = startupData['startupClassification'].apply(ast.literal_eval)
    # startupData['keyword'] = startupData['keyword'].apply(ast.literal_eval)
    # startupData['dealInvestmentAmount'] = startupData['dealInvestmentAmount'].apply(ast.literal_eval)
    # startupData['roundDate'] = startupData['roundDate'].apply(ast.literal_eval)
    # startupData['roundInvestmentAmount'] = startupData['roundInvestmentAmount'].apply(ast.literal_eval)
    # startupData['roundInvestorCount'] = startupData['roundInvestorCount'].apply(ast.literal_eval)
    # startupData['roundLeadInvestorType'] = startupData['roundLeadInvestorType'].apply(ast.literal_eval)
    # startupData['roundValuation'] = startupData['roundValuation'].apply(ast.literal_eval)
    # startupData['equityValuation			'] = startupData['equityValuation			'].apply(ast.literal_eval)
    # startupData['investorName'] = startupData['investorName'].apply(ast.literal_eval)
    # startupData['investorType'] = startupData['investorType'].apply(ast.literal_eval)
    # startupData['investmentStage'] = startupData['investmentStage'].apply(ast.literal_eval)
    # startupData['founderName'] = startupData['founderName'].apply(ast.literal_eval)
    # startupData['investorName'] = startupData['investorName'].apply(ast.literal_eval)
    # startupData['linkedinURL'] = startupData['linkedinURL'].apply(ast.literal_eval)


	# Make changes that is definite here. It should pass through this step before it goes to the database

		# Add the new column, whether startupValidated

    # print  all(isinstance(item, np.nan) for item in startupData['roundDate'])



	# startupData['']

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


def adjustPerson():
    # remove unicodes
    # Validators
    # Push to database
    print "DO nothing"

def main():
	adjustStartup(db=None)

    # try:
    #     conn = pymongo.MongoClient()
    #     print "Connected successfully!!!"
    # except pymongo.errors.ConnectionFailure, e:
    #     print "Could not connect to MongoDB: %s" % e
    #
    # db = conn.YNOS

    # takes input as a startupData and person Data with the investor Founder mapping
    # startupData = pd.read_csv('../dataGeneration/output/startupData.csv')
    # personData = pd.read_csv('../dataGeneration/output/personData.csv')




    # startupInfo = startupData.ix[:,col]

    # get the investment related details


    # get the person detail

    # get the academic details

    # get the experience detail







    # print personData.shape


    # split into the 5 collections

    # Validate

    # push into database

    # adjustStartup(db=None)
    # adjustPerson(db)
if __name__=="__main__":
    main()


