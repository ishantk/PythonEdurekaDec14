# importing a User Defined Module
# Importing a module shall execute code in the module
# import Session7D
# print(dir(Session7D))

# importing a built in Module
# import math
# print(dir(math))
#
# print(math.sqrt(16))

# from statement while importing
# from math import sqrt
# print(sqrt(16))


# from statement while importing with alias
from math import sqrt as sq
print(sq(16))
