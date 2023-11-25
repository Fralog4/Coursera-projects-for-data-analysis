#Exercise: 
#Define a function that triples the stock prices and adds $200
#Apply the function to the DataFrame
#Calculate the updated total networth of all clients combined
import pandas as pd
bank_client_df= pd.DataFrame({"Bank Vlient ID":[111,222,333,444],
                             "Bank Client Name":["Chanel","Steve","Mitch","Ryan"],
                             'Net Worth[$]':[3500,29000,10000,2000],
                             'Years with bank':[3,4,9,5]})
def networth_update(balance):
    return balance*3+200
result=bank_client_df['Net Worth[$]'].apply(networth_update)
print(result)
print('the total networth is:',result.sum())