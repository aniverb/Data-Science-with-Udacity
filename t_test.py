
import pandas as pd
import scipy.stats
df=pd.read_csv('C:/Users/Tobi/Downloads/baseball_data.csv')
baseball.head()

#how to add a column to data and write data to a file
baseball=df
baseball['nameFull']= baseball['nameFirst']+" "+baseball['nameLast']
baseball.to_csv('C:/Users/Tobi/baseball2.csv')

baseballR=baseball['avg'][baseball['handedness']=='R']
baseballL=baseball['avg'][baseball['handedness']=='L']
tuple=scipy.stats.ttest_ind( baseballL, baseballR , equal_var=False)
if tuple[1]<=.05: 
    print '(False, ('+ str(tuple[0].tolist())+','+str(tuple[1])+')'
else:
    print '(True, ('+ str(tuple[0].tolist())+','+str(tuple[1])+')'
    
    
#official answer    
if tuple[1]<=.05: 
        return (False, (float(tuple[0]), float(tuple[1]))) #float()/str() will cast array properly, no need for .tolist()
else:
        return (True, (float(tuple[0]), float(tuple[1])))
        
baseballR=baseball['avg'][1]


'''3 ways to do the same thing: calculating row difference in dataframe'''

#intuitive
df['weight_diff']=0 
count=-1       
for i in df['weight']:
    count+=1
    print inspect.currentframe().f_back.f_lineno
    if i=='NaN':
        df['weight_diff'][count]=1
    elif count==1156:
        df['weight_diff'][count]=1
    elif df['weight'][count+1]=='NaN':
        df['weight_diff'][count]=1
    else:
        df['weight_diff'][count]=df['weight'][count+1]-i
print df.tail()

#foolproof and more readable, also in a function
df=pd.read_csv('C:/Users/Tobi/Downloads/baseball_data.csv')  
def weight_diff_calc(df):     
        df['weight_diff']=0 
        count=-1       
        for i in df['weight']:
            count+=1
            if pd.isnull(i)==True: #foolproof
                df['weight_diff'][count]=1
            elif count==len(df)-1: #readability
                df['weight_diff'][count]=1
            elif pd.isnull(df['weight'][count+1])==True:
                df['weight_diff'][count]=1
            else:
                df['weight_diff'][count]=df['weight'][count+1]-i
        return df.tail()  
        
weight_diff_calc(pd.read_csv('C:/Users/Tobi/Downloads/baseball_data.csv'))        
#df.shift(1).head() understanding shift function

#based off of the problem's steering/hints (result actually puts result a row below the 2 solutions above)
df=pd.read_csv('C:/Users/Tobi/Downloads/baseball_data.csv')
df['weight_diff']=0
df['weight_diff']=df['weight']-(df['weight'].shift(1))
df['weight_diff']=df['weight_diff'].fillna(1)
print df.head()


def find(word, letter):
    index=-1
    match=0
    while index <len(word)-1:
        index+=1
        if word[index] == letter:
            print index
            match+=1
    if match==0:
        print letter + ' not in ' + word

def find(word, letter):
    match=0
    for index in range(len(word)):
        if word[index] == letter:
            print index
            match+=1
    if match==0:
        print letter + ' not in ' + word
        
find ('banana', 'a')
len('banana')
range(len('banana')+1)
6

def fib(n):
     list=[0]
     a, b = 0, 1
     while a < n:
         a, b = b, a+b
         list.append(a)
     print list[:-1] 
fib(1000)
range(9)[:-1]

def hello():
    return "Hello World!"
    
hello()
