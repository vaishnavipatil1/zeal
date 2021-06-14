import pandas as pd
data = pd.read_csv("../input/weather-dataset/weatherHistory.csv")
data
data.head()
data.index
data.shape
data.columns
data.dtypes
data[' _windchillm'].unique()
data.nunique()
data.count()
data.info()
data.head(2)
data.nunique()
data['datetime_utc'].nunique()
data['datetime_utc'].unique() #answer
data.head(2)
data[data.	datetime_utc == '19961101-11:00']
data.isnull().sum()
data.notnull().sum()
data.head(2)
data.rename(columns = {'_conds':'nice fog'})
