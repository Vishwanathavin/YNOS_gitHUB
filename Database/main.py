# Import packages
import pandas as pd
from datetime import datetime
import pymongo
import ast
import numpy as np
# Class

class classCollectionData:
    def __init__(self):
        self.startupInfo = { 'startupID': str,
                        'ICB_industry':str,
                        'ICB_sector':str,
                        'accelaratorResult':str,
                        'accelerator':str,
                        'accleratorDate':str,
                        'businessModel':str,
                        'description':str,
                        'foundedDate':str,
                        'groupClassification':list,
                        'incubator':str,
                        'incubatorDate':str,
                        'incubatorResult':str,
                        'keyword':list,
                        'source':str,
                        'startupClassification':list,
                        'startupName':str,
                        'startupStatus':str,
                        'state':str,
                        'founderName':list,
                        'website':str,
                        'city':str
                        }
        self.fundingInfo = {}
        self.personInfo = {}
        self.educationInfo = {}
        self.experienceInfo = {}


class classStartupData:

    # Dataframe
    def __init__(self, my_dataframe):
        self.DataFrame = my_dataframe

    # Modified Dataframe with cells not having valid type removed
    validatedData = pd.DataFrame()
    # def: split the strings into arrays ( List)
    # return same dataframe
    def convertStringsToLists(self,colList):
        # startupData.fillna('',inplace=True)
        for col in colList:
            self.DataFrame[col] = self.DataFrame[col].apply(ast.literal_eval)

    # This is not used at the moment since mongodb cannot store the datetime. Wea re usingit as string
    def convertStringsToDate(self,dateCol):
        for col in dateCol:
            print col, type(self.DataFrame.loc[0,col])
            self.DataFrame[col] = self.DataFrame[col].apply(lambda x: datetime.strptime(x,'%Y-%m-%d'))
            print col, type(self.DataFrame.loc[0,col])
    # def: replace nan into '[]'
    def treatEmptyCols(self, colList):

        for col in colList:
            self.DataFrame[col].fillna('[]',inplace=True)

    # Check of the column types on input dataframe is the same as we expected
    def validateCollection(self,dictionary):
        for key,val in dictionary.iteritems():
            self.validatedData[key]= self.DataFrame.loc[self.DataFrame[key].apply(type)==val,key]






# validate the datatype of each element of the column
def validateData():

    # Get the dict having details about the types of collection
    startupInfoDict =  collectionObject.startupInfo

    # Validate the data in each column
    startupObject.validateCollection(startupInfoDict)


    # # We can get more such collections tested by running a for loop on the collection list
    #
    # # Get the locations where data is rejected by our validator
    changedLocations = (np.where(startupObject.DataFrame[startupInfoDict.keys()] != startupObject.validatedData))

    reworkDataframe = pd.DataFrame(np.nan, index=startupObject.DataFrame[startupInfoDict.keys()].index, columns=startupObject.DataFrame[startupInfoDict.keys()].columns)
    reworkDataframe[['startupID','startupName']] = startupObject.DataFrame[['startupID','startupName']]
    for row in range(len(changedLocations[0])):
        reworkDataframe.ix[changedLocations[0][row], changedLocations[1][row]] = startupObject.DataFrame[startupInfoDict.keys()].ix[
            changedLocations[0][row], changedLocations[1][row]]

    reworkDataframe.fillna('').to_csv('rework.csv', index=False)
    #


# passed, failed = def Validate the data ( dict)


# Get the strings of startup data as arrays
def treatStartupData():
    # Get the dict having details about the types of collection
    startupInfoDict = collectionObject.startupInfo

    # Get the columns that have list as the type in the collection
    listCol = [key for key,val in startupInfoDict.iteritems() if val == list]

    # Convert the emptyLocations(nan) into empty array. Helpful in using ast.Literaleval
    startupObject.treatEmptyCols(listCol)

    # Convert the strings to list inside the class
    startupObject.convertStringsToLists(listCol)


    # Store dateime as string since mongodb cannot anyway  use it

    # # Get the columns that have list as the type in the collection
    # dateCol = [key for key, val in startupInfoDict.iteritems() if val == datetime]
    #
    # # Convert the strings to datetime inside the class
    # startupObject.convertStringsToDate(dateCol)


if __name__=='__main__':

    # Get the collection Info as a class: This has the data types of all the variables in the collections
    collectionObject = classCollectionData()



    # Read input file
    startupData = pd.read_csv('./data/startupData.csv')

    # Connect to DB to get the latest ID
    try:
        conn = pymongo.MongoClient()
        print "Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e

    YNOSdatabase = conn.YNOS

    # Check if id exists for our input file
    isUpDate = True if 'startupID' in startupData.columns else False

    # If yes: it is an update operation. Do nothing
    # if no # Generate IDS for them by incrementing the DatabaseiD
    if(not isUpDate):
        # Change this logic after connecting to DB
        startupData['startupID'] = ["S_" + str(index) for index, row in startupData.iterrows()]


    #Push dataframe into a class
    startupObject = classStartupData(startupData)


    # treat the data in the dataframe to get them into desired formats
    treatStartupData()

    #  Validate the formats
    validateData()


    # Add other validators in the mongoDB database

    # Check if the ID exists in the database ( Test using empty database and filled database
    # If yes update that particular field
    # If no, append to database




