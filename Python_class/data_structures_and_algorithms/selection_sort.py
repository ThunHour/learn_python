def selection(arr):
    for i in range(len(arr)):
        min_pos = i #to store value of the index[0]
        for j in range(i+1,len(arr)): 
            if arr[min_pos]> arr[j]: #if value of index[0] > value of index[1]
                min_pos =j #change min_pos to j
        
        arr[i], arr[min_pos] = arr[min_pos],arr[i]


arr = [12,10,5,3,55,45]

selection(arr)
print(arr)

