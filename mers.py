import pandas as pd


# desired_width = 320
# pd.set_option('display.width', desired_width)
# pd.set_option('display.max_columns', None)

# cifra = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
df = pd.read_csv('mers.csv', sep=';', decimal=',', thousands = " ",
                 dtype={'Product':'unicode', 'Description':'unicode'},
                 usecols = lambda column : column not in ["#", "Weight", "Discount Group", "Price comment"])

df.rename(columns={'Price, euro': 'Price'}, inplace=True)
df['Pst'] = 1
print(df.info())
print(df.head())
# print(type(df['Price'][20]))

df.to_csv('mers_new.csv', sep=';', index=False, decimal=',')