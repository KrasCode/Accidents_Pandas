import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/ksp.xlsx', decimal=',', dtype=str)
df.columns = ['name', 'vcode', 'fcode', 'vendor', 'psc', 'price']

df['price']=df['price'].fillna('0')

# df = df.loc[~df['vendor'].isin(['Итого', 'Avtohimia'])]
df['fcode']=df['fcode'].fillna('')

df["price"] = pd.to_numeric(df["price"])
df["psc"] = pd.to_numeric(df["psc"])
df = df[~df.name.str.contains("Ароматизатор")]
df = df[~df.name.str.contains("Освеж.")]
df = df[~df.name.str.contains("БУ")]
df = df[~df.name.str.contains("дефект")]
df = df[~df.name.str.contains("Дефект")]
df = df[~df.vcode.str.contains("дефект")]
df = df[~df.fcode.str.contains("дефект")]
df = df[~df.vcode.str.contains("REF")]
df = df[~df.fcode.str.contains("REF")]
df = df[~df.vcode.str.contains("ref")]
df = df[~df.fcode.str.contains("ref")]


df = df.loc[df['psc'] != 0]
df = df.loc[df['price'] != 0]
print(df.info())
print(df.head())
df.to_csv('ksp.csv', sep=';', index=False, decimal=',')