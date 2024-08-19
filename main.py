import pandas as pd 

df = pd.read_csv('sumo_since_1957.csv')
print(df.head())


print('最も多くの力士を輩出した出身地はどこですか？')

#力士の出身地カラムを抽出。
df_Shusshin=df[["Shusshin"]] 

#print(df_Shusshin.head())

# カラムの値をカウントし、辞書型に変換する。
d = df_Shusshin.value_counts().to_dict()  
keys = [k for k, v in d.items() if v == 1449]

# タプルから要素を取り出して新しいリストを作成
aomori_list = [item[0] for item in keys]

print(f"力士輩出、最多出身地は{aomori_list[0]}です。")


print('片男波で練習している力士は誰ですか?')

#まず、データフレームから部屋名カラムからkataonamiを抽出したデータフレームを作成する。
df_Kataonami= df[df['Heya'] == 'Kataonami']

#df_Kataonamiからに所属する力士の名前を取り出す。

df_meuber_kataonami = df_Kataonami['Rikishi'].unique()
print(df_meuber_kataonami.shape)

rikishi_count = 0
for i in df_meuber_kataonami:
    rikishi_count += 1
    print(i)
    
print(f"片男波所属の力士は上記の{rikishi_count}にんです。")    






   

