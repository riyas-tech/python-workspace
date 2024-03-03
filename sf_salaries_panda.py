import numpy as np
import pandas as pd

sal = pd.read_csv("D:\\pyspark-workspace\\python-workspace\\salaries.csv", na_values='Not Provided')
print(sal.head())
print(sal.info())

average_salary = sal['BasePay'].mean()
print("Average Salary   :" , average_salary)

# Highest amount of overtime pay

highest_over_pay = sal['OvertimePay'].max()
print("Overtime Pay  :" , highest_over_pay)

# Job title of JOSHEPH DRISCOLL

job_title = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL'] ['JobTitle']
print ("Job Title   :", job_title)

# How much does JOSEPH DRISCOLL make (including benefits) ?

total_pay = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL'] ['TotalPayBenefits']
print ("Total Pay  :", total_pay)

# What is the name of the highest paid person ()
ind = sal['TotalPayBenefits'].idxmax()
employee_name = sal.loc[ind]['EmployeeName']
print ("Employee Name   :" , employee_name)

highest_paid_person = sal.sort_values(by='TotalPayBenefits', ascending=False).iloc[0]['EmployeeName']
print("Highest Paid Person    :", highest_paid_person)


#What is the name of the lowest paid person 
lowest_paid_person = sal.sort_values(by='TotalPayBenefits', ascending=True).iloc[0];
print("Lowest Paid Person Details")
print(lowest_paid_person)


# What was the average (mean) BasePay of all employees per year
#sal['Year'] = pd.to_numeric(sal['Year'], errors ='coerce')
#sal['BasePay'] = pd.to_numeric(sal['BasePay'], errors ='coerce')
#average_base_pay = sal.groupby('Year').mean()['BasePay']
#print("Average Base Pay Per Year")
#print(average_base_pay)


# How many unique job titles are there ?
unique_titles = sal['JobTitle'].nunique()
print("Unique Titles....")
print(unique_titles)