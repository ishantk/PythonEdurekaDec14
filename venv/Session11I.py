import numpy as np
import pandas as pd

# np.random.rand(5, 4) -> 5 1-D arrays with each array having 4 random numbers

cols = ["A", "B", "C", "D"]

table = pd.DataFrame(np.random.rand(5, 4), columns=cols)
print(table)

print("--------")
print()

# Iterate in Columns of Table i.e. DataFrame !!
for key, value in table.iteritems():
    print("Key is:", key)
    print(value)
    print("-------------")
    print()


# Iterate in rows of Table i.e. DataFrame !!
"""
for key, value in table.iterrows():
    print("Key is:", key)
    print(value)
    print("-------------")
    print()
"""

"""
for row in table.itertuples():
    print(row)
    print("-------------")
    print()
"""
