sum = 0
userInput = ''
while (userInput != "stop"):

    userInput = input("Input a number: ")
    if userInput == "stop":
        break
    else:
        #First try if userInput == type int
        try:
            userInput = int(userInput)
            sum += userInput
        except:
            try:
                #Try again if userInput == type float
                userInput = float(userInput)
                sum += userInput
                #If not int or float ==> eror
            except ValueError:
                print("The input must be a valid number")

print(f"Sum = {sum}")


# sum = 0
# userInput = ''
# while (userInput != "stop"):

#     userInput = input("Input a number: ")
#     if userInput == "stop":
#         break
#     else:

#         try:
#             userInput = int(userInput)
#             sum += userInput
#         except:
#             try:
#                 userInput = float(userInput)
#                 sum += userInput
#             except ValueError:
#                 print("The input must be a valid number")


# print(f"Sum = {sum}")
