def sum_of_digit(string):
    list=[]
    for i in string:
        if i.isdigit():
            num=int(i)
            list.append(num)
    return sum(list)

print(sum_of_digit('i go school 342 kit'))

