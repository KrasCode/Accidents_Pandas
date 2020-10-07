import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/elit.xlsx', decimal='.', dtype=str)
df.columns = ['fcode', 'vcode', 'vendor', 'name', 'Descr', 'price', 'psc', 'psc2', 'psc3', 'psc4', 'psc5']
df['name'] = df['name'].str.strip()
df['Descr'] = df['Descr'].str.strip()
df['psc'] = df['psc'].str.strip('+')
df['psc2'] = df['psc2'].str.strip('+')
df['psc3'] = df['psc3'].str.strip('+')
df['psc4'] = df['psc4'].str.strip('+')
df['psc5'] = df['psc5'].str.strip('+')
df['vendor']=df['vendor'].fillna('0')
df['vcode']=df['vcode'].fillna('0')
df['vendor'] = df['vendor'].str.replace('KS', 'KOLBENSCHMIDT')
df = df.loc[~df['vendor'].isin(['0', 'YR SA-50327', 'Aromacar быт', 'CASTROL', 'BIZOL', 'CASTROL', 'LIQUI MOLY',
                                'MOBIL', 'Aroma Car', 'VATOIL', 'AROMA', 'AROMACAR', 'VatOil'])]
df = df.loc[df['vcode'] != '0']

df["price"] = pd.to_numeric(df["price"])
df["psc"] = pd.to_numeric(df["psc"])
df["psc2"] = pd.to_numeric(df["psc2"])
df["psc3"] = pd.to_numeric(df["psc3"])
df["psc4"] = pd.to_numeric(df["psc4"])
df["psc5"] = pd.to_numeric(df["psc5"])
df['stock']=df[['psc', 'psc2', 'psc3', 'psc4']].sum(axis=1)

df1 = df[['fcode', 'vcode', 'vendor', 'name', 'Descr', 'price', 'psc5']]
df.drop(columns=['psc','psc2','psc3','psc4', 'psc5'], inplace=True)
df1 = df1.loc[df1['psc5'] != 0]
df = df.loc[df['stock'] != 0]
# print(df.info())
print(df.head())
# print(df1.head())
df.to_csv('C:/Users/Admin/Desktop/iparts/1509/elitkiev.csv', sep=';', index=False, decimal=',')
df1.to_csv('C:/Users/Admin/Desktop/iparts/1509/elitregion.csv', sep=';', index=False, decimal=',')
