number = input('Input a number: ')

if number.isdecimal():

     number = int(number)
     if number%2 == 0:
          print("Even Number")
     else:
          print("Odd Number")

else:
     print("Not a valid ")
