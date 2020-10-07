import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

df = pd.read_excel('C:/Users/Admin/Desktop/iparts/0109/export_stok.xlsx', decimal=',',
                 dtype=str, usecols = [0, 1, 2, 3, 4])
df2 = pd.read_excel('C:/Users/Admin/Desktop/iparts/0109/export_aesf.xlsx', decimal=',',
                 dtype=str, usecols = [0, 1, 2, 3, 4])
df.columns = ['vendor', 'vcode', 'name', 'psc', 'price']
# df["price"] = pd.to_numeric(df["price"]).map('{:,.2f}'.format)
# df['price'] = df['price'].str.replace(',', '')
df["price"] = pd.to_numeric(df["price"])
df["psc"] = pd.to_numeric(df["psc"])

df2.columns = ['vendor', 'vcode', 'name', 'psc', 'price']
df2["price"] = pd.to_numeric(df2["price"])
df2["psc"] = pd.to_numeric(df2["psc"])
print(df.info())
print(df.head())
df.to_csv('tehno_odd.csv', sep=';', index=False, decimal=',', float_format = '%.2f')
df2.to_csv('tehno_arab.csv', sep=';', index=False, decimal=',', float_format = '%.2f')