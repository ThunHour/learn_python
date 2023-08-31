# sum=0
# userinput = ''
# while userinput !="stop" :
#     userinput=input("Enter your number:")
#     if userinput.isdecimal():
#         userinput=int(userinput)
#         sum += userinput
#     elif userinput =='stop':
#         break
#     else:print(' The input is valid number')
# print(sum)
word= input('Input a text:')
if len(word)>0:
    firstword=len(word)//2
    print(word[:firstword:]+word[firstword:])
else: print('The string is empty.')
