# File Operations with pandas !!
import pandas as pd

# table = pd.read_csv("CityTemps.csv")
# print(table)
# print(type(table))

# Locating Column
# print(table["Year"])

# locating Row !!
# print(table.iloc[1])

# Slicing
# print(table.iloc[1:5])

# table.to_csv("NewCityTemps.csv")
# print("==Data Written==")

# For xlsx please install xlrd package in preferences of pycharm !!

table = pd.read_excel("ScoreFinal.xlsx")
print(table)

# Convert JSON to Excel
# pd.read_json() -> Create a DataFrame
# pd.to_excel()  -> Dump it into xlsx

# to Connect ot DB
# mysql.connector library
# We have libraries with which we can connect to DB !!
