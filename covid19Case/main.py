

'''
import pandas as pd
mydataset = [
   ["BMW", "Volvo", "Ford"],
   [3, 7, 2]
]

myvar = pd.Series(mydataset, index = ["Array 1", "Array 2"]) 
#colowm with lables in index array associate to objects in  mydataset array

#print(myvar["Array 1"])

calories = {"day1": 420, "day2": 380, "day3": 390} #dic key/value where keys become labels no need 


#myvar = pd.Series(calories)
myvar = pd.Series(calories, index = ["day1", "day2"])

#2-D
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

print()
#print(myvar.loc[0]) Return row 0 
print(myvar.loc[[1,2]]) #Return row 0 and 1:

print()'''

'''
#opn csv file
import pandas as pd
import matplotlib.pyplot as plt

# maximum returned rows
returned_rows = pd.options.display.max_rows

df = pd.read_csv('data.csv') #Original data set

quick_view = df.head(20)

last_rows = df.tail()

#df_info = df.info() 



#Remove empty cells if any

  #removed_empty_cell_data = df.dropna() #drops whole rolls that has empyt rows instead I will use fillna()

#Replace empty cells with value

  #print(df.fillna(0))

#info about first row in data-frame/table
  #print(df.loc[0].info())
  
#Convert to date format
df['Date'] = pd.to_datetime(df['Date'])
#show firs and last 5 dates
df['Date']
#show all dates
df['Date'].to_string()

#Removing null values in Date colounm and create new instance of data frame
df.dropna(subset=['Date'], inplace = True)
#show info about data frame indicating no null values in the date colunm
#df.info()

#Consititution of wrong date data is anything but thi format : 2020-01-16 and should be removed

'''


'''

#replace null values for specific coloumn in table with zero, make new instance of table and manipulate it(inplace parameter)
df["positive"].fillna(0, inplace = True)
m = df["positive"].max()
mean = df["positive"].mean()
median = df["positive"].median()
mode = df["positive"].mode()
#print("\nHighest",m," average: ",mean," Middle: ",median," Most Frequent: ",mode)

df["death"].fillna(0, inplace = True)
m = df["death"].max()
mean = df["death"].mean()
median = df["death"].median()
mode = df["death"].mode()
#print("\nHighest",m," average: ",mean," Middle: ",median," Most Frequent: ",mode)

df["recovered"].fillna(0, inplace = True)
m = df["recovered"].max()
mean = df["recovered"].mean()
median = df["recovered"].median()
mode = df["recovered"].mode()
#print("\nHighest",m," average: ",mean," Middle: ",median," Most Frequent: ",mode)

#total_tested 
df["total_tested"].fillna(0,inplace=True)
m = df["total_tested"].max()
mean = df["total_tested"].mean()
median = df["total_tested"].median()
mode = df["total_tested"].mode()
#print("\nHighest",m," average: ",mean," Middle: ",median," Most Frequent: ",mode)

print(df['Country_Region'])

'''

'''

#.....boolean datatype......

print(type(False)) 

#.....int datatype......

print(type(12)) 

#.....float datatype......  

print(type(1.067)) 

# print(type(1006L)) error

#.....string datatype....

print(type("True"))

'''

'''
s = input("enter anything")
if s.__contains__(st.ascii_letters) and s.__contains__(""):
  print(type(""))
else:
  print(type(9))
'''

'''
import string as st

s = input("enter anything")
if s.__contains__(st.ascii_letters):
    print(type(""))
else:
    print(type(9))
'''



# New_Arr = [df['positive'],df['death'],df['recovered'], df['active'], df['hospitalized']
    # ,df['daily_tested'],df['hospitalizedCurr']]
    
    
s = input("Your name is: ")
print(s,s,s)
