import pandas as pd
df=pd.read_csv('./weather_jan_2016.csv')
print(df)
print(df['Temperature'])
print(df['EST'][df['Events']=='Rain'])
df.fillna("0",inplace=True)
print(df)
print(df.shape)
rows,columns=df.shape
print(rows,columns)
print(df.head(10))
print(df.tail(10))
print(df[3:7])