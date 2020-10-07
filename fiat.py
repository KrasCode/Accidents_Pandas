import pandas as pd


# desired_width = 320
# pd.set_option('display.width', desired_width)
# pd.set_option('display.max_columns', None)

cifra = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
df = pd.read_csv('fiat.csv', sep=';', decimal=',',
                 dtype={'Code':'unicode', 'Descr':'unicode'},
                 usecols = lambda column : column not in ["Ersetzung", "LC"])

df = df[df['RG'].isin(cifra)]
df["Preise"] = pd.to_numeric(df["Preise"])
df["RG"] = pd.to_numeric(df["RG"])
print(df.info())
print(df.head())

df.to_csv('fiat_new.csv', sep=';', index=False, decimal=',')