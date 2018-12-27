# DataFrame in Pandas
import pandas as pd
import numpy as np

numbers = [11, 22, 33, 44, 55]
arr = np.arange(10, 21)
# salaries = {"john": 10000, "jennie": 20000, "jim": 23000, "jack": 30000, "joe": 35000}
salaries = [{"john": 10000, "jennie": 20000, "jim": 23000, "jack": 30000, "joe": 35000}]
employees = [{"eid": 101, "name": "John", "salary": 30000}, {"eid": 201, "name": "Fionna", "salary": 50000, "age": 30}]


# Constructing from 1-D Data
table1 = pd.DataFrame(numbers)
print(table1)
print(type(table1))

print()

table2 = pd.DataFrame(arr)
print(table2)
print(type(table2))

print()

""" errror 
table3 = pd.DataFrame(salaries)
print(table3)
print(type(table3))

"""
# table3 = pd.DataFrame(salaries)
# table3 = pd.DataFrame(employees)
# table3 = pd.DataFrame(employees, index=["John", "Jennie"])
table3 = pd.DataFrame(employees, index=[10, 20])
print(table3)
print(type(table3))
print()
