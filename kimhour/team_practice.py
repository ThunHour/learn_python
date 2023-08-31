#1
def remove_duplicate(array):
    #method 1
    res = []
    for num in array:
        if num not in res:
            res.append(num)

    return res

    #method2
    return list(set(array))

print(remove_duplicate([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))


#2
def double_integer(array):
    res = []

    for length in range(0,len(array)):
        if length % 2!= 0:
            res.append(array[length] * 2) #array[2] ==> 210
        else:
            res.append(array[length]) 
    
    return res

print(double_integer( [-1000,1653, 210, 0, 1]))



#3
def inverse_num(array):
    #method1
    res = []
    for num in array:
        if num < 0:
            res.append(abs(num))  # abs(-2) ==> 2, abs(2) ==>2
        
        else:
            res.append(-num)

    return res

    #method2
    return [-num for num in array]


print(inverse_num([1,-2,3,-4,5]))


#4
def reverse_string(strings):
    return strings[::-1]

print(reverse_string("world"))


#5
def sum_num_list(array):

    return sum(list(map(int, array)))

print(sum_num_list([9, 3, '7', '3']))


#6
def count_divisors(number):
    res = 0
    for num in range(1,number+1): #range(start,end-1)
        if number % num ==0:
            res+= 1

    return res

print(count_divisors(30))


#7
def odd_even(array):

    #Method 1
    sumArr = 0
    for i in array:
        sumArr += i
    
    if sumArr % 2 ==0:
        return "even"
    
    else:
        return "odd"

    #method 2
    return "even" if sum(array) % 2== 0 else "odd"

print(odd_even([]))
