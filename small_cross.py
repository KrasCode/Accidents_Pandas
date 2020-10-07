import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_csv('KSP.csv', sep=';', decimal=',', thousands = " ", encoding='ISO-8859-1',
                 dtype=str, usecols = lambda column : column not in ["name"])
df = df.loc[df['art'] != df['cross_art']]
df = df.loc[df['art'] != '']
columnsTitles=["vendor", "art", "cross_vendor", "cross_art"]
df=df.reindex(columns=columnsTitles)
print(df.info())
print(df.head())

df.to_excel('ksp_cross.xlsx', index=False)