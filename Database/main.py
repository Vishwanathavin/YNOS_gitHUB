import pymongo
import pandas as pd
import json

def adjustStartup(db):
    startupFile = pd.read_csv('./data/startupData.csv')
    records = json.loads(startupFile.T.to_json()).values()

    db.trial.insert(records)
    # get the city in the right format

    # Set validators
    # Push
    print "Do nothing"
def adjustPerson():
    # remove unicodes
    # Validators
    # Push to database
    print "DO nothing"

def main():
    try:
        conn = pymongo.MongoClient()
        print "Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e

    db = conn.YNOS

    adjustStartup(db)
    # adjustPerson(db)
if __name__=="__main__":
    main()


