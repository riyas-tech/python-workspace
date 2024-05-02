import pandas as pd
from datetime import datetime

data = ['2023-01-20', '2023-04-27', '2023-06-15']
my_series = pd.Series(data)
print(my_series)

my_series = pd.to_datetime(my_series)
print(my_series)

print(my_series.dt.year)
print(my_series.dt.month)
print(my_series.dt.day)


print(datetime.strptime('25/11/2022', '%d/%m/%Y'))