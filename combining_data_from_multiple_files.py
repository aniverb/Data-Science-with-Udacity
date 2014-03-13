
import os
import pandas as pd
os.chdir("C:/Users/Tobi/Documents/Python Scripts/anaconda")


def create_master_turnstile_file(filenames,output_file):
    file_df=[]
    for files in filenames:
        file_df.append(pd.read_csv(files))
    output=pd.concat(file_df)
    output.to_csv(output_file)
    
create_master_turnstile_file(['test1.csv','test2.csv'],'new_test.csv')

test1=pd.read_csv('test1.csv')
test2=pd.read_csv('test2.csv')
pd.concat([test1,test2])

    
