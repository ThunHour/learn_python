# def liner_search(list,finding):
#     pos = -1
#     for i in range(len(list)): #range of list
#         if finding == list[i]:
#             return i #position 
#     return pos #-1

# print(liner_search([50,65,123,23,12],65))
# print(liner_search([50,65,123,23,12],541))

#While loops
# def liner_search(list1,s_no):
#     position = 0
#     while position <len(list1): #0 >
#         if list1[position] == s_no:
#             return position
#         position += 1

#     return -1

# print(linear_search([50,65,123,23,12],65))
# print(linear_search([50,65,123,23,12],541))

    

# def linear_search(list, s_no):
#     pos = -1
#     i = 0
#     for i in range(len(list)-1):
#         if s_no == list[i]:
#             return f'Number found at {i}'
#     return f'Number not found in the list'

# print(linear_search([50,65,123,23,12],65))
# print(linear_search([50,65,123,23,12],541))


# res = linear_search([21,433,42,43,52,13,75], 42)
# if res == -1:
#     print('Number not found in the list')
# else:
#     print('Number found at ', res)

# def linear_search(list, s_no):
#     pos = -1
#     i = 0
#     for i in range(len(list)-1):
#         if s_no == list[i]:
#             return i
#     return pos

# res = linear_search([21,433,42,43,52,13,75], 42)
# if res == -1:
#     print('Number not found in the list')
# else:
#     print('Number found at ', res)


# newList = []
# i = 0
# while i<= len(a):
#     first_num = a[0]
#     newList.append(first_num)
#     last_num = a[-1]
#     newList.append(last_num)
#     a = a[1:-1]
#     i +=2 
#     if len(a) < 2:
#         aList = a[::-1]
#         for j in aList:
#             newList.append(j)
# print(newList)


#Find duplicate Number

# def duplicate(num):
#     sorted(num)
#     for i in range(len(num)):
#         if num[i] == num[i+1]:
#             return num[i]
# print(duplicate([6,4,2,2,2,1,1]))

def liner_search(arr,finding):

    pos = -1

    for index in range(len(arr)):
        if finding == arr[index]:
            return index
    
    return pos
    
print(liner_search([50,65,123,23,12],65))
print(liner_search([50,65,123,23,12],541))
