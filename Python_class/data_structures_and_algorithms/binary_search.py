#You need to have sorted list before perform binary search

# # For loop
# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0   

#     for i in range(len(arr)):
#         mid = (low + high)//2
        
#         # If x is greater, ignore left half
#         if arr[mid] > x:
#             high = mid - 1
        
#         # If x is smaller, ignore right half
#         elif arr[mid]<x:
#             low = mid+ 1
        
#         # means x is present at mid
#         else:
#             return mid
#     return -1

# print(binary_search([5,10,11,13,27,48,77], 77))


# While_loop
# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0   
    
#     while low <= high:

#         mid = (high + low) // 2
#         # If x is greater, ignore left half
#         if arr[mid] < x:
#             low = mid + 1
#         # If x is smaller, ignore right half
#         elif arr[mid] > x:
#             high = mid - 1

#         # means x is present at mid
#         else:
#             return mid

    # If we reach here, then the element was not present
#     return -1

# print(binary_search([5,10,11,13,27,48,77], 48))
# print(binary_search([77,48,27,13,11,10,5],77))


# #Reverse_list
# def binary_search(arr,x):
#     low = 0
#     high = len(arr)-1
#     mid = 0

#     if arr[-1] < arr[0]:
#         newList = sorted(arr)
#     else:
#         newList = arr
    
#     for i in range(len(newList)):
#         mid = (low+high)//2

#         if newList[mid] > x:
#             high = mid -1
#         elif newList[mid] <x:
#             low = mid +1
#         else:
#             return mid
#     return -1 
# print(binary_search([77,48,27,13,11,10,5],40))


# def binary_search(arr,x):
#     low = 0
#     high = len(arr)-1
#     mid = 0 
#     if arr[-1] < arr[0]:
#         newList = sorted(arr)
#     else:
#         newList = arr

#     while low <= high:
#         mid = (low + high)//2

#         if newList[mid] >x:
#             high = mid-1
#         elif newList[mid] <x:
#             low = mid +1
#         else:
#             return mid
#     return -1 

# print(binary_search([5,10,11,13,27,48,77], 48))



def binary_search(arr,findig):
    low = 0 #index of low
    high = len(arr)-1 #index of high
    mid = 0

    for index in range(len(arr)):
        mid = (low + high)//2


        if arr[mid] > findig:
            high = mid - 1 
        elif arr[mid] < findig:
            low = mid + 1

        else:
            return mid 

print(binary_search([5,10,11,13,27,48,77], 48))