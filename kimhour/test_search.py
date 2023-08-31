def linear(list, search):
    for key,values in enumerate(list):
        if values == search:
            print(f'The number was found with execution {key}')
            return 1
    return -1


list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 23, 34, 44, 45, 65]
search = 45
number = linear(list, search)
if number == -1:
    print('Searching is fail')
elif number == 1 :
    print("Searching is Successful")


for i in range(10):
    print("@_@")


def binary_search(list,search):
    low = 0
    up =len(list)-1
    count=1
    while low <= up :
        mid =(low+up)//2
        if list[mid] == search:
            print(f'we use {count} execution')
            return mid
        elif list[mid] < search:
            low = mid +1
        else:
            up = mid -1
        count +=1
    print(f'we use {count}execution')
    return -1


list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 23, 34, 44, 45, 65]
search = 45
number1 = binary_search(list, search)
if number1 == -1:
    print('The number can not found')
else:
    print(f"The number is found at index {number1}")
