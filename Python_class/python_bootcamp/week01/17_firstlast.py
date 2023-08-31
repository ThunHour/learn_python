# userInput = input("Input a string: ")
#
# if len(userInput) >0:
#     print(f"First Character: {userInput[0]}")
#     print(f"last Character: {userInput[-1]}")
# else:
#     print("The string is empty.")


# userInput = input("Enter something: ")
#
# print(userInput[0:3])

string = input("Input a text:") #1

print(string.upper())
if not string: #3
    print("The string is empty") #4
else:
    print(string.upper()) #2
