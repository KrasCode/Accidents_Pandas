import pandas as pd
import xlrd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)


df = pd.read_excel('C:/Users/Admin/Desktop/iparts/1509/avtonovad.xls', decimal=',',
                 thousands = " ",
                 dtype=str, usecols = lambda column : column not in ["Цена Розница"])
df.columns = ['Descr', 'fcode', 'vcode', 'vendor', 'name', 'psc', 'price']
df = df.loc[~df['vendor'].isin(['АЛЯSКА', 'ДОСТАВКА', 'Тосол-Синтез', 'ENERGY RELEASE', '!Avtohimia', '!Reklama',
                                '5277', 'Vip Oil', 'Аксессуары', 'СУВЕНИРЫ', 'ТОЧКА ОПОРИ', 'Дорожная карта',
                                'Цитрон', 'Кама Ойл', 'Руслан-комплект', 'АТР-Холдинг', 'КЕДР', 'КОЛАН',
                                'ПЕКАР', 'Ульяновский автомобильный завод', 'АДС, г.Ульяновск',
                                'СОАТЭ', 'Аурида', 'Авто-мастер', 'ТАРА', 'Сфера ЧП', 'ОСВАР', 'НЕВСКИЙ ФИЛЬТР',
                                'УМЗ Торговый Дом ООО', 'Мотордеталь', 'ШААЗ', 'Автодеталь-сервис ОАО', 'МФК',
                                'Агринол', 'Начало', 'Antonio Masiero'])]
df = df.loc[df['vcode'] != '']
df = df.loc[~df['psc'].isin(['0', ''])]

df["psc"] = pd.to_numeric(df["psc"]).astype(int)
df["price"] = pd.to_numeric(df["price"])
df = df.loc[df['psc'] != 0]
print(df.info())
# print(df.head())

df.to_csv('avtonovad.csv', sep=';', index=False, decimal=',')