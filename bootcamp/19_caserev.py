userInput = input('Input a string:')
word = ''
if len(userInput)>0:
    for i in userInput:
        newWord =i.swapcase()
        word+=newWord
    print(word)
else:
    print('The string is empty.')


