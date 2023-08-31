# Create a python program that asks the user: "Enter something: " Then display the sentence until the first # (hashtag) character. IF no hashtag is entered, you will just print the sentence.
# IF no value is entered, you will not print anything.

userInput = input("Enter something: ")
newString = ""
if not userInput :
    pass
else:
    for i in userInput:
        if i == "#":
            break
        newString += i

    print(newString)
