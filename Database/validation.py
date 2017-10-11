import pandas as pd
import numpy as np
import ast
class classStartupData:

    def __init__(self, my_dataframe):
        self.DataFrame = my_dataframe

    startupInfoCol = {'startupID':str,
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
    'city':str,
    'dataValidation':bool,
    'investmentStatus':bool
    }
    fundingInfoCol = {'dealInvestmentAmount': 'string',
                        'roundDate': 'string',
                        'roundInvestmentAmount': 'string',
                        'roundInvestorCount': 'string',
                        'roundLeadInvestorType': 'string',
                        'roundValuation': 'string',
                        'equityValuation': 'string',
                        'investorName': 'string',
                        'investorType': 'string',
                        'investmentStage': 'string',
                        'linkedinURL': 'string',
                        'stageClassification':'string'
                      }
    # Split the dataframe
    def splitDataFrame(self):
        self.startupInfo = self.DataFrame[[col for col,value in self.startupInfoCol.iteritems()]]
        self.fundingInfo = self.DataFrame[[col for col,value in self.fundingInfoCol.iteritems()]]


    def printDataType(self):
        print "Printing startup Info datatypes"
        for column in self.startupInfo:
            print type(self.startupInfo.loc[0,column]),column
        print "Printing funding Info datatypes"
        for column in self.fundingInfo:
            print type(self.fundingInfo.loc[0,column]),column

    def validateDataType(self):
        # self.startupInfo.loc[0,'ICB_industry'] = 25
        print "Before dropping"
        print self.startupInfo.shape
        self.checkedInfo = pd.DataFrame()
        # self.checkedInfo['startupName'] = self.startupInfo['startupName']


        for key,val in self.startupInfoCol.iteritems():

            self.checkedInfo[key]= self.startupInfo.loc[self.startupInfo[key].apply(type)==val,key]

        # To be changed ingo
        # toBeChangedInfo = (self.startupInfo != self.checkedInfo).any(1)
        changedLocations =  (np.where(self.startupInfo != self.checkedInfo))
        changeDataFrame = pd.DataFrame(np.nan,index=self.startupInfo.index,columns=self.startupInfo.columns)
        changeDataFrame['startupName'] = self.startupInfo['startupName']
        for row in changedLocations[0]:
            # print self.startupInfo.ix[row,changedLocations[1][row]]
            changeDataFrame.ix[row,changedLocations[1][row]]=self.startupInfo.ix[row,changedLocations[1][row]]
        changeDataFrame.fillna('').to_csv('output.csv',index=False)
        # seriesList = []
        # # val = zip(toBeChangedInfo2[0],toBeChangedInfo2[1])
        #
        #
        # Arrays =  [(cell,toBeChangedInfo2[1][cell]) for cell in toBeChangedInfo2[0]]
        #
        #
            # series = pd.Series[self.startupInfo.ix[cell,toBeChangedInfo2[1][cell-1]]]
            # print self.startupInfo.ix[cell,toBeChangedInfo2[1][cell-1]]
            # print series

        # print self.rework
        # self.startupInfo.ix[toBeChangedInfo2[0], toBeChangedInfo2[1]].to_csv('./recheck.csv')
        # print toBeChangedInfo2
        #
        #     print self.startupInfo.ix[val[0],val[1]]
        # print [(val[0],val[1]) for val in zip(toBeChangedInfo2[0],toBeChangedInfo2[1])]
        # print self.startupInfo.ix[toBeChangedInfo2[0],toBeChangedInfo2[1]]
    # use apply map to get the rows where it doesnt meet the datatype requirement
    # df.loc[df.C.apply(type) != float]


# Get the string representation of ararays into arrays
def startupInfoTreat(startupData):
    startupData.fillna('',inplace=True)

    arrayColumns = ['groupClassification','startupClassification','keyword','founderName']

    for col in arrayColumns:
        startupData[col]=startupData[col].apply(ast.literal_eval)

    startupObject = classStartupData(startupData)
    startupObject.splitDataFrame()
    # startupObject.printDataType()
    startupObject.validateDataType()


    # Print the members of the class
    # members = [attr for attr in dir(startupObject) if not callable(getattr(startupObject, attr)) and not attr.startswith("__")]
    # print members

def main():
    startupData = pd.read_csv('./data/startupData.csv',na_filter=False)
    # personData = pd.read_csv('../dataGeneration/output/personData.csv')


    # Fill additional details to the starupupdata
    # StartupID: we need to think of a way to do it better
    startupData['startupID'] = ["S_" + str(index) for index,row in startupData.iterrows()]
    #  dataValidation
    startupData['dataValidation'] = True
    # investmentStatus
    startupData['investmentStatus'] = False
    # get the startup related details
    # col = []

    # startupInfo = startupData.ix[:, col]

    startupInfoTreat(startupData)


if __name__=='__main__':
    main()