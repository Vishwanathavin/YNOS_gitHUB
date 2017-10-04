import pandas as pd
class classStartupInfo:

    def __init__(self, my_dataframe):
        self.my_dataframe = my_dataframe


def startupInfoValidate(startupInfo):

    startupObject = classStartupInfo(startupInfo)


def main():
    startupData = pd.read_csv('../dataGeneration/output/startupData.csv')
    personData = pd.read_csv('../dataGeneration/output/personData.csv')

    # get the startup related details
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

    startupInfo = startupData.ix[:, col]
    startupInfoValidate(startupInfo)


if __name__=='__main__':
    main()