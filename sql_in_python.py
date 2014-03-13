
import pandas
import pandasql #had to pip install via command line (below)

'''C:\Users\Tobi>cd C:\Users\Tobi\Documents\Python Scripts
C:\Users\Tobi\Documents\Python Scripts>python get-pip.py
C:\Users\Tobi\Documents\Python Scripts>pip install -U pandasql'''

aadhaar_data = pandas.read_csv('C:/Users/Tobi/Downloads/aadhar.csv')
aadhaar_data.head()

def sql_query(q):
    # Read in our aadhaar_data csv to a pandas dataframe.  Then rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase.
    aadhaar_data = pandas.read_csv('C:/Users/Tobi/Downloads/aadhar.csv')
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    # Select out the first 50 values for "registrar" and "enrolment_agency"
    aadhaar_solution = pandasql.sqldf(q, locals())
    return aadhaar_solution 

sql_query("""SELECT registrar, enrolment_agency FROM aadhaar_data LIMIT 50""")
sql_query("""SELECT District, count(District) from aadhaar_data WHERE Age>50 and Aadhaar_generated=1 GROUP BY District LIMIT 50""")
sql_query("""SELECT District, Gender, count(Gender) from aadhaar_data WHERE Age>50 and Aadhaar_generated=1 GROUP BY District, Gender limit 50""") #should be the ssame as below
sql_query("""SELECT  District, Gender, sum(Aadhaar_generated) from aadhaar_data WHERE Age>50 GROUP BY District, Gender LIMIT 50""")


#how to add a column to data and write data to a file
baseball=pandas.read_csv(path_to_csv)
baseball['nameFull']= baseball['nameFirst']+" "+baseball['nameLast']
baseball.to_csv(path_to_new_csv)
