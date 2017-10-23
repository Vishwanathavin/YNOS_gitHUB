# Import packages
import pandas as pd  # Handling the data as a dataframe
import pymongo       # mongodb API

# has the details about the columns to be used.
# # Subsequent releases need us to change these values
from startupClass import classCollectionData,classStartupData

import numpy as np
from math import isnan
from datetime import datetime

# validate the datatype of each element of the column
def validateData():

    # Get the dict having details about the types of collection
    colDict =  collectionObject.getColumns()

    # Validate the data in each column
    startupObject.validateCollection(colDict)

    # # Get the locations where data is rejected by our validator routine
    # This variable is a tuple of size two with each element being a list having
    # rows and columns of thecorresponsing changed columns
    changedLocations = (np.where(startupObject.treatedData[list(colDict)] != startupObject.validData))

    # Initialize a column. We will write out a dataframe that will have original input
    # values intact and another column whihc bears all the changed values
    startupObject.DataFrame["errorKeys"] = [[] for _ in range(len(startupObject.DataFrame))]

    # Scan through the changed locations and get the column names for each row that has changed
    # Assign them to the new column and write it out
    for index in range(len(changedLocations[0])):
        startupObject.DataFrame.loc[changedLocations[0][index], "errorKeys"].append( startupObject.DataFrame[list(colDict)].columns[changedLocations[1][index]])

    # Write out a file that has all the info for erroneous data
    #
    startupObject.DataFrame.fillna('').to_csv('rework.csv', index=False)

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

def main():



    # treat the data in the dataframe to get them into desired formats
    print("Treating the data...")
    print()
    treatStartupData()

    #  Validate the formats at application level
    print("Validating the data...")
    print()
    validateData()

    # Connect to DB. Work on the exception handlers. They dont seem to work
    print("Connecting to database...")
    print()
    try:
        conn = pymongo.MongoClient()
        print("Connected successfully!!!")
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s" % e)

    YNOSdatabase = conn.YNOS

    print("Inserting the data into the Database...")
    print()
    for index, row in startupObject.validData.iterrows():

        # Convert each row in the dataframe in to a dict
        record = row.to_dict()

        # For cases where lat and lon is not null, add a new element called location
        if not isnan(record["Lat"]) and not isnan(record["Lon"]):
            record['Location'] = [record["Lat"], record["Lon"]]

        # Delete lat and lon for all the cases. They wont feature in the database
        del record['Lon']
        del record['Lat']

        # Update the data in the database
        # Here update is preferred onver insert since we might have periodic updates of some of the columns
        # Using upsert=True willmake sure both update and insert are performed
        YNOSdatabase.startupInfo.update({"_id": record["startupID"]}, {'$set': record}, upsert=True)

    print("Database is ready...")
    print()
    # Trial to check if the geoJSON is done correctly. It will stay commented
    # query = {"Location": {"$near": [19.0, 72.0]}}
    # # query = {"$and" : [{ "Location": {"$near": [19.0, 72.0 ]}},{"Location": {"$exists": True}}]}
    # cursor = YNOSdatabase.startupInfo.find(query)
    # for val in cursor:
    #     print(val['startupID'])

if __name__=='__main__':

    # Get the fields to be used in various collections
    # Currently only startupInfo data is filled in
    # Will get update on subsequent versions
    collectionObject = classCollectionData()

    # Read input file
    # For python 3 use, encoding = 'ISO-8859-1'
    print ("Reading the input file...")
    print()
    startupData = pd.read_csv('./data/startupData.csv', encoding='ISO-8859-1')

    # Push dataframe into a class
    # It contains various functions to treat the data into a form suitable for the database
    startupObject = classStartupData(startupData)

    # Perform the operation on the data and push to database
    main()


# Backup which explains some altenatives

    # Convert dataframe to dict
    # record = json.loads(row.T.to_json(orient='records')).values()



    # Assign geoJson details
        # record['Location'] ={"type": "Point", "coordinates": [record["Lat"], record["Lon"]]}

    # # Assign Geo JSON Type
        # YNOSdatabase.startupInfo.create_index([("Location", pymongo.GEO2D)])

    # query = {"Location": {"$near": [19.0, 72.0]}}
    # # query = {"$and" : [{ "Location": {"$near": [19.0, 72.0 ]}},{"Location": {"$exists": True}}]}
    # cursor = YNOSdatabase.startupInfo.find(query)
    # for val in cursor:
    #     print(val['startupID'])
    # # FindResults =  YNOSdatabase.starupInfo.find({"foundedDate": {"$exists": True}})
    # FindResults =  YNOSdatabase.starupInfo.find({ "$type": "double" })

        # YNOSdatabase.startupInfo.find({'foundedDate': { "$type": "double"}} ).forEach(function(x){x["foundedDate"] = new timstamp(x.bad)})
        # db.foo.save(x)});
    # How do we change the double to timestamp
    # https://stackoverflow.com/questions/4973095/mongodb-how-to-change-the-type-of-a-field

        # Add other validators in the mongoDB database
