#Final Project
#1)Define a dataframe named 'Bank_df_1' that contains the first and last names for 5 bank clients with IDs = 1, 2, 3, 4, 5
#2)Assume that the bank got 5 new clients, define another dataframe named 'Bank_df_2' that contains a new clients with IDs = 6, 7, 8, 9, 10
#3)Let's assume we obtained additional information (Annual Salary) about all our bank customers (10 customers)
#4)Concatenate both 'bank_df_1' and 'bank_df_2' dataframes
#5)Merge client names and their newly added salary information using the 'Bank Client ID'
#6)Let's assume that you became a new client to the bank
#7)Define a new DataFrame that contains your information such as client ID (choose 11), first name, last name, and annual salary.
#8)Add this new dataframe to the original dataframe 'bank_df_all'
import pandas as pd
Bank_df_1=pd.DataFrame({'First Name':['Marco','Luca','Kevin','Sara','Nicola'],
                        'Last Name':['Landers','Fazio','Lasagna','Youssef','Neglia'],
                        'Bank Client ID':['1','2','3','4','5']

})
Bank_df_2=pd.DataFrame({'First Name':['Marlon','Giuseppe','Andrea','Pino','Frank'],
                        'Last Name':['Friks','Vita','Pellegrino','Insegno','Caruso'],
                        'Bank Client ID':['6','7','8','9','10']
})
salary={'Bank Client ID': ['1','2','3','4','5','6','7','8','9','10'],
        'Annual Salary [$/year]': [25000,35000,45000,50000,32000,22000,100000,10000,34000,23400]}
bank_df_salary=pd.DataFrame(salary,columns= ['Bank Client ID','Annual Salary [$/year]'])
bank_df_all=pd.concat([Bank_df_1,Bank_df_2])
bank_df_all=pd.merge(bank_df_all,bank_df_salary, on='Bank Client ID')
me={'Bank Client ID':['11'],
    'First Name':['Francesco'],
    'Last Name':['Lo Gullo'],
    'Annual Salary [$/year]':[40000]
    }
bank_df_me=pd.DataFrame(me,columns= ['Bank Client ID','First Name','Last Name','Annual Salary [$/year]'])
bank_df_all_plus_me=pd.concat([bank_df_all,bank_df_me])
print(bank_df_all_plus_me)