# Raw String Literal : Escape Charaters shall be ignored
# path = r"C:\john\Documents\nodejs\server.js"
# print(path)

# User Defined Exception !!
#Inheritance
class BankingException(Exception):
    pass

class Banking:

    attempts = 0

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount

        if self.balance <= 2000:
            self.balance = self.balance + amount
            print("Sorry !! Balance is Low !! ",self.balance)
            Banking.attempts = Banking.attempts + 1
        else:
            print(amount, "Withdrawn ! New Balance is", self.balance)

        # Raising an Exception to Crash the Program !!
        if Banking.attempts == 3:
            # raise ValueError("Illegal Attempts !!")
            raise BankingException("Illegal Attempts !!")

print("==Banking Started==")

bRef = Banking(10000)

# Can be a use case that some hacker is trying to occupy bank's resources
# Somehow, Bank Server will go busy !!
try:
    for i in range(1, 60000):
        bRef.withdraw(3000)
except Exception as e:              # e is ref variable to the object of exception which is thrown and contains error message
    print("Some Error: ", e)


print("==Banking Finished==")
