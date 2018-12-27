# DataFrame from Series
import pandas as pd

s1 = pd.Series([10000, 12000, 15000], index=["John", "Jennie", "Jim"])
print(s1)

print()

s2 = pd.Series([15000, 17000, 21000, 30000], index=["John", "Jennie", "Jim", "Jack"])
print(s2)

print()

s3 = pd.Series([19000, 21000, 25000, 34000], index=["John", "Jennie", "Jim", "Jack"])
print(s3)

print()

# Creating a Table i.e. DatFrame from Series !!
# Dictionary of Series !!
table = pd.DataFrame({"2014": s1, "2015": s2})
print(table)

# Adding Series in DataFrame
# Working on Columns:
table["2016"] = s3

print()
print("==Table==")

print(table)


# Access a Series from DataFrame
print()
print(table["2015"])


print()

# del table["2015"]
# table.pop("2016")

# Working on rows:
rows = pd.DataFrame([[30000, 40000], [50000, 60000]], columns=["2014", "2016"])

table = table.append(rows, sort=True)

table = table.drop("Jim")

print(table)

print()

print(table.loc["John"])

print()

print(table.iloc[4])
