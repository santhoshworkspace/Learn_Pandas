import pandas as pd
df=pd.read_csv('./weather_jan_2016.csv')
print(df)
print(df['Temperature'])
print(df['EST'][df['Events']=='Rain'])
df.fillna("0",inplace=True)
print(df)
print("hai:",df.shape)
rows,columns=df.shape
print(rows,columns)
print(df.head(10))
print(df.tail(10))
print(df[3:7])
find=df[df.Temperature>=40]
find_isRain =df[df.Events=="Rain"]
print(find)
print(find_isRain)
find_dateTempHigh = df['EST'] [df['Temperature'] == df['Temperature'].max()]
print(find_dateTempHigh)
set_indexDay=df.set_index('EST',inplace=True)
print(set_indexDay)
print(df)
print(df.loc['1/4/2016'])