import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/0109/VAG092020.xlsx', decimal=',', dtype=str,
                   usecols = lambda column : column not in ["Gewicht", "Land"])
df.columns = ['vcode', 'descr', 'price', 'psc']
df['psc'] = 5
df['price']=df['price'].fillna('0')

# df = df.loc[~df['vendor'].isin(['Итого', 'Avtohimia'])]
# df['fcode']=df['fcode'].fillna('')

df["price"] = pd.to_numeric(df["price"])
# df["psc"] = pd.to_numeric(df["psc"])

# df = df.loc[df['psc'] != 0]
df = df.loc[df['price'] != 0]
print(df.info())
print(df.head())
df.to_csv('vagger.csv', sep=';', index=False, decimal=',')