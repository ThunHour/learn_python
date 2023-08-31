
oddSum=0
evenSum=0
num=input('Input a number:')
if num.isdecimal():
    num=int(num)
    for number in range(0,num+1):

        if number %2 == 0:
            evenSum += number
        else:
            oddSum += number
    print(f'Sum of odd numbers = {oddSum}')
    print(f'Sum of even numbers = {evenSum}')
else:
    print('invalid Input')
    print(f'Sum of odd numbers ={oddSum}')
    print(f'Sum of even numbers ={evenSum}')
