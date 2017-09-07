import os
from inspect import getsourcefile
import shutil



path = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))

#Delete contents in a folder and create a new folder

shutil.rmtree(path+'/dataGeneration/metaOutput')
if not os.path.exists(path+'/dataGeneration/metaOutput'):
    os.makedirs(path+'/dataGeneration/metaOutput')

shutil.rmtree(path+'/dataGeneration/output')
if not os.path.exists(path+'/dataGeneration/output'):
    os.makedirs(path+'/dataGeneration/output')

shutil.rmtree(path+'/Algorithm/Recommendation/output')
if not os.path.exists(path+'/Algorithm/Recommendation/output'):
    os.makedirs(path+'/Algorithm/Recommendation/output')
if os.path.exists(path+'/Algorithm/Recommendation/data/expData.csv'):
    os.remove(path+'/Algorithm/Recommendation/data/expData.csv')
if os.path.exists(path+'/Algorithm/Recommendation/data/educationData.csv'):
    os.remove(path+'/Algorithm/Recommendation/data/educationData.csv')

