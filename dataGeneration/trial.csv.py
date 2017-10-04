import pandas as pd

internold = pd.read_csv('./temp/interns.csv')


internnew = pd.read_csv('./temp/internNew.csv')

commondata = internold[internold.startupName.isin(internnew.startupName)]

uncommondata1 =  internold[~internold.startupName.isin(internnew.startupName)]
uncommondata2 =  internnew[~internnew.startupName.isin(internold.startupName)]
print uncommondata1.shape,uncommondata2.shape

internData = pd.concat([uncommondata1, uncommondata2], axis=0, ignore_index=True)

internData.to_csv('./temp/interndata.csv')
