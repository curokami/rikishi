import pandas as pd 

df = pd.read_csv('sumo_since_1957.csv')
print(df.head())

df_Shusshin=df[["Shusshin"]] 

print(df_Shusshin.head())


   

