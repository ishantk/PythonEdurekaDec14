# Lambdas : Anonymous one line functions capable of evaluating a single expression

lm = lambda x, y : x * y    # Copying Reference of Anonymous Function to lm
print(lm)
print(type(lm))

# Since lambdas has no name we got a reference variable to hold the name

print(lm(10,20))

lm1 = lambda x, y, z : x * y * z
print(lm1(10,20,30))