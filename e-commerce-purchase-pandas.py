import pandas as pd
import numpy as np

ecom = pd.read_csv("D:\\pyspark-workspace\\python-workspace\\Ecommerce Purchases.csv", na_values='Not Provided')
print(ecom.head())
print(ecom.info())


# What is the average purchase price
average_purchase_price = ecom["Purchase Price"].mean()
print("Average Purchase Price : "   , average_purchase_price)

# Highest and Lowest Purchase Price
highest_price = ecom["Purchase Price"].max()
lowest_price = ecom["Purchase Price"].min()

print("Highest Purchase Price :", highest_price)
print("Lowest Purchase Price  :", lowest_price)

# How many people have 'en' as their language of choice on the website ?

count_en = ecom[ecom['Language'] == 'en']['Language'].count()
print("Count   =", count_en)

# How many people have the job title as "Lawyer"
count_lawyer = len(ecom[ecom['Job'] == 'Lawyer'])
print("Count Lawyer   :", count_lawyer)

# How many people purchsed in AM  and how many people purchased in PM
count_am = len(ecom[ecom['AM or PM'] == 'AM'])
count_pm = len(ecom[ecom['AM or PM'] == 'PM'])

print("Count AM   :", count_am)
print("Count PM   :", count_pm)


# What are the 5 most common Job Titles
top_titles = ecom['Job'].value_counts().head(5)
print("Top Titels   :", top_titles)

# Someone mae a purchase that came from Lot : 90 WT , what was the purchase Price for this transaction.
purchase_price = ecom[ecom['Lot'] == '90 WT']['Purchase Price']
print("Purchase Price   :", purchase_price)


# How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
purchase_above_95 = len(ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)])
print("Purchase Pirce Above  95   :" , purchase_above_95)

# How many people have a credit card that expires in 2025?
expiry = sum(ecom['CC Exp Date'].apply(lambda x : x[3:] == '25'))
print("Expiry    :" , expiry)

# what are the top 7 popular email providers 
email_providers = ecom['Email'].apply(lambda x : x.split('@')[1]).value_counts().head(7)

print("Top email providers")
print(email_providers)