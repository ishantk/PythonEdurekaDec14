# Reference to a Function

def sayHello(name):
    age = 10
    print("Hello",name," Age is",age)

sayHello("John")

print("sayHello is",sayHello)
print(type(sayHello))

# Reference Copy !!
say = sayHello     # we are creating an alias name to our function

print("say is",say)
print(type(say))


say("Jennie")



