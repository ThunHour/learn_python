inputByUser = input("Enter your name:")
timeToDisplay = int(input("Enter number of time to display:"))

if len(inputByUser) > 1: #to check if user has put input or not
    for i in range(timeToDisplay):
        print(inputByUser)

else:
    print("No name entered")
