while True:
    print("Press 1 to encode")
    print("Press 2 to decode")
    chooseNumber = input()
    newInput = ""
    if chooseNumber == "1":
        userInput = input("Enter the string to encode: ")
        newInput = userInput

    elif chooseNumber == "2":
        userInput = input("Enter the string to decode: ")
        newInput = userInput

    result = ""
    for char in newInput:
        char_values = ord(char)
        if char_values >= ord('a') and char_values <= ord('z'):
            if char_values > ord('m'):
                char_values -= 13
            else:
                char_values += 13
        elif  char_values >= ord('A') and char_values <= ord('Z'):
            if char_values > ord('M'):
                char_values -= 13
            else:
                 char_values += 13
        result += chr(char_values)

    print(result)


    print("Do you want to continue? [Y/N]")
    answer = input()

    if answer == "N":
        print("Thank you !")
        break
    else:
        continue


# # sum = 0
# # while True:
# #     num = input("Input a number: ")
# #     if num.isdigit():
# #         sum += int(num)
# #     elif num == "stop":
# #         break
# #     else:
# #         print("The input must be a valid number!")
# # print("The Sum is: {}".format(sum))
# #
# userInput = input("Enter something: ")
# # letter = "abcdefghijklmnopqrstuvwxyz"
# # bigLetter = "ABCDEFGHIJKLMNOPGQRSTUVWXYZ"
# # decode = ""
#
# # decode = ""
# # for char in userInput:
# #     if char.islower():
# #         check_word = ord(char)
# #         decode_value = check_word + 13
# #         decode_letter = chr(decode_value)
# #         decode += decode_letter
# #     else:
# #         check_word = ord(char)
# #         decode_value = check_word + 13
# #         decode_letter = chr(decode_value)
# #         decode += decode_letter
# #
# # print(decode)
#
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
#
