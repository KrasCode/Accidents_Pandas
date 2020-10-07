import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/D1.xlsx', decimal='.', dtype=str)
df.columns = ['vendor', 'fcode', 'name', 'price', 'psc', 'psc2', 'psc3', 'psc4', 'psc5', 'psc6', 'psc7', 'vcode']
df['name'] = df['name'].str.strip()
df['psc'] = df['psc'].str.strip('>')
df['psc2'] = df['psc2'].str.strip('>')
df['psc3'] = df['psc3'].str.strip('>')
df['psc4'] = df['psc4'].str.strip('>')
df['psc5'] = df['psc5'].str.strip('>')
df['psc6'] = df['psc6'].str.strip('>')
df['psc7'] = df['psc7'].str.strip('>')
df['vendor']=df['vendor'].fillna('0')
df['vcode']=df['vcode'].fillna('0')
df['vendor'] = df['vendor'].str.replace('KS', 'KOLBENSCHMIDT')
df = df.loc[~df['vendor'].isin(['0'])]
df = df.loc[df['vcode'] != '0']

df["price"] = pd.to_numeric(df["price"])
df["psc"] = pd.to_numeric(df["psc"])
df["psc2"] = pd.to_numeric(df["psc2"])
df["psc3"] = pd.to_numeric(df["psc3"])
df["psc4"] = pd.to_numeric(df["psc4"])
df["psc5"] = pd.to_numeric(df["psc5"])
df["psc6"] = pd.to_numeric(df["psc6"])
df["psc7"] = pd.to_numeric(df["psc7"])
df['stock1']=df[['psc', 'psc2']].sum(axis=1)
df['stock2']=df[['psc3', 'psc4', 'psc5', 'psc6', 'psc7']].sum(axis=1)

df1 = df[['vendor', 'name', 'price', 'stock2', 'vcode']]
df.drop(columns=['fcode', 'psc','psc2','psc3','psc4', 'psc5', 'psc6', 'psc7', 'stock2'], inplace=True)
df = df[['vendor', 'name', 'price', 'stock1', 'vcode']]
df['stock1'] = df['stock1'].astype(int)
df1['stock2'] = df1['stock2'].astype(int)
df1 = df1.loc[df1['stock2'] != 0]
df = df.loc[df['stock1'] != 0]
print(df.info())
print(df.head())
print(df1.head())
df.to_csv('avtotech.csv', sep=';', index=False, decimal=',')
df1.to_csv('avtotechregion.csv', sep=';', index=False, decimal=',')
