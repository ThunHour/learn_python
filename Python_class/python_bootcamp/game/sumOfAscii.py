while True:
    def sum_of_ascii():
        userInput = " "
        while userInput != 'stop' or 'Stop':
            userInput = input("Enter something: ")

            if userInput.isalpha():
                if userInput == "stop" or userInput == "Stop":
                    print("You asked to stop the program... Stopping")
                    quit()

                else:
                    total_of_ascii = 0
                    for char in userInput:
                        total_of_ascii += ord(char)
                    return f' {userInput}: {total_of_ascii}'

            else:
                print("Invalid String can't be converted")
                continue

    print(sum_of_ascii())
