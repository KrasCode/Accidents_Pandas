import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('1509/inductor.xlsx', decimal=',', dtype=str)
df.columns = ['vcode', 'name', 'vendor', 'price', 'psc', 'psc2']

df['psc']=df['psc'].fillna('0')
df['psc2']=df['psc2'].fillna('0')

df = df.loc[~df['vendor'].isin(['AREON', 'JB GERMAN OIL', 'TASOTTI', 'Agrinol', 'EkoKemika', 'Glasurit',
                                'HENKEL', 'Honeywell', 'JOHNSON', 'JVC', 'KARCHER', 'KATRIN', 'KochChemie',
                                'Lesta', 'LLumar', 'B-Style', 'COLAD', 'DOLONI', 'DuPont', 'Mirka', 'ORIUM',
                                'NORTON', 'QuickLine', 'Solid', 'STANDARTPLAST', 'Tectyl', 'TESA', 'Kimberly-Clark'])]
df = df.loc[~df['vcode'].isin(['хетчбек', 'УСИЛЕННЫЙ', '49', '111', '0,25', '0,5', '0.5 (77,0)',
                               'вольтметр', 'сальники', 'цоколь больш.', 'цоколь малый', 'черный'])]
df['vcode'] = df['vcode'].str.replace(',', '')
df['psc'] = df['psc'].str.replace('+', '1')
df['psc2'] = df['psc2'].str.replace('+', '1')
df["price"] = pd.to_numeric(df["price"])
df["psc"] = pd.to_numeric(df["psc"])
df["psc2"] = pd.to_numeric(df["psc2"])
df['vendor'] = df['vendor'].str.replace('Ks', 'KOLBENSCHMIDT')

df1 = df[['vcode', 'name', 'vendor', 'price', 'psc2']]
df.drop(columns=['psc2'], inplace=True)
df1 = df1.loc[df1['psc2'] != 0]
df = df.loc[df['psc'] != 0]
print(df1.info())
print(df.head())
print(df1.head())
df.to_csv('1509/inductor.csv', sep=';', index=False, decimal=',')
df1.to_csv('1509/inductor1d.csv', sep=';', index=False, decimal=',')
