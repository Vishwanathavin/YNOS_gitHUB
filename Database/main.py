import pymongo
import pandas as pd
import json

def adjustStartup(db):
    # startupFile = pd.read_csv('./data/startupData.csv')
    # records = json.loads(startupFile.T.to_json()).values()
    records={
  "fields": [
    {
      "name": "_id",
      "path": "_id",
      "count": 1,
      "types": [
        {
          "name": "ObjectID",
          "bsonType": "ObjectID",
          "path": "_id",
          "count": 1,
          "values": [
            "59c40ef93de3541955910469"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "ObjectID",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "businessModel",
      "path": "businessModel",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "businessModel",
          "count": 1,
          "values": [
            "B2B2C"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "city",
      "path": "city",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "city",
          "count": 1,
          "values": [
            "Chennai"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "dealDate",
      "path": "dealDate",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "dealDate",
          "count": 1,
          "values": [
            "[Timestamp('2015-09-17 00:00:00'), Timestamp('2015-09-17 00:00:00'), Timestamp('2015-09-17 00:00:00')]"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "founderID",
      "path": "founderID",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "founderID",
          "count": 1,
          "values": [
            "['F001','','F002']"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "founderName",
      "path": "founderName",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "founderName",
          "count": 1,
          "values": [
            "['MOHAMMED BHOL', 'KRISHNAKANT THAKUR', 'ANURAG MEHROTRA']"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "groupClassification",
      "path": "groupClassification",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "groupClassification",
          "count": 1,
          "values": [
            "['DevOps','Alternate energy sources ']"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "ICB_Industry",
      "path": "ICB_Industry",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "ICB_Industry",
          "count": 1,
          "values": [
            "Technology"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "ICB_Sector",
      "path": "ICB_Sector",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "ICB_Sector",
          "count": 1,
          "values": [
            "Technology Hardware & Equipment"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "investorID",
      "path": "investorID",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "investorID",
          "count": 1,
          "values": [
            "['F001','F002']"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "investorName",
      "path": "investorName",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "investorName",
          "count": 1,
          "values": [
            "'VINOD MUTHUKRISHNAN', 'SRIRAM SUBRAMANIAN'"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "Lat",
      "path": "Lat",
      "count": 1,
      "types": [
        {
          "name": "Number",
          "bsonType": "Number",
          "path": "Lat",
          "count": 1,
          "values": [
            12.98
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "Number",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "Lon",
      "path": "Lon",
      "count": 1,
      "types": [
        {
          "name": "Number",
          "bsonType": "Number",
          "path": "Lon",
          "count": 1,
          "values": [
            80.20945
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "Number",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "roundInvestmentAmountINR",
      "path": "roundInvestmentAmountINR",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "roundInvestmentAmountINR",
          "count": 1,
          "values": [
            "[28.868617159999999, 28.868617159999999, 28.868617159999999]"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "Source",
      "path": "Source",
      "count": 1,
      "types": [
        {
          "name": "Null",
          "bsonType": "Null",
          "path": "Source",
          "count": 1,
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "Null",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "startupClassification",
      "path": "startupClassification",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "startupClassification",
          "count": 1,
          "values": [
            "Clean Technology"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "startupID",
      "path": "startupID",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "startupID",
          "count": 1,
          "values": [
            "s001"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    },
    {
      "name": "startupName",
      "path": "startupName",
      "count": 1,
      "types": [
        {
          "name": "String",
          "bsonType": "String",
          "path": "startupName",
          "count": 1,
          "values": [
            "Gradient-U"
          ],
          "total_count": 0,
          "probability": 1,
          "unique": 1,
          "has_duplicates": "false"
        }
      ],
      "total_count": 1,
      "type": "String",
      "has_duplicates": "false",
      "probability": 1
    }
  ],
  "count": 1
}
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


