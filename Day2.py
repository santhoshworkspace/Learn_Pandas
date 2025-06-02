from unittest.mock import inplace

import pandas as pd

df = pd.read_csv("weather_jan_2016.csv")
print(df)

df = pd.read_excel("weather_data.xlsx","Sheet1")
print(df)

weather_data = {
    'Data' : ['2025-06-01','2025-06-02','2025-06-03'],
    'Temperature':[32,33,34],
    'Event':['Sunny','Cloudy',"Rain"]
}
df =pd.DataFrame(weather_data)
print(df)

weather_data = [('2025-06-01',32,'Sunny'),('2025-06-02',33,'Cloudy'),
                ('2025-06-03',34,"Rain")]
df = pd.DataFrame(weather_data,columns=["Data",'Temperature','Event'])
print("List : \n",df)

weather_data=[{"Data":'2025-06-01','Temperature':32,'Event':'Sunny'},
              {"Data":'2025-06-02','Temperature':33,'Event':'Cloudy'},
              {"Data":'2025-06-03','Temperature':34,'Event':'Rain'}]
pf=pd.DataFrame(weather_data)
print("Another Way :\n",pf)

pf =pd.read_csv("New_Weather.csv",skiprows=1)
print(pf)

pf =pd.read_csv("New_Weather.csv",header=1,names=["EST","Temperature","DewPoint"])
print(pf)

pf =pd.read_csv("New_Weather.csv",nrows=1)
print(pf)

