import pandas as pd
import xlrd
import openpyxl

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

df = pd.read_excel('Cross_Polcar.xlsx', nrows=5, dtype=str,
                   usecols = lambda column : column not in ["vendor"])

print(df.info())
print(df.head())

df = \
(df.set_index(df.columns.drop('art', 1).tolist())
   .art.str.split(', ', expand=True)
   .stack()
   .reset_index()
   .rename(columns={0:'art'})
   .loc[:, df.columns]
)
df.insert(0, 'vendor', '', True)
print(df.head())
# print(df['art'][2][2])


# df.to_excel('cross_pol.xlsx', index=False)