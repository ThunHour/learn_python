#Create a python program that ask the user to enter a number:
#"Enter a number: " and then print "Hello World!" N times.
#IF the user input is a negative number or 0 you will not print anything.

n = int(input("Enter a number: "))
if n <1:
    pass
else:
    count = 0
    while count < n:
        print("Hello World!")
        count +=1
