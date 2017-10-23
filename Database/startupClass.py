import ast
from datetime import datetime
import time
import pandas as pd
import numpy as np
class classCollectionData:
    def __init__(self):
        self.startupInfo = { 'startupID': {"type": str},
                            'ICB_industry':{"type": str},
                            'ICB_sector':{"type": str},
                            'accelaratorResult':{"type": str},
                            'accelerator':{"type": str},
                            'accleratorDate':{"type": datetime},
                            'businessModel':{"type": str},
                            'description':{"type": str},
                            'foundedDate':{"type": datetime},
                            'groupClassification':{"type": list,
                                                   "element":{"type": str}
                                                   },
                            'incubator':{"type": str},
                            'incubatorDate':{"type": datetime},
                            'incubatorResult':{"type": str},
                            'keyword':{"type": list,
                                       "element":{"type": str}
                                       },
                            'source':{"type": str},
                            'startupClassification':{"type": list,
                                                     "element":{"type": str}
                                                     },
                            'startupName':{"type": str},
                            'startupStatus':{"type": str},
                            'state':{"type": str},
                            'founderName':{"type": list,
                                           "element":{"type": str}
                                           },
                            'website':{"type": str},
                            'city':{"type": str},
                            'Lat' : {"type": float},
                            'Lon' : {"type": float}
                        }
        self.fundingInfo = {}
        self.personInfo = {}
        self.educationInfo = {}
        self.experienceInfo = {}

    # append all the fields from all the collections and return
    # collections whose columns are not yet filled will be empty
    def getColumns(self):
        colDict = {}
        colDict.update(self.startupInfo)
        colDict.update(self.fundingInfo)
        colDict.update(self.personInfo)
        colDict.update(self.educationInfo)
        colDict.update(self.experienceInfo)
        return colDict


class classStartupData:

    # Dataframe
    def __init__(self, my_dataframe):
        # Original dataframe
        self.DataFrame = my_dataframe
        # Copy of the dataframe so that we can treat the data.
        #  We need to retail the old format later use
        # copy is used so that the dataframe is duplicated
        self.treatedData = my_dataframe.copy()

    # split the strings into arrays ( List)
    def convertStringsToLists(self,colList):
        # For each column in the list whose type is 'list'
        for col in colList:
            # for each row split string to list for rows that are not null. ast.literal eval will fail for null values
            self.treatedData[col] = self.treatedData[col].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else x)

    # Convert the strings into datetime
    def convertStringsToTimeStamp(self,dateCol):
        # For each column in the list whose type is 'date'
        for col in dateCol:
            for index, row in self.treatedData[self.treatedData[col].notnull()].iterrows():
                self.treatedData.loc[index, col] = datetime.strptime(row[col][:10], '%Y-%m-%d')

    def removeUnicodes(self,colList):
        for col in colList:
            self.treatedData[col] = self.treatedData[self.treatedData[col].notnull()][col].apply(
                lambda x: x.decode('unicode_escape'). \
                encode('ascii', 'ignore'). \
                strip())

    # Replace nan with '[]'
    def treatEmptyCols(self, colList):
        for col in colList:
            self.treatedData[col].fillna('[]',inplace=True)

    # Check of the column types on input dataframe is the same as we expected
    def validateCollection(self,dictionary):
        # declare a dataframe that has only elements that has passed validation
        # Initialize the dataframe with nan values and the dimensions equal to the original dataframe

        self.validData = pd.DataFrame(np.nan, index=self.DataFrame[list(dictionary)].index,
                                       columns=self.DataFrame[list(dictionary)].columns)

        # For each column/field in the collections
        for key,val in dictionary.items():

           # Check if the dimesnions are equal to the corresponding field
           self.validData[key] =  self.treatedData.loc[self.treatedData[key].apply(type) == val["type"],key]

           # In case of list elements, we need to further check if the sub elements are of the same type
           if val["type"] == list:
               # Check only the sub elements of the ones that are not null.
               # We are using the entire column for this loop and we need to filter out the nan elements
               for index, row in self.validData[self.validData[key].notnull()].iterrows():

                   # initialize a list. We will append the list with the correct values and assign it to the corresponding cell
                   elemList=[]

                   # For each element in the cell ( row, column are already being iterated)
                   for elem in self.validData.loc[index, key]:
                       # Append the element to the list if it matches
                       if (isinstance(elem, val["element"]['type']) == True):
                           elemList.append(elem)
                       # Append nan if it fails
                       else:
                           elemList.append(np.nan)
                   # Set it to the cell.
                   # This list will have the elements where it is right and a nan if it is wrong
                   self.validData.set_value(index, key,elemList)


# Comments
# #    # print type(self.treatedData.loc[0,key]),self.treatedData.loc[0,key], val, key
# #    print self.treatedData[key].apply(type) == val,key
#    print key
#    print self.treatedData[key].apply(lambda x: type(x) == dictionary[key])
#    self.validData[key] =  self.treatedData.loc[self.treatedData[key].apply(lambda x: type(x) == dictionary[key] if pd.notnull(x) else False),key]
# print self.treatedData['foundedDate'].apply(
#     lambda x: type(x) == dictionary['foundedDate'] )
# print dictionary.keys()

# Datetime formats
# self.treatedData[col] = self.treatedData[self.treatedData[col].notnull()][col].apply(lambda x: datetime.strptime(x[:10], '%Y-%m-%d'))
# self.treatedData.loc[index, col] = datetime.strptime(row[col], '%Y-%m-%d %H:%M:%S')
# self.treatedData[col] = self.treatedData[col].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S') if pd.notnull(x) else np.nan)
# self.treatedData[col] = self.treatedData[col].apply(lambda x: time.mktime(datetime.strptime(x,'%Y-%m-%d %H:%M:%S').timetuple()) if pd.notnull(x) else '' )