def insertion(arr):
    for i in range(len(arr)-1):
        while arr[i]> arr[i+1] and i>=0: #arr[i] ==> value of index i
            #check if arr[0] > arr[1]
            #if it is bigger swip
            arr[i],arr[i+1] = arr[i+1],arr[i]
            i-=1

arr = [12,10,5,3,55,45]
insertion(arr)
print(arr)



def insertion_sort(arr):
    for i in range(len(arr)-1):
        while arr[i] < arr [i-1] and i>0: #arr[i] ==> value of index i 
            #check if arr[1] < arr[0]
            #if arr[1] is smaller than arr[0] swip
            arr[i], arr [i-1] = arr [i-1], arr[i]
            i-=1

arr = [12,10,5,3,55,45]
insertion_sort(arr)
print(arr)