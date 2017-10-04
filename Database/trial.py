import pandas as pd
class classStartupInfo:

    def __init__(self, my_dataframe):
        self.name = my_dataframe.name
        self.age = my_dataframe.age

    def printType(self):
        print type(self.name.iloc[0]),self.name.iloc[0]
        print type(self.age),self.age

def main():
    startupData = pd.read_csv('temp.csv')

    startupClass = classStartupInfo(startupData)
    startupClass.printType()

if __name__=='__main__':
    main()