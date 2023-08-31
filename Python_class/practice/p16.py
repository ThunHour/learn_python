# Create a python program that ask the user for a title: "Enter a title: " Then print the title as HTML TITLE Style: <h1>Your title here</h1>
# IF the user did not enter value the program will print "Nothing to display."

userInput = input("Enter a title: ")
if not userInput:
    print("Nothing to display")
else:
    print(f'<h1>{userInput}</h1>')
