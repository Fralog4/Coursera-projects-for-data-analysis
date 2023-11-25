#To use numpy you have to import it using 
	import numpy as np
	 #(as np to say just in the code np and not numpy, it's quicker)
	list_1=[10,20,30,40,50]
	list_1 #create an array
#How to create a numpy_array:
	my_numpy_array= np.array(list_1)
	my_numpy_array
	type(my_numpy_array) #(it's to use TAB)
#How to creare multi-dimensional array(MATRIX):
	my_matrix=np.array([ [3,5,6],[8,8,9] ])
	my_matrix
#exercise: 
    my_matrix1= np.array([[3,7,6,5],[5,6,7,8]])
#TASK2:  RAND():
	x=np.random.rand(20)
	x #(It shows 20 random number from 0 to 1)
#you can create a matrix of random number as well
	x=np.random.rand(3,3)
	x
# "randint" is used to generate random integers between upper and lower bounds
	x=np.random.randint(1,50)
	x
# "randint" can be used to generate a certain number of random itegers as follows+
	x=np.random.randint(1,100,15)
	x
	#(I wanted to generate 15 numbers in range 1 to 100)
# np.arange creates an evenly spaced values within a given interval
	x= np.arange(1,30)
	x
# create a diagonal of ones and zeros everywhere else
	x= np.eye(7)
	x #(I have created a matrix in which the diagonal numbers(1+1+1+...=7) is the number is parenthesis)
# Matrix of ones
	x=np.ones((7,7))
	x      #(matrix of 7 rows x 7 columns that have only 1 numbers)
# Matrix of zeros
 x=np.zeros(8)
 x
#Exercise: Write a code that takes in a positive int x from user and creates an array with random numbers from 0 to x in 1x10
	import numpy as np
	x=int(input("Please enter a positive int:"))
	my_matrix= np.random.randint(0,x,10)
	my_matrix
#MATHS WITH NUMPY:
#Define two arrays and sum them:
x=np.arange(1,10)
y=np.arange(1,10)
sum= x+y
squared= x**2
sqrt=np.sqrt(squared)
#Ex: Give the distance between x and y:
	x= np.array([5,7,20])
	y=np.array([9,15,4])
	z= np.sqrt(x**2 + y**2)
	z
#HOW TO SLICE AND INDEXING ARRAY
my_numpy_array= np.array([3,5,6,2,8,10,20,50])
my_numpy_array
my_numpy_array[0] #it acces to the first element that is 3
my_numpy_array[0:3] #it shows the first three elements
my_numpy_array[0:4] = 7 #this overwrite the first 4 elements and put 7 on them
# Let's define a two dimensional numpy array
matrix = np.random.randint(1,10,(4,4))
matrix
#Get a row from matrix
matrix[0]
#the second row etc... matrix [1]or matrix[-1] to get the last one
#Get one element
matrix[0,2] #first row second element
#PERFORM ELEMENTS SELECTION:
#Let's define a multidimensional array 5x5
	import numpy as np
	matrix= np.random.randint(1,10,(5,5))
	matrix
#now we start filtering and putting condition... we want only the elements >7
	new_matrix=matrix[matrix>7]
	new_matrix
#Now I want only the odd numbers(dispari)
	new_matrix=matrix[matrix%2==1] #(if I put the == 0 I obtain the(pari) numbers)
	new_matrix
#Exercise : In the following matrix replace negative element by 0 and replace odd elements with -2
X = np.array([[2, 30, 20, -2, -4],
    [3 ,4 ,40 ,-3 ,-2],
    [-3 ,4, -6, 90, 10],
    [25 ,45 ,34 ,22 ,12],
    [13 ,24 ,22, 32, 37]])
X
X[X<0]=0 #if there's a numbers less than 0 then replace it with 0
X[X%2==1]=-2 #if there is an odd number than replace it with -2
X
#you do not need any "if" statement
#PANDA FUNDAMENTALS:
# Pandas is a data manipulation and analysis tool that is built on Numpy.
# Pandas uses a data structure known as DataFrame (think of it as Microsoft excel in Python). 
# DataFrames empower programmers to store and manipulate data in a tabular fashion (rows and columns).
# Series Vs. DataFrame? Series is considered a single column of a DataFrame.
# Let's define a two-dimensional Pandas DataFrame
# Note that you can create a pandas dataframe from a python dictionary
	import pandas as pd
	bank_client_df= pd.DataFrame({"Bank Vlient ID":[111,222,333,444],
                             "Bank Client Name":["Chanel","Steve","Mitch","Ryan"],
                             'Net Worth[$]':[3500,29000,10000,2000],
                             'Years with bank':[3,4,9,5]})
	bank_client_df
#With this you create a table with all elements in it
# you can only view the first couple of rows using .head()
bank_client_df.head(x) #x= a number ex.2 you see the first two rows of the table
# you can only view the last couple of rows using .tail()
bank_client_df.tail(x)
#Exercise:
#A porfolio contains a collection of securities such as stocks, bonds and ETFs. Define a dataframe named 'portfolio_df' that holds 3 different stock ticker symbols, number of shares, and price per share (feel free to choose any stocks)
#Calculate the total value of the porfolio including all stocks
portfolio_df= pd.DataFrame({'Stock ticker symbol':['AAPL','AMZN','T'],
                           'Price per share[$]':[3500,200,400],
                           'Number of stocks':[3,4,9]})
portfolio_df
stocks_dollar_value= portfolio_df['Price per share[$]']*portfolio_df['Number of stocks']
stocks_dollar_value
stocks_dollar_value.sum() #you get the sum of the portfolio
#PANDAS WITH CSV AND HTML:
#Now I'm going to read website's info by Pandas:
import pandas as pd
house_price_df= pd.read_html('https://www.livingin-canada.com/house-prices-canada.html')
house_price_df[0] or house_price_df[1]
#PANDAS OPERATIONS:
import pandas as pd
bank_client_df= pd.DataFrame({"Bank Vlient ID":[111,222,333,444],
                             "Bank Client Name":["Chanel","Steve","Mitch","Ryan"],
                             'Net Worth[$]':[3500,29000,10000,2000],
                             'Years with bank':[3,4,9,5]})
bank_client_df
# Pick certain rows that satisfy a certain criteria 
df_loyal= bank_client_df[ bank_client_df['Years with bank'] >=5]
df_loyal
# Delete a column from a DataFrame
del bank_client_df['Bank Client ID'] (put the name of the column you want to delete)
bank_client_df
#Exercise:
#Using "bank_client_df" DataFrame, leverage pandas operations to only select high networth individuals with minimum $5000 
#What is the combined networth for all customers with 5000+ networth?
#solution:
df_high_networth= bank_client_df[ bank_client_df['Net Worth[$]']>=5000]
df_high_networth
df_high_networth['Net Worth[$]'].sum()
#PANDAS WITH FUNCTIONS:
# Define a function that increases all clients networth (stocks) by a fixed value of 20% (for simplicity sake) 
def networth_update(balance):
    return balance * 1.2 (1.2=20%)
# You can apply a function to the DataFrame 
bank_client_df['Net Worth[$]'].apply(networth_update)
#Another example of apply:
bank_client_df['Bank Client Name'].apply(len) #it show the len of bank client names
#Exercise: 
#Define a function that triples the stock prices and adds $200
#Apply the function to the DataFrame
#Calculate the updated total networth of all clients combined

def networth_update(balance):
    return balance*3+200
result=bank_client_df['Net Worth[$]'].apply(networth_update)
result
result.sum()
#PERFOM SORTING AND ORDERING IN PANDAS:
# You can sort the values in the dataframe according to number of years with bank
bank_client_df.sort_values(by = 'Years with bank')
# Note that nothing changed in memory! you have to make sure that inplace is set to True
# Set inplace = True to ensure that change has taken place in memory 
bank_client_df.sort_values(by='Years with bank',inplace=True)
#MERGING AND CONCATENATING WITH PANDAS:
#Let's define some DataFrame
import pandas as pd
df1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                 'B':['B0','B1','B2','B3'],
                 'C':['C0','C1','C2','C3'],
                 'D':['D0','D1','D2','D3']},
                index=[0,1,2,3])
df1

df2=pd.DataFrame({'A':['A4','A5','A6','A7'],
                 'B':['B4','B5','B6','B7'],
                 'C':['C4','C5','C6','C7'],
                 'D':['D4','D5','D6','D7']},
                index=[4,5,6,7])
df2

df3=pd.DataFrame({'A':['A8','A9','A10','A11'],
                 'B':['B8','B9','B10','B11'],
                 'C':['C8','C9','C10','C11'],
                 'D':['D8','D9','D10','D11']},
                index=[8,9,10,11])
df3
#Now I want to concatenate these dataframe
pd.concat([df1,df2,df3]) #it will shows a large df wich contains all of them
#TASK 12 PROJECT:
#1)Define a dataframe named 'Bank_df_1' that contains the first and last names for 5 bank clients with IDs = 1, 2, 3, 4, 5
#2)Assume that the bank got 5 new clients, define another dataframe named 'Bank_df_2' that contains a new clients with IDs = 6, 7, 8, 9, 10
#3)Let's assume we obtained additional information (Annual Salary) about all our bank customers (10 customers)
#4)Concatenate both 'bank_df_1' and 'bank_df_2' dataframes
#5)Merge client names and their newly added salary information using the 'Bank Client ID'
#6)Let's assume that you became a new client to the bank
#7)Define a new DataFrame that contains your information such as client ID (choose 11), first name, last name, and annual salary.
#8)Add this new dataframe to the original dataframe 'bank_df_all'.

#Solutions:
import pandas as pd
import numpy as np
raw_data={'Bank Client ID':['1','2','3','4','5'],
         'First Name':["Nancy",'Alex','Shep','Max','Allen'],
         'Last Name':['Rob','Ali','George','Mitch','Steve']}
Bank_df_1=pd.DataFrame(raw_data, columns=['Bank Client ID','First Name','Last Name'])
Bank_df_1
raw_data={'Bank Client ID':['6','7','8','9','10'],
         'First Name':["Rob",'Dina','Sarah','Matteo','Allan'],
         'Last Name':['Robbinson','Akit','Guzzo','Mitchelle','Stevenson']}
Bank_df_2=pd.DataFrame(raw_data,columns=['Bank Client ID','First Name','Last Name'])
Bank_df_2
raw_data= {'Bank Client ID':['1','2','3','4','5','6','7','8','9','10'],
          'Annual Salary [$/year]': [25000,35000,45000,50000,32000,22000,100000,10000,34000,23400]}
bank_df_salary=pd.DataFrame(raw_data,columns= ['Bank Client ID','Annual Salary [$/year]'])
bank_df_salary
bank_df_all=pd.concat([Bank_df_1, Bank_df_2])
bank_df_all= pd.merge(bank_df_all,bank_df_salary, on = 'Bank Client ID')
bank_df_all
new_client={'Bank Client ID':['11'],
           'First Name':['Francesco'],
           'Last Name':['Lo Gullo'],
           'Annual Salary [$/year]':[5000]}
new_client_df=pd.DataFrame(new_client,columns= ['Bank Client ID',
                                                'First Name','Last Name', 'Annual Salary [$/year]']) 
new_client_df
new_df= pd.concat([bank_df_all,new_client_df], axis=0)
new_df
