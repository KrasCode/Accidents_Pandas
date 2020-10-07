import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/0109/LandRover092020.xlsx', decimal=',', dtype=str,
                   usecols = lambda column : column not in ["Gewicht", "Land"])
df.columns = ['vcode', 'descr', 'price', 'psc']
df['psc'] = 5
df['price']=df['price'].fillna('0')

df["price"] = pd.to_numeric(df["price"])

df = df.loc[df['price'] != 0]
print(df.info())
print(df.head())
df.to_csv('landger.csv', sep=';', index=False, decimal=',')