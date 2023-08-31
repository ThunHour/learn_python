#linear_search
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

print(linear_search([50,65,123,23,12],65))

#binary_search
def binary_search(arr,x):
    mid = 0
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] > x:
            high = mid -1
        
        elif arr[mid] < x:
            low = mid +1
        
        else:
            return mid

print(binary_search([5,10,11,13,27,48,77],77))


#bubble_sorted
def bubble_sorted(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [50,65,8,12,65,7]
bubble_sorted(arr)
print(arr)


#Insertion_sorted
def insertion_sorted(arr):
    for i in range(len(arr)-1):
        while arr[i] < arr[i-1] and i > 0:
            arr[i],arr[i-1] = arr[i-1],arr[i]
            i -=1
    return arr

print(insertion_sorted([12,10,5,3,55,45]))

#Selection_sorted
def selection_sorted(arr):
    for i in range(len(arr)):
        min_pos = i
        for j in range(i+1,len(arr)):
            if arr[min_pos] > arr[j]:
                min_pos = j
    
        arr[i],arr[min_pos]= arr[min_pos],arr[i]

    return arr

print(selection_sorted([12,10,5,3,55,45]))


#Merge_sorted

