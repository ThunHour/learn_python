from random import randint
def random_tuple(n):
    tup1 = ()
    sum = 0
    for i in range(1,n+1):
        random_num = randint(0,100)
        tup1 += (random_num,)
        print(f'Random number {i}: {random_num}')
        sum += random_num
    print(tup1)
    print(sum)
    return sum


random_tuple(5)
