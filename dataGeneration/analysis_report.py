import os
import pandas as pd
from inspect import getsourcefile
import codecs
import numpy as np

def analysis(filename):
    path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    if (os.path.exists(path+'/output/%s'%filename)):
        print(path.replace('\\', '/')+'/output/%s'%filename)
        with codecs.open(path.replace('\\', '/')+'/output/%s'%filename, "r", encoding='utf-8', errors='ignore') as temp_file:
            startupData = pd.read_csv(temp_file)
        # startupData = pd.read_csv(path.replace('\\', '/')+'/output/%s'%filename)
        missing_startupData = startupData[startupData.isnull().any(axis=1)]
        missing_startupData.to_csv(path + '/metaOutput/missing _comps_details.csv', index=False,
                                   encoding='utf-8')

        log_file_path = path + '/metaOutput/log_missing_values.txt'
        empty_cells = startupData.isnull().sum().sum()
        empty_cols = startupData.isnull().sum().to_frame().transpose()
        col_names = ','.join(startupData.columns)
        footer = '\nTotal empty cells needs to be filled: ' + str(empty_cells) + '\n' + 'Total number of companies ' \
                 'containing missing data: ' + str(missing_startupData.shape[0]) + '\n '

        np.savetxt(log_file_path, empty_cols.values, fmt='%d', delimiter=',', header=col_names, footer=footer)

    else:
        print('File is not present')

if __name__ == '__main__':
    file = 'startupData.csv'
    analysis(file)