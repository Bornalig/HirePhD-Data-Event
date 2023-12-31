# -*- coding: utf-8 -*-
"""Copy of LinkedIn Vs Eventbrite.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1txRMZ6MbKyz4AFH-20OKdeU8lxI8HncK

# Import all the files from the drive containing the event information

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#mounting the csv files into the colab, 30 numbers of files need to be uploaded through the choose file option

from google.colab import files
uploaded=files.upload()

import glob

# list all csv files only
csv_files = glob.glob('*.{}'.format('csv'))
csv_files

import pandas as pd

df_csv_append = pd.DataFrame()

# append the CSV files
for file in csv_files:
    df = pd.read_csv(file)
    df_csv_append = df_csv_append.append(df, ignore_index=True)

df_csv_append

df_csv_append.fillna(0)

# save the data to a report csv file
df_csv_append.to_csv("report.csv", index= False)

# Find duplicate data based on rows
#import modules

import pandas as pd

#reading the csv file
report_data = pd.read_csv('report.csv')
report_data.head()
report_data.columns
duplicateRowsDF = report_data[report_data.duplicated()]
print("Duplicate Rows except first occurrence based on all columns are :")
print(duplicateRowsDF)

#list the files in the directory
! ls

# Display the conent of the report file(the output file)
! cat report.csv

# reading the csv file using read_csv
# storing the data frame in variable called df
df = pd.read_csv('report.csv')

# creating a list of column names by
# calling the .columns
list_of_column_names = list(df.columns)

# displaying the list of column names
print('List of column names : ',
      list_of_column_names)

import pandas as pd

df=pd.read_csv('report.csv')


#FINDING MAX AND MIN
p=df['Order Date'].max()
q=df['Order Date'].min()


print(q)
print(p)

# Lets select few columns for this exercise
columns_to_select = ['Order #', 'Order Date', 'Quantity', 'Total Paid', 'Attendee Status', 'Price Tier', 'Currency']

columns_to_select

import pandas as pd

# Load your CSV data 
df = pd.read_csv('report.csv')

# Specify the columns you want to keep
columns_to_keep = ['Order #', 'Order Date', 'Quantity', 'Total Paid', 'Attendee Status', 'Price Tier', 'Currency']

# Keep only the specified columns
df_subset = df[columns_to_keep]

# Save the result to a new CSV file 
df_subset.to_csv('report_concise.csv', index=False)

#View the data in the output file
! cat report_concise.csv

# Load your CSV data 
df = pd.read_csv('report_concise.csv')

# Count the number of entries (rows)
num_entries = len(df)

print(f"Number of entries in the CSV file: {num_entries}")

# to check the format of the dates find the error 

from datetime import datetime, timezone

# Creating a timezone-naive datetime object
naive_datetime = datetime(2023, 1, 1, 12, 0, 0)

# Creating a timezone-aware datetime object
aware_datetime = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

# Attempting to compare the two datetime objects
try:
    result = naive_datetime >= aware_datetime
except TypeError as e:
    print(f"Error: {e}")

#changing the time stamp format to similar datetime zone and stamp through out the Order Date column
# Load your CSV data 
df = pd.read_csv('report_concise.csv')

# Assuming your CSV has a column named 'timestamp', adjust based on your actual column name
date_column = 'Order Date'

# Convert the 'timestamp' column to a pandas datetime object, handling errors
df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

# Check for rows with invalid datetime values (NaT - Not a Time)
invalid_rows = df[df[date_column].isna()]

# Display or handle invalid rows as needed
if not invalid_rows.empty:
    print(f"Invalid datetime values in the following rows:\n{invalid_rows}")

# Save the result to a new CSV file (replace 'output_data.csv' with your desired file name)
df.to_csv('output_data.csv', index=False)

#finding the intial and last date in the column Order Date
df=pd.read_csv('output_data.csv')


#FINDING MAX AND MIN
p=df['Order Date'].max()
q=df['Order Date'].min()


print(q)
print(p)

# Maximum and minimum amounts paid
df=pd.read_csv('output_data.csv')


#FINDING MAX AND MIN
p=df['Total Paid'].max()
q=df['Total Paid'].min()


print(q)
print(p)

# Total revenue collected in the events

# Load your CSV data 
df = pd.read_csv('output_data.csv')

# Assuming you have a column named 'Total paid'
column_to_sum = 'Total Paid'

# Calculate the sum of the specified column
total_amount = df[column_to_sum].sum()

print(f"Total sum of '{column_to_sum}': {total_amount}")

# Finding the turn around before a specific date here(2022-07-09)
# Load your CSV data 
df = pd.read_csv('output_data.csv')

# Assuming you have a column named 'Order Date', replace it with your actual column name
date_column = 'Order Date'

# Specify the specific date (replace 'yyyy-mm-dd' with your desired date)
specific_date = '2022-07-09'


# Filter the DataFrame to include only entries before the specific date
entries_before_date = df[df[date_column] < specific_date]

# Count the number of entries before the specific date
count_before_date = len(entries_before_date)

print(f"Number of entries before {specific_date}: {count_before_date}")

# Finding the turn around before a specific date here(2022-07-09)
# Load your CSV data 
df = pd.read_csv('output_data.csv')

# Assuming you have a column named 'Order Date', replace it with your actual column name
date_column = 'Order Date'

# Specify the specific date (replace 'yyyy-mm-dd' with your desired date)
specific_date = '2023-06-19'


# Filter the DataFrame to include only entries before the specific date
entries_before_date = df[df[date_column] < specific_date]

# Count the number of entries before the specific date
count_before_date = len(entries_before_date)

print(f"Number of entries before {specific_date}: {count_before_date}")

# Specify the two specific dates
start_date = '2022-07-09'
end_date = '2023-06-19'

# Filter the DataFrame to include only entries within the specified date range
entries_within_range = df[(df[date_column] >= start_date) & (df[date_column] <= end_date)]

# Count the number of entries within the specified date range
count_within_range = len(entries_within_range)

print(f"Number of entries between {start_date} and {end_date}: {count_within_range}")

