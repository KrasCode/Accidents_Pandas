import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/avtotrade.xls', decimal=',', dtype=str)
df.columns = ['vendor', 'vcode',  'descr', 'name', 'price', 'psc']
df['vendor'] = df['vendor'].str.replace('KS', 'KOLBENSCHMIDT')
df['price']=df['price'].fillna('0')

df = df.loc[~df['vendor'].isin(['Итого', 'Avtohimia'])]
df['descr']=df['descr'].fillna('')

df["price"] = pd.to_numeric(df["price"])
df["psc"] = pd.to_numeric(df["psc"])

df = df.loc[df['psc'] != 0]
df = df.loc[df['price'] != 0]
print(df.info())
print(df.head())
df.to_csv('autotrade.csv', sep=';', index=False, decimal=',')