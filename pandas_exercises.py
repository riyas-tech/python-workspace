import numpy as np
import pandas as pd
from numpy.random import randn

labels = ['a', 'b', 'c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a' :10, 'b' : 20, 'c' : 30}
print(pd.Series(data = my_data, index = labels))
print(pd.Series(data = arr, index = labels))
print(pd.Series(d))

series_1 = pd.Series([1,2,3,4], ['USA', 'India', 'Canada', 'UK'])
print (series_1)

# Get information from series

print(series_1['USA'])

#-----------------------------------------------------------------------------------------------------------------#

# DataFrame
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z'])
print(df)

print(df.loc['A']['Z'])

df_1 =  df[df['W'] > 0]
print(df_1)


d = {'A' :[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C' :[1,2,3]}
df = pd.DataFrame(d)
print(df)

df_missing = df.dropna()
print(df_missing)

df_fillna = df.fillna(value='FILL Value')
print(df_fillna)

#---------------------------------------------------#

data = {
    'company' : ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'person' : ['riyas', 'sam', 'Amy',  'John', 'carl', 'sarah'],
    'sales' : [200,120,340,124,243,350]
}

df = pd.DataFrame(data)
print(df)

df_group_by = df.groupby('company')
print(df_group_by)

print(df_group_by.mean('sales'))
print(df_group_by.sum('sales'))

print(df_group_by.sum('sales').loc['FB'])
print(df_group_by.count())

