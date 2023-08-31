print("Enter something: ")
userInput = input()

try:
    userInput = int(userInput)

    if userInput % 2 == 0:
        print("The number you have entered is Even")
    else:
        print("The number you have entered is Odd")

except:
    try:
        newFloat = float(userInput)
        #find "." in the string
        dot = userInput.find(".")

        #get all the len of userInput
        lenOfUserInput = len(userInput)

        #ALl in index of string
        allIndex = lenOfUserInput - 1

        #Reminding after the dot
        reminding = allIndex - dot

        i = 1
        remindingOfFloat = 1

        while i <= reminding:
            remindingOfFloat *=10
            i += 1
        multipleOffloat = remindingOfFloat
        if (newFloat * multipleOffloat) % 2 == 0:
            print("The number you have entered is Even")
        else:
            print("The number you have entered is Odd")

    except ValueError:
        print("Not a valid")
