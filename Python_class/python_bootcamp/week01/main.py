# print('Press 1 to encode')
# print('Press 2 to decode')
# word1=input('Enter the string to encode: ')
# deword=''
# for word1 in word1:
#     word1=ord(word1)
#     if word1 <=77:
#         word1+=13
#         word1=chr(word1)
#         deword+=word1
#     else:
#         word1-=13
#         word1=chr(word1)
#         deword+=word1
# print(f'The decoded text is:{deword}')
# print('Do you want to continue? [Y/N] ')
# next=input('')
# if next=="Y":
#     print('Press 1 to encode')
#     print('Press 2 to decode')
#     word1=input('Enter the string to decode: ')
#     deword=''
#     for word1 in word1:
#
#         word1=ord(word1)
#         if word1 <=77:
#             word1+=13
#             word1=chr(word1)
#             deword+=word1
#         else:
#              word1-=13
#              word1=chr(word1)
#              deword+=word1
#     print(f'The decoded text is:{deword}')
# else:
#     pass
#


# user_input = str(input("Enter a sentence: ")) #Python support OOP and FP
#
# replace_string = user_input.replace("OOP","Object Oriented Programming")
# otherNewString = replace_string.replace("FP","Functional Programming")
# newNewString =  otherNewString.replace("AI","Artificial Intelligence")
# print(newNewString)


userInput = input("Enter something : " )
newstring = ""
for i in userInput :
    if i == "#":
        break
    newstring += i
print(newstring)
