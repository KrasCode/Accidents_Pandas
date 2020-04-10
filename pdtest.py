import pandas as pd
import numpy as np
import calendar
import plotly.graph_objs as go

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)
df = pd.read_csv('accidents_2017.csv')
#df.replace('Unknown',np.nan, inplace=True)  колонки с Unknown оказалтсь не нужны
#print(df.isnull().sum().any())


df.drop(['District Name','Neighborhood Name','Part of the day'], axis=1, inplace=True)
df.rename(columns=lambda x: x.replace(' ', '_').lower(), inplace=True)
df['year'] = np.repeat(2017, df.shape[0])
month_to_int = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
df['month'].replace(month_to_int, inplace=True)
df['date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

# Извлекаем год
#df['date'].dt.year
# Извлекаем месяц
#df['date'].dt.month
# Извлекаем день
#df['date'].dt.day
# Извлекаем час
#df['date'].dt.hour
# Извлекаем день недели
#df['date'].dt.dayofweek

df.drop(['year','month','day', 'hour', 'weekday', 'street'], axis=1, inplace=True)
df.id = df.id.apply(lambda x: x.strip())
df.set_index('id', inplace=True)
#df[df.duplicated()]
df.drop_duplicates(inplace=True)

#df.info()
print(df.head())
print('Total number of accidents in 2017 :{}'.format(df.shape[0]))
accidents_month = df.groupby(df['date'].dt.month)['date'].count()
accidents_month.index = [calendar.month_name[x] for x in range(1, 13)]
t_accident = accidents_month.tolist()
t_month = list(accidents_month.index)

trace = go.Bar(
    y=t_accident,
    x=t_month,
    text=t_accident,
    textposition='inside',
    marker_color=['red']*12
)

layout = go.Layout(
    title_text='Accidents in Barcelona in 2017',
    xaxis_title='Month',
    yaxis_title='Accidents'
)

fig = go.Figure(data=trace, layout=layout)
#fig.show()

accidents_day = df.groupby(df['date'].dt.dayofweek)['date'].count()
accidents_day.index = [calendar.day_name[x] for x in range(0, 7)]
t_accident_week = accidents_day.tolist()
#t_day = list(accidents_day.index)

trace1 = go.Bar(
    x=accidents_day.index,
    y=t_accident_week,
    text=t_accident_week,
    textposition='inside',
    marker_color=['blue']*7
)
layout1 = go.Layout(
    title_text='Accidents in Barcelona in 2017',
    xaxis_title='Day of the week',
    yaxis_title='Accidents'
)

fig1 = go.Figure(data=trace1, layout=layout1)
#fig1.show()

accidents = df.groupby(df['date'].dt.date)['date'].count()
t_accid = accidents.tolist()
trace2 = go.Scatter(
    y=t_accid,
    x=accidents.index,
    mode='lines',
    name='Accid_in_days'
)
layout2 = go.Layout(
    title='Accidents in Barcelona in 2017',
    xaxis_title='Dates',
    yaxis_title='Accidents'
)
fig2 = go.Figure(data=trace2, layout=layout2)
fig2.show()

#print(accidents.index)







