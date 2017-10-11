import pandas as pd

file = pd.DataFrame()
print "File",file
data = pd.Series({"index": 0,"A": 21})
print "Data",data
# data2 = pd.Series({index"C":30})
# data=data.append(data2)
file=file.append(data)
data = pd.Series({"index" : 3,"B": 32})

file=file.append(data,ignore_index=True)
print file.head()