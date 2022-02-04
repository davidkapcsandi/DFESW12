# class Lettertest:

#     stringofletters = "AEIOU"

#     def testaletter(self,letterin):
#         if letterin.upper() in self.stringofletters:
#             return True
#         else:
#             return False




# testletter = "f"
# vowel = Lettertest()
# consonant = Lettertest()
# letterwithoneendpoint = Lettertest()
# consonant.stringofletters = "BCDFGHJKLMNPQRSTVWXYZ"
# letterwithoneendpoint.stringofletters = "P"
# vowelresult = vowel.testaletter(testletter)
# print(vowel.stringofletters)
# print(consonant.stringofletters)
# print(letterwithoneendpoint.stringofletters)

class Budget:

    def __init__(self, balance=0,):

        self.balance= balance
    
    def  balance_check(self):

        self.balance= int(input("How much is your balance? "))

        print(f"Your current balance is £{self.balance}")

    def balance_add(self, addval):

        self.balance = addval + self.balance

    def balance_remove(self, removeval):

         self.balance = self.balance - removeval


    def transfer(self, transferval, budget_name):

       #  self.balance= food.balance + self.balance

       self.balance_add(transferval)

       budget_name.balance_remove(transferval)

       clothes=Budget(50)

food=Budget(100)
pets=Budget(400)
food.balance_add(100)
clothes=Budget(50)
print(f"This is your food balance: £{food.balance}")
clothes.balance_add(1000)
print(f"This is your clothes balance: £{clothes.balance}")
clothes.balance_remove(500)
print(f"This is your clothes balance: £{clothes.balance}")
clothes.transfer(500, food)
pets.transfer(300, food)
print(f"This is your pets balance: £{pets.balance}")
print(f"This is your clothes balance: £{clothes.balance}")
print(f"This is your food balance: £{food.balance}")