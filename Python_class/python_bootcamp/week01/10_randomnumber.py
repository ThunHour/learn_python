from random import randint

SumEven = 0
n = int(input("Input Number:"))

for i in range(n):
   randomNumber = randint(2000,3000)

   if randomNumber % 2 == 0:
      SumEven += randomNumber

print(f'Sum of even random numbers: {SumEven}')


