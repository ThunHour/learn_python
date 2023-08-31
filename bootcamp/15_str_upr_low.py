word= input('Input a text:')
if len(word)>0:
    firstword=len(word)//2
    print(word[0:firstword].upper(),word[firstword:].lower())
else: print('The string is empty.')
