word= input('Input a text:')
if len(word)>0:
    firstword=len(word)//2
    print(word[:firstword],word[firstword:])
else: print('The string is empty.')



