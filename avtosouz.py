import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/avtosouz.xls', decimal=',', dtype=str,
                   usecols = lambda column : column not in ["Резерв", "Віддалений склад*"])
df.columns = ['vcode', 'vendor', 'name', 'psc', 'price']
df = df.loc[~df['vendor'].isin(['Tire', 'Oil'])]
df["price"] = pd.to_numeric(df["price"])
df["psc"] = pd.to_numeric(df["psc"])
df['psc'] = df['psc'].astype(int)
#
df = df.loc[df['price'] != 0]
df = df.loc[df['psc'] != 0]
print(df.info())
print(df.head())
df.to_csv('avtosouz.csv', sep=';', index=False, decimal=',', float_format = '%.2f')