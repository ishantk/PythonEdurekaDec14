import json
employees = {"eid": 101, "name": "John", "experience": 10, "salary": 80000}
print(type(employees))

# Convert Dictionary Data into String
# This String or Textual data in the form of dictionary is called JSON (Java Script Object Notation)
# In Client/Server Architecture Request and Respone industrially happens using REST Architecture which further uses JSON
# REST is Representational State Transfer : Data from Client to Server or Vice Versa using HTTP !!
data = json.dumps(employees)
print(data)
print(type(data))

# Textual JSON Data
jsonData = """{
  "bookstore": [
    {
      "price": "100 INR", 
      "name": "Objective C", 
      "author": "Steve Jobs"
    }, 
    {
      "price": "200 INR", 
      "name": "Android Programming", 
      "author": "Aaron Brooks"
    }, 
    {
      "price": "300 INR", 
      "name": "Advance Java", 
      "author": "David Smith"
    }
  ]
}"""

result = json.loads(jsonData)  # loads takes json as input and creates dictionary for us !!
print(result)
print(type(result))

# PS: JSON Module helps to convert dictionary into json (textual string) and vice versa !!
