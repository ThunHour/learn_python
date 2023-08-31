userInput = input("Enter a word: ")

if not userInput:
    print("0"*4)

else:
    if len(userInput) == 1:
        print(str(userInput)*4)

    elif len(userInput) > 2:
        fristString = userInput[0:2]
        firstStringReverse = fristString[::-1]
        secondString = userInput[-2:]
        secondStringReverse = secondString[::-1]
        print(firstStringReverse + secondStringReverse)
    else:
        print(str(userInput)*2)
