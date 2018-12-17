nums = (10,20,30)

print("nums hashcode is",hex(id(nums)))

# + operation on sequence shall concatenate
# 2 tuples can be concatenated to create a new 3rd tuple
nums = nums + (40,50,60) # A new Tuple is created and nums is refering now to the new tuple

print("nums hashcode after manipulation is",hex(id(nums)))

# As per observation it seems that tuple is MUTABLE
# But it is not !!
print(nums)

# del nums[1]  # error
# del nums   # Tuple is deleted from Memory


