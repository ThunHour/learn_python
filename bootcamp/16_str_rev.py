word= input('Input a text:')
if len(word)>0:
    firstword=len(word)//2
    print(word[:firstword:][::-1]+word[firstword:])
else: print('The string is empty.')
