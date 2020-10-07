import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

dfb = pd.read_excel('C:/Users/Admin/Desktop/iparts/listban.xlsx',  dtype=str)
dfb.drop_duplicates(inplace=True)
m = dfb['vendor'].tolist()
musor = ['<>', '0.NN', 'Автонормаль ОАО, г. Белебей']
m += musor
print(m)
df = pd.read_excel('C:/Users/Admin/Desktop/iparts/1008/omega.xlsx', decimal=',', dtype=str, sheet_name='PriceList',
                   usecols = lambda column : column not in ["Вес", "NORM", "Харьков (шины)", "Киев (шины)"])
df.columns = ['vendor', 'fcode', 'vcode', 'name', 'descr', 'price', 'r1', 'k1', 'r2', 'r3', 'r4', 'r5', 'r6'
              , 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15', 'r16', 'r17', 'r18', 'r19']
df.drop([0], inplace=True)
df['descr']=df['descr'].fillna('')

# df['psc']=df['psc'].fillna('0')
# df['psc2']=df['psc2'].fillna('0')
df['vendor'] = df['vendor'].str.replace('1.', '')
df = df.loc[~df['vendor'].isin(m)]

df['r1'] = df['r1'].str.replace('>', '')
df['r2'] = df['r2'].str.replace('>', '')
df['r3'] = df['r3'].str.replace('>', '')
df['r4'] = df['r4'].str.replace('>', '')
df['r5'] = df['r5'].str.replace('>', '')
df['r6'] = df['r6'].str.replace('>', '')
df['r7'] = df['r7'].str.replace('>', '')
df['r8'] = df['r8'].str.replace('>', '')
df['r9'] = df['r9'].str.replace('>', '')
df['r10'] = df['r10'].str.replace('>', '')
df['r11'] = df['r11'].str.replace('>', '')
df['r12'] = df['r12'].str.replace('>', '')
df['r13'] = df['r13'].str.replace('>', '')
df['r14'] = df['r14'].str.replace('>', '')
df['r15'] = df['r15'].str.replace('>', '')
df['r16'] = df['r16'].str.replace('>', '')
df['r17'] = df['r17'].str.replace('>', '')
df['r18'] = df['r18'].str.replace('>', '')
df['r19'] = df['r19'].str.replace('>', '')
df['k1'] = df['k1'].str.replace('>', '')
df['vcode']=df['vcode'].fillna('0')
df['vendor']=df['vendor'].fillna('0')
df = df.loc[~df['vcode'].isin(['0', ''])]
df = df.loc[~df['vendor'].isin(['0', ''])]
df[["price", "r1", 'k1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15',
    'r16', 'r17', 'r18', 'r19']] = df[["price", "r1", 'k1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10',
                                       'r11', 'r12', 'r13', 'r14', 'r15', 'r16', 'r17',
                                       'r18', 'r19']].apply(pd.to_numeric)
dfk = df[['vendor', 'fcode', 'vcode', 'name', 'descr', 'price', 'k1']]
df.drop(columns=['k1'], inplace=True)
df['psc'] = df[['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15',
    'r16', 'r17', 'r18', 'r19']].sum(axis=1)
df.drop(columns=['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15',
    'r16', 'r17', 'r18', 'r19'], inplace=True)

dfk = dfk.loc[dfk['k1'] != 0]
df = df.loc[df['psc'] != 0]

print(df.info())
print(df.head())
print(dfk.head())

df.to_csv('omegareg.csv', sep=';', index=False, decimal=',')
dfk.to_csv('omega.csv', sep=';', index=False, decimal=',')
