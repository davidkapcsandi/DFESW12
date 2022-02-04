# testitems ={ "valve1":True,"valve2":True,"valve3":True,"valve4":True,"valve5":False,"valve6":True, }

# for i in testitems.keys():
#     print(i,"Is Ok: ",testitems[i])


# countvar = 5
# while countvar > 0:
#     namevar1 = input("Type NAME: ")
#     print(f"{namevar1} is awesome!")
#     countvar = countvar - 1

# countvar = 5
# listvar = []
# while countvar > 0:
#     listvar.append(input("Type Name: "))
#     countvar = countvar -1
# print(listvar)

# var1 = '* '

# for i in range(1,10):
#     while i > 0:
#         print(var1)
#         i = i -1

# number = 0

# while number < 5:
#     print(number)
#     number += 1


# my_fruit = ["Apple", "Banana", "Orange"]

# for fruit in my_fruit:
#     print(fruit.upper())


# for number in range(10):
#     print(number)

# for word in "Hello world".split():
#     print(word)

# for value in {"key": "value"}.values():
#     print(value)

# for key, value in {"key": "value"}.items():
#     print(key, value)


# n=5;
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')




# numbers =(1, 2, 3, 4, 5, 6, 7, 8, 9)
# count_odd = 0
# count_even = 0
# for x in numbers:
#     if not x %2:
#         count_even+=1
#     else:
#         count_odd+=1
# print("Number of even numbers", count_even)
# print("Number of odd numbers", count_odd)



# temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# degree = int(temp[:-1])
# i_convention = temp[-1]

# if i_convention.upper() == "C":
#   result = int(round((9 * degree) / 5 + 32))
#   o_convention = "Fahrenheit"
# elif i_convention.upper() == "F":
#   result = int(round((degree - 32) * 5 / 9))
#   o_convention = "Celsius"
# else:
#   print("Input proper convention.")
#   quit()
# print("The temperature in", o_convention, "is", result, "degrees.")