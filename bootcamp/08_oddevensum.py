
oddSum=0
evenSum=0
countOdd=0
countEven=0
num=input('Input a number:')
if num.isdecimal():
    num=int(num)
    for number in range(0,num+1):
        if number %2 == 0:
            evenSum += number
            countEven += 1
        else:
            oddSum += number
            countOdd+=1
    print(f'Sum of odd numbers = {oddSum/countOdd}')
    print(f'Sum of even numbers = {evenSum/countEven}')
else:
    print('invalid Input')

