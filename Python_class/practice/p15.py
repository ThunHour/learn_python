# Create a python program that prints RANDOMLY 0 or 1 N times.
# N correspond to the number passed in the input by the user (check the examples)

from random import randint
userInput = int(input("Enter a number: "))

for i in range(userInput):
    print(randint(0,1))
