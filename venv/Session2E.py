# Sets
# Which ensures UNIQUENESS
numbers = {10, 20, 30, 40, 50, 30, 40, 12, 56}
names = {"John","Abby","Sia","John","Mike","Leo","Sia"}

print(numbers)
print(names)

A = {1, 2, 3, 4, 5, 6}
B = {3, 4, 5}

C = A | B # C is A Union B

print(C)

S1 = {10, 20, 30, "John", "Fionna"}
S2 = {10, "John"}

# S2 is a subset of S1
# S1 is a superset of S2

print(10 in S1)
print("John" in S2)
print("Sia" not in S2)

print(S2.issubset(S1))
print(S1.issuperset(S2))

print(S1.union(S2))
print(S1.intersection(S2))
print(S1.difference(S2))

# Sets are MUTABLE AND UNIQUE
S3 =  {10, 20, 30, "John", "Fionna"}
S3.add(100)
S3.add("Kim")

# S3.remove(10)
# S3.discard(10)

print(S3)

S3.pop()

print(S3)

S3.clear()

print(S3)