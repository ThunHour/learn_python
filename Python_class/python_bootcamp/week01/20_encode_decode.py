while True:
    print("Press 1 to encode")
    print("Press 2 to decode")
    chooseNumber = input()

    if chooseNumber == "1":
        userInput = input("Enter the string to decode: ")

        lowerCase = userInput.lower()
        letter = "abcdefghijklmnopqrstuvwxyz"
        decode = ""

        for char in lowerCase:
            decode += letter[(letter.find(char)+13)%26]

        print(decode.upper())

    elif chooseNumber == "2":
        userInput = input("Enter the string to decode: ")

        lowerCase = userInput.lower()
        letter = "abcdefghijklmnopqrstuvwxyz"
        decode = ""

        for char in lowerCase:
            decode += letter[(letter.find(char)-13)%26]
        print(decode.upper())
    else:
        print("Please choose 1 or 2")

    print("Do you want to continue? [Y/N]")
    answer = input()

    if answer == "N":
        break
    else:
        continue



# while True:
#     print("Press 1 to encode")
#     print("Press 2 to decode")
#     chooseNumber = input()
#     newInput = ""
#     if chooseNumber == "1":
#         userInput = input("Enter the string to encode: ")
#         newInput = userInput
#
#     elif chooseNumber == "2":
#         userInput = input("Enter the string to decode: ")
#         newInput = userInput
#
#     result = ""
#     for char in newInput:
#         char_values = ord(char)
#         if char_values >= ord('a') and char_values <= ord('z'):
#             if char_values > ord('m'):
#                 char_values -= 13
#             else:
#                 char_values += 13
#         elif  char_values >= ord('A') and char_values <= ord('Z'):
#             if char_values > ord('M'):
#                 char_values -= 13
#             else:
#                  char_values += 13
#         result += chr(char_values)
#
#     print(result)
#
#
#     print("Do you want to continue? [Y/N]")
#     answer = input()
#
#     if answer == "N":
#         print("Thank you !")
#         break
#     else:
#         continue



