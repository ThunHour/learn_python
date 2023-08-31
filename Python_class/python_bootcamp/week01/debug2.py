userInput = input("Enter something: ")

try:
    userInput = int(userInput)

    if userInput % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

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
            print("Even Number")
        else:
            print("Odd Number")

    except ValueError:
        print("Not a valid")
