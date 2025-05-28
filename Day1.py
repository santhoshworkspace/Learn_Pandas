import pandas as pd
df=pd.read_csv('./weather_jan_2016.csv')
print(df)
Temperature=df['Temperature']
print("Temperature",Temperature)