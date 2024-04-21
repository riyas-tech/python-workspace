import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import hvplot.pandas

df = pd.read_csv("D:\\pyspark-workspace\\python-workspace\\police_project.csv")
print(df.head())
print(df.info())

# #   Column              Non-Null Count  Dtype
# ---  ------              --------------  -----
#  0   stop_date           91741 non-null  object
#  1   stop_time           91741 non-null  object
#  2   county_name         0 non-null      float64
#  3   driver_gender       86406 non-null  object
#  4   driver_age_raw      86414 non-null  float64
#  5   driver_age          86120 non-null  float64
#  6   driver_race         86408 non-null  object
#  7   violation_raw       86408 non-null  object
#  8   violation           86408 non-null  object
#  9   search_conducted    91741 non-null  bool
#  10  search_type         3196 non-null   object
#  11  stop_outcome        86408 non-null  object
#  12  is_arrested         86408 non-null  object
#  13  stop_duration       86408 non-null  object
#  14  drugs_related_stop  91741 non-null  bool
# dtypes: bool(2), float64(3), object(10)

print(df.describe())

# Remove the column that only contains missing values 
# county_name . All the data is missing 

for column in df.columns:
    missing = df[column].isna().sum() / df.shape[0]
    print(f"{column:{20}}: ==========================>{missing * 100:.2f}%")

# for column in df.columns:: This iterates over each column in the DataFrame df.\
# missing = df[column].isna().sum() / df.shape[0]: For each column, 
# it calculates the percentage of missing values. It does this by counting the number of missing values in the column (df[column].isna().sum()) 
# and dividing it by the total number of rows in the DataFrame (df.shape[0]). This gives the proportion of missing values for the current column.

# print(f"{column:{20}}: ==========================>{missing * 100:.2f}%"): This prints out the column name, followed by a series of equal signs for 
# visual separation, and then the percentage of missing values in that column, formatted to display two decimal places. The {column:{20}} part ensures that the column name is left-aligned in a space of width 20 characters.
    

print (df.dropna(axis=1, how='all').shape)
df.drop('county_name', axis=1, inplace=True)

for column in df.columns:
    missing = df[column].isna().sum() / df.shape[0]
    print(f"{column:{20}}: ==========================>{missing * 100:.2f}%")


# Do men or women speed more often
print(df.driver_gender.value_counts())
print(df.driver_gender.value_counts(normalize=True))

# Group all the violations
print(df['violation'].value_counts())
print(df['violation'].value_counts(normalize=True))


speed_violation = df[df.violation == 'Speeding']
fig = plt.figure(figsize=(12,6))

plt.subplot(121)
sns.countplot(x = 'driver_gender', data=df)
plt.title('Men and Women Distribution')

plt.subplot(122)
sns.countplot(x = 'driver_gender', data=speed_violation)
plt.title('Men and Women distribution (Violation = Speeding)')

plt.show()