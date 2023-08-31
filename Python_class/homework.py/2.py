def sum_of_num(number):
    if number <= 1:
        return number
    return number +  sum_of_num(number-1)
print(sum_of_num(2)) #1+2
print(sum_of_num(5)) #1+2+3+4+5
