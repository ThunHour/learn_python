# userInput = input("Input a string: ")
#
# if len(userInput)>0:
#     for i in userInput:
#         print(f'{i} :',ord(i))
# else:
#     print("The string is empty.")
#

# userInput = input("Input a string: ")
# if not userInput:
#     print("The string is empty.")
# else:
#     for i in userInput:
#         print(f'{i} :',ord(i))


text = input("Input a string :")

for i,j in zip(text,text) :
    print(i,j)
  # if not str(text) :
  #   print("The string is empty")
  #
  # else :
  #   print(i, ord(j), sep = ":")
