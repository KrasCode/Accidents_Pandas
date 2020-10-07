import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/atlantm.xls', decimal=',',
                 thousands = " ",
                 dtype=str, usecols = lambda column : column not in ["Акція"])
df.columns = ['vcode', 'vendor', 'name', 'psc', 'price']

df = df.loc[df['vcode'] != '']
df = df.loc[~df['psc'].isin(['0', ''])]

df["psc"] = pd.to_numeric(df["psc"]).astype(int)
df["price"] = pd.to_numeric(df["price"])
df = df.loc[df['psc'] != 0]
print(df.info())
# print(df.head())

df.to_csv('atlant.csv', sep=';', index=False, decimal=',')