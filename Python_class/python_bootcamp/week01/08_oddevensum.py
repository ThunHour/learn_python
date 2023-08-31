oddSum = 0
evenSum = 0
countOdd = 0
countEven = 0

num = input("Input a number: ")

if num.isdecimal():
    num = int(num)
    for i in range(0,num+1):
        if i % 2 ==0:
            evenSum += i
            countEven += 1

        else:
            oddSum += i
            countOdd += 1


    print(f'Average of odd numbers = {evenSum / countEven}')
    print(f'Average of even numbers = {oddSum / countOdd}')

else:
    print("Invalid Input")

