#Exercise:
#Using "bank_client_df" DataFrame, select only high networth individuals with minimum $5000 
#What is the combined networth for all customers with 5000+ networth?
import pandas as pd
bank_client_df= pd.DataFrame({"Bank Vlient ID":[111,222,333,444],
                             "Bank Client Name":["Chanel","Steve","Mitch","Ryan"],
                             'Net Worth[$]':[3500,29000,10000,2000],
                             'Years with bank':[3,4,9,5]})
df_high_networth= bank_client_df[ bank_client_df['Net Worth[$]']>=5000]
print(df_high_networth)
combined=df_high_networth['Net Worth[$]'].sum()
print('combined networth is: ',combined)