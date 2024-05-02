import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

companies = pd.read_csv("D:\\pyspark-workspace\\python-workspace\\unicorn.csv")

print(companies.head(10))

print("Size   :", companies.size)

#Number of rows and columns
print(companies.shape)


#Basic informaton about dataset 
print(companies.info())


# Get statistics 
print(companies.describe())

companies["Date Joined"] = pd.to_datetime(companies["Date Joined"])
print(companies.info())

companies["Year Joined"] = companies["Date Joined"].dt.year
companies.head()


#sample data
companies_sample = companies.sample(n = 50, random_state = 42)

# Create new `years_till_unicorn` column 
companies_sample["years_till_unicorn"] = companies_sample["Year Joined"] - companies_sample["Year Founded"]

# Group the data by `Industry`. For each industry, get the max value in the `years_till_unicorn` column.
grouped = (companies_sample[["Industry", "years_till_unicorn"]]
           .groupby("Industry")
           .max()
           .sort_values(by="years_till_unicorn")
          )
print (grouped)