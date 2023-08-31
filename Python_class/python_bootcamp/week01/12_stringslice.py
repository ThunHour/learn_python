userInput = input("Input a text: ")

if len(userInput)> 0:

    middle = len(userInput) // 2

    fistHalf = userInput[:middle]
    secondHalf = userInput[middle:]

    print(fistHalf + "  " + secondHalf )
else:
    print("The string is empty.")
