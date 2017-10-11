import pandas as pd
import numpy as np

dictionary = {
            'startupID':'string',
            'ICB_industry':'string',
            'ICB_sector':'string',
            'accelaratorResult':'string',
            'accelerator':'string',
            'accleratorDate':'string',
            'businessModel':'string',
            'description':'string',
            'foundedDate':'string',
            'groupClassification':'string',
            'incubator':'string',
            'incubatorDate':'string',
            'incubatorResult':'string',
            'keyword':'string',
            'source':'string',
            'startupClassification':'string',
            'startupName':'string',
            'startupStatus':'string',
            'state':'string',
            'founderName':'string',
            'website':'string',
            'city':'string',
            'dataValidation':'string',
            'investmentStatus':'string'
}

for key,value in dictionary.iteritems():
    print key," : ", value


# val1 = internData[internData['startupClassification'].notnull()]['startupClassification']
# val2 = internData[internData['startupClassification2'].notnull()]['startupClassification2']
# print val1.index.values
# print val2.index.values
# print zip(val1,val2)

# for val in(zip(internData[internData['startupClassification'].notnull()]['startupClassification'],internData[internData['startupClassification2'].notnull()]['startupClassification2'])):
#     print val,len(val)
# internData['startupClassification'] = [list(val) if len(val) > 1 else val for val in(zip(internData[internData['startupClassification'].notnull()]['startupClassification'],internData[internData['startupClassification2'].notnull()]['startupClassification2']))]
# print internData['startupClassification']
# for index, rows in internData.iterrows():
#     print len(internData.loc[index,'startupClassification'])