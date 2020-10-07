import pandas as pd
import xlrd
import openpyxl

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

df = pd.read_excel('OE.xlsx', dtype=str)
df['OE'] = df['OE'].str.strip()
# print(df.info())
# print(df.head())

df = \
(df.set_index(df.columns.drop('OE', 1).tolist())
   .OE.str.split('  ', expand=True)
   .stack()
   .reset_index()
   .rename(columns={0:'OE'})
   .loc[:, df.columns]
)

columnsTitles=["OE", "OE Germany"]
df=df.reindex(columns=columnsTitles)
df.insert(0, 'vendor', '', True)
df.insert(2, 'cross_vendor', '', True)
print(df.info())
print(df.head())
# print(df['art'][2][2])


df.to_excel('cross_oe1.xlsx', index=False)