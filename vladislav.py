import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/Admin/Desktop/iparts/1509/vladislav.csv', sep=';', decimal=',', thousands = " ",
                  dtype=str,
                 usecols = lambda column : column not in ["7", '1', '10'])
df.columns = ['fcode', 'vendor', 'descr', 'vcode', 'price', 'psc', 'name']

df = df.loc[~df['vendor'].isin(['УЗЭМИК (РОССИЯ)', 'БРЕНДЫ ИРБИС', 'DANNEV', 'UA', 'ВАМП', 'E-TEC',
                                'ИТАЛИЯ', 'А-МЕГА', 'КИТАЙ'])]
df['psc'] = df['psc'].str.strip('>')
df['price'] = df['price'].str.strip(' ')
df['price'] = df['price'].str.replace(',', '.')
df['price'] = df['price'].str.replace(' ', '')
df["price"] = pd.to_numeric(df["price"])
df["psc"] = pd.to_numeric(df["psc"])
df = df.loc[df['psc'] != 0]
df = df.loc[df['price'] != 0]
df['vcode']=df['vcode'].fillna('0')
df = df.loc[df['vcode'] != '0']
df['vcode'] = df['vcode'].str.lstrip('.')
print(df.info())
print(df.head())

df.to_csv('vlad.csv', sep=';', index=False, decimal=',')
# df.to_excel('vlad.xlsx', index=False)