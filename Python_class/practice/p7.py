# Create a python program that ask the user for input: "Enter something: " Then the program will print the last character.
# IF the user input is empty, the program will print: "Nothing to display."


userInput = input("Enter something: ")
if not userInput:
    print("Nothing to display")
else:
    print(userInput[-1])
