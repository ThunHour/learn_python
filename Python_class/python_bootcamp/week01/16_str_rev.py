userInput = input("Enter a string: ")

if len(userInput) > 0:

    middle = len(userInput)//2

    firstHalf = userInput[:middle] #start to middle
    secondHalf = userInput[middle:] #middle to end
    string = firstHalf[::-1] + secondHalf #resluts
    print(string)
    print(firstHalf[::-1] + secondHalf)

else:
    print("The string is empty.")
