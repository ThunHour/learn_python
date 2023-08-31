inputByUser = int(input("Input your age: "))

if inputByUser > 0:

    if inputByUser >= 18:
        print("You are eligible to vote")

    else:
        print("You aren't adult yet... Sorry can't vote")

else:
    print("Age must be a positive digit")
