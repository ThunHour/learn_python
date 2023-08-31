#Create a python program that ask the user to enter a number:
#then print a countdown from the given number to 1 and finally display "BOOM!"

userInput = int(input("Enter a number: "))

count = 0
if userInput >= 0:
        while count < userInput:
                print(userInput)
                userInput -=1
        print("BOOM!")
else:
        pass



