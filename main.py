import pandas as pd 

df = pd.read_csv('sumo_since_1957.csv')
print(df.head())


print('最も多くの力士を輩出した出身地はどこですか？')
df_Shusshin=df[["Shusshin"]] 

#print(df_Shusshin.head())

#df_Shusshin.value_counts()

d = df_Shusshin.value_counts().to_dict()  
keys = [k for k, v in d.items() if v == 1449]

# タプルから要素を取り出して新しいリストを作成
aomori_list = [item[0] for item in keys]

print(f"力士輩出、最多出身地は{aomori_list[0]}です。")







   

