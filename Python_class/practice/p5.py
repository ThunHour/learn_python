#Create a python program that asks the user for a number: "Enter a number: " and then print "ODD" or "EVEN" based on the given input.

# userInput = int(input("Enter a number: "))

# if userInput % 2 ==0:
#     print("EVEN")
# else:
#     print("ODD")


for i in range(1,101):
    res = 0
    if i % 3 == 0 or i % 4 ==0:
        res += 1
        print("True")
    else:
        print("False")
print(res)