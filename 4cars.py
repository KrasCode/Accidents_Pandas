import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/sklad.xlsx', decimal='.', dtype=str,
                   usecols = lambda column : column not in ["term"])
df2 = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/sklad2.xlsx', decimal='.', dtype=str,
                   usecols = lambda column : column not in ["term"])
# df3 = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/Signeda.xlsx', decimal='.', dtype=str,
#                    usecols = lambda column : column not in ["term"])

df["price"] = pd.to_numeric(df["price"])
df["stock"] = pd.to_numeric(df["stock"])
df2["price"] = pd.to_numeric(df2["price"])
df2["stock"] = pd.to_numeric(df2["stock"])
# df3["price"] = pd.to_numeric(df3["price"])
# df3["stock"] = pd.to_numeric(df3["stock"])
df = df.loc[~df['brand'].isin(['deleted'])]
df2 = df2.loc[~df2['brand'].isin(['deleted'])]
# df3 = df3.loc[~df3['brand'].isin(['deleted'])]

print(df.info())
print(df.head())
print(df2.info())
print(df2.head())

df.to_csv('4cars.csv', sep=';', index=False, decimal=',')
df2.to_csv('4cars2.csv', sep=';', index=False, decimal=',')
# df3.to_csv('signeda.csv', sep=';', index=False, decimal=',')