userInput = input("Enter a string: ")

if len(userInput) > 0:

    middle = len(userInput)//2

    firstHalf = userInput[:middle]
    secondHalf = userInput[middle:]
    String = firstHalf.upper() + secondHalf.lower()
    print(String)


else:
    print("The string is empty.")
