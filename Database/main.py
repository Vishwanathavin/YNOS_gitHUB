# Import packages
import pandas as pd
import pymongo
from startupClass import classCollectionData,classStartupData
import numpy as np
from math import isnan
from pprint import pprint
from datetime import datetime
# validate the datatype of each element of the column
def validateData():

    # Get the dict having details about the types of collection
    colDict =  collectionObject.getColumns()
    # Validate the data in each column
    startupObject.validateCollection(colDict)

    #  Move all this to after database writing
    # # Get the locations where data is rejected by our validator
    changedLocations = (np.where(startupObject.treatedData[list(colDict)] != startupObject.validData))


    startupObject.DataFrame["errorKeys"] = [[] for _ in range(len(startupObject.DataFrame))]

    for index in range(len(changedLocations[0])):
        startupObject.DataFrame.loc[changedLocations[0][index], "errorKeys"].append( startupObject.DataFrame[list(colDict)].columns[changedLocations[1][index]])

    startupObject.DataFrame.fillna('').to_csv('rework.csv', index=False)

# passed, failed = def Validate the data ( dict)


# Get the strings of startup data as arrays
def treatStartupData():
    # Get the dict having details about the types of collection
    colDict = collectionObject.getColumns()


    # Get the columns that have list as the type in the collection
    # Python 2: listCol = [key for key,val in colDict.iteritems() if val == list]
    listCol = [key for key,val in colDict.items() if val["type"] == list]

    # put a '[]' in an empty column
    startupObject.treatEmptyCols(listCol)

    # Convert the strings to list inside the class
    startupObject.convertStringsToLists(listCol)

    # # Get the columns that have list as the type in the collection
    dateCol = [key for key, val in colDict.items() if val["type"] == datetime]

    # # Convert the strings to datetime inside the class
    startupObject.convertStringsToTimeStamp(dateCol)

    # Assign unicode columns
    unicodeCol = ['description','startupName']
    # Remove unicodes in the description
    # Commenting this since we are already encoding during the file reading
    # startupObject.removeUnicodes(unicodeCol)


    # Convert lat lon in geopolitical format
    # Convert other float, int double types if needed


if __name__=='__main__':

    collectionObject = classCollectionData()


    # Read input file
    # For python 3 use, encoding = 'ISO-8859-1'
    startupData = pd.read_csv('./data/startupData.csv',encoding='ISO-8859-1')


    #Push dataframe into a class
    startupObject = classStartupData(startupData)


    # treat the data in the dataframe to get them into desired formats
    treatStartupData()

    #  Validate the formats
    validateData()

    # Connect to DB to get the latest ID
    try:
        conn = pymongo.MongoClient()
        print ("Connected successfully!!!")
    except pymongo.errors.ConnectionFailure as e:
        print ("Could not connect to MongoDB: %s" % e)

    YNOSdatabase = conn.YNOS

    # # Push into database first without validation. Later on with validation
    for index,row in startupObject.validData.iterrows():
    #     # record = json.loads(row.T.to_json(orient='records')).values()
        record = row.to_dict()

        # We need to add this here so that Location is not set for cases which has "Lat, Lon as null
        if not isnan(record["Lat"]) and not isnan(record["Lon"]):
            # record['Location'] ={"type": "Point", "coordinates": [record["Lat"], record["Lon"]]}
            record['Location'] = [record["Lat"], record["Lon"]]
        # Use exception handlers. If passes update database if failed :
        #startupObject.DataFrame.fillna('').to_csv('rework.csv', index=False)
        del record['Lon']
        del record['Lat']
        YNOSdatabase.startupInfo.update({"_id": record["startupID"]}, {'$set': record},upsert=True)

    exit()
    # Assign Geo JSON Type
    YNOSdatabase.startupInfo.create_index([("Location", pymongo.GEO2D)])
    query = {"Location": {"$near": [19.0, 72.0]}}
    # query = {"$and" : [{ "Location": {"$near": [19.0, 72.0 ]}},{"Location": {"$exists": True}}]}
    cursor = YNOSdatabase.startupInfo.find(query)
    for val in cursor:
        print(val['startupID'])
    # # FindResults =  YNOSdatabase.starupInfo.find({"foundedDate": {"$exists": True}})
    # FindResults =  YNOSdatabase.starupInfo.find({ "$type": "double" })

        # YNOSdatabase.startupInfo.find({'foundedDate': { "$type": "double"}} ).forEach(function(x){x["foundedDate"] = new timstamp(x.bad)})
        # db.foo.save(x)});
    # How do we change the double to timestamp
    # https://stackoverflow.com/questions/4973095/mongodb-how-to-change-the-type-of-a-field

        # Add other validators in the mongoDB database




