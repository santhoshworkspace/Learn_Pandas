import pandas as pd
df=pd.read_csv("New_Weather.csv",skiprows=1,names=["EST","Temperature","DewPoint"],na_values=["not_found"])
print(df)
df=pd.read_csv("New_Weather.csv",skiprows=1,names=["EST","Temperature","DewPoint"],na_values={'DewPoint':["no"]})
print(df)
df.to_csv("developed.csv",index=False)
df=pd.read_csv("New_Weather.csv",header=1,names=["Date","Weather","Weather_point"],na_values={'DewPoint':["no"]})
print(df)
getColumns=df.columns
print(getColumns)
df.to_csv("developed.csv",header=False)
df.columns=["Date","Weather","Weather_point"]
df.to_csv("developed.csv",index=False)
