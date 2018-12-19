lm1 = lambda x, y, z : x*y*z

# Map with Lambdas
m1 = map(lm1,[1,2,3,4,5],[3,4,5,6,7],[2,2,2,2,2])
print(m1)
print(type(m1))
print(list(m1))

# List of Dictionaries
employees = [ {"eid":101,"name":"John"}, {"eid":201,"name":"Fionna"}, {"eid":301,"name":"Sia"} ]
lm2 = lambda emps : emps["eid"]
result = map(lm2,employees)
print(list(result))

def add(X, Y):
    return X+Y

lm3 = lambda P, Q : P + Q
L1 = [10, 20, 30, 40, 50]
L2 = [11, 21, 33, 44, 55]
# result = map(lm3, L1, L2)
result = map(add, L1, L2)
print(list(result))


lm4 = lambda num : num%2 == 0
L3 = [10,20,30,40,50,11,12,13,14,15]
result = map(lm4,L3)
print(list(result))

print("*************")

# filter with Lambdas
result = filter(lm4,L3)
print(list(result))

print("*************")

# reduce with Lambdas
# functools is a built in python module i.e. kind of functools.py
from functools import reduce

lm5 = lambda x,y : x*y
L4 = [1, 2, 3]
result = reduce(lm5, L4)
print(result)

# PS: Using Lambdas we write single expression functions which has no name
#     We can pass lambda and a big size data structure into either map, filter or reduce
#     so as to perform any operation
