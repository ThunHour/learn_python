import random
sumEven =0
num= input('Input Number:')
if num.isdecimal():
    num=int(num)
    y=0
    while y<num:
        x=random.randint(2000,3000)
        if x%2==0:
            sumEven+=x
        y+=1
    print(f'Sum of even random numbers:{sumEven}')




