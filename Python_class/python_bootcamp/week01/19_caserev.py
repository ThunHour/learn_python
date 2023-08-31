# newString = ""
# userInput = input("Enter a string: ")
#
# if not len(userInput):
#     print("The string is empty.")
# else:
#     for char in userInput:
#         newString += char.swapcase()
#     print(newString)

newString = ''
userInput = input("Input a string: ")

for char in userInput: #

    if char.isupper():  #True
        # print(char.isupper())
        change = char.lower()
        newString += change

    else:
        change = char.upper() #True
        newString += change

print(newString)

