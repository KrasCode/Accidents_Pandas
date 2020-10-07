import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/price_polcar_full.xlsx', decimal='.', dtype=str,
                   usecols = lambda column : column not in ["oem"])

# df['stock']=df['stock'].fillna('0')
df['name']=df['name'].fillna('')
df['description']=df['description'].fillna('')
# df = df.loc[df['stock'].isin(['1', '2', '3', '4', '5'])]
# df = df.loc[~df['stock'].isin(['0'])]
#
df["price"] = pd.to_numeric(df["price"])
df["stock"] = pd.to_numeric(df["stock"])
#
df = df.loc[df['price'] != 0]
df = df.loc[df['stock'] != 0]
print(df.info())
print(df.head())
df.to_csv('polcar.csv', sep=';', index=False, decimal=',')