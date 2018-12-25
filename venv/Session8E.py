# re is Regular Expressions
import re

# If we put r in front of a string it becomes a raw string
# Escape Sequences shall not be considered

# message = r'Lets meet at John\'s Cafe'
message = R'Lets meet at John\'s Cafe'
print(message)

quote = "Search the Candle rather than cursing the darkness"
# result = re.match(r"the", quote)      # we will have no match
result = re.match(r"Search", quote)     # match matches from beginning
print(result)
print(type(result))
print(result.start())
print(result.end())

print("**************")

result = re.search(r"the", quote)
print(result)
print(type(result))
print(result.group(0))

print("**************")
result = re.findall(r"the", quote)
print(result)
print(type(result))

print("**************")
result = re.split(r"the", quote)
print(result)
print(type(result))

print("**************")
result = re.sub(r"the", "a", quote)
print(result)
print(type(result))






