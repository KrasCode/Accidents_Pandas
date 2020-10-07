import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

df = pd.read_excel('BGA.xlsx', dtype=str, skip_blank_lines=True,
                   usecols=lambda column: column not in ["PG", "Reference Description"])

print(df.info())
print(df.head())

source_col_loc = df.columns.get_loc('AE') # column position starts from 0

df['art'] = df.iloc[:,source_col_loc+1:source_col_loc+91].apply(
    lambda x: ", ".join(x.dropna().astype(str)), axis=1)
df.drop(df.columns[1:92], axis=1, inplace=True)
columnsTitles=["art", "BGA REFERENCE"]
df=df.reindex(columns=columnsTitles)

df = \
(df.set_index(df.columns.drop('art',1).tolist())
   .art.str.split(', ', expand=True)
   .stack()
   .reset_index()
   .rename(columns={0:'art'})
   .loc[:, df.columns]
)
df['art'] = df['art'].str.strip()
df = df.loc[df['art'] != df['BGA REFERENCE']]
df.insert(0, 'vendor', '', True)
df.insert(2, 'cross_vendor', '', True)
# print(df.info())
print(df.head())
# print(len(df['art'][4]))
# print(df['art'][1])


df.to_excel('bga_cross.xlsx', index=False)