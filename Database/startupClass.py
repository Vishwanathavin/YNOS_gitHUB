import ast
from datetime import datetime
import time
import pandas as pd
import numpy as np
class classCollectionData:
    def __init__(self):
        self.startupInfo = { 'startupID': str,
                        'ICB_industry':str,
                        'ICB_sector':str,
                        'accelaratorResult':str,
                        'accelerator':str,
                        'accleratorDate':datetime,
                        'businessModel':str,
                        'description':str,
                        'foundedDate':datetime,
                        'groupClassification':list,
                        'incubator':str,
                        'incubatorDate':datetime,
                        'incubatorResult':str,
                        'keyword':list,
                        'source':str,
                        'startupClassification':list,
                        'startupName':str,
                        'startupStatus':str,
                        'state':str,
                        'founderName':list,
                        'website':str,
                        'city':str,
                        'Lat' : float,
                        'Lon' : float
                        }
        self.fundingInfo = {}
        self.personInfo = {}
        self.educationInfo = {}
        self.experienceInfo = {}

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
        self.DataFrame = my_dataframe
        self.treatedData = my_dataframe.copy()

    # def: split the strings into arrays ( List)
    # return same dataframe
    def convertStringsToLists(self,colList):
        # startupData.fillna('',inplace=True)
        for col in colList:
            self.treatedData[col] = self.treatedData[col].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else x)

    def convertStringsToTimeStamp(self,dateCol):
        for col in dateCol:
            for index, row in self.treatedData[self.treatedData[col].notnull()].iterrows():
                # self.treatedData[col] = self.treatedData[self.treatedData[col].notnull()][col].apply(lambda x: datetime.strptime(x[:10], '%Y-%m-%d'))
                self.treatedData.loc[index, col] = datetime.strptime(row[col][:10], '%Y-%m-%d')
                # self.treatedData.loc[index, col] = datetime.strptime(row[col], '%Y-%m-%d %H:%M:%S')
            # self.treatedData[col] = self.treatedData[col].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S') if pd.notnull(x) else np.nan)
            # self.treatedData[col] = self.treatedData[col].apply(lambda x: time.mktime(datetime.strptime(x,'%Y-%m-%d %H:%M:%S').timetuple()) if pd.notnull(x) else '' )
    # def: replace nan into '[]'

    def removeUnicodes(self,colList):
        for col in colList:
            self.treatedData[col] = self.treatedData[self.treatedData[col].notnull()][col].apply(
                lambda x: x.decode('unicode_escape'). \
                encode('ascii', 'ignore'). \
                strip())

    def treatEmptyCols(self, colList):

        for col in colList:
            self.treatedData[col].fillna('[]',inplace=True)

    # Check of the column types on input dataframe is the same as we expected
    def validateCollection(self,dictionary):
        self.validData = pd.DataFrame(np.nan, index=self.DataFrame[dictionary.keys()].index,
                                       columns=self.DataFrame[dictionary.keys()].columns)
        for key,val in dictionary.iteritems():
           self.validData[key] =  self.treatedData.loc[self.treatedData[key].apply(type) == val,key]



        # #    # print type(self.treatedData.loc[0,key]),self.treatedData.loc[0,key], val, key
        # #    print self.treatedData[key].apply(type) == val,key
        #    print key
        #    print self.treatedData[key].apply(lambda x: type(x) == dictionary[key])
        #    self.validData[key] =  self.treatedData.loc[self.treatedData[key].apply(lambda x: type(x) == dictionary[key] if pd.notnull(x) else False),key]
           # print self.treatedData['foundedDate'].apply(
           #     lambda x: type(x) == dictionary['foundedDate'] )
           # print dictionary.keys()

