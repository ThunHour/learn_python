import array
arr=array.array('i',[12,13,14,15,33,11,33,55,6,3,5,9,0,16])
for i in range(len(arr),0,-1):
    for j in range(0,i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
