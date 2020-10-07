import pandas as pd


# desired_width = 320
# pd.set_option('display.width', desired_width)
# pd.set_option('display.max_columns', None)

df = pd.read_csv('ford.csv', sep=';', decimal=',', thousands = " ",
                 dtype={'Product':'unicode', 'Description':'unicode'},
                 usecols = lambda column : column not in ["#", "Weight", "Discount Group", "Price comment"])

df.rename(columns={'Price, euro': 'Price'}, inplace=True)
df['Pst'] = 1
print(df.info())
print(df.head())
# print(type(df['Price'][20]))

df.to_csv('ford_new.csv', sep=';', index=False, decimal=',')