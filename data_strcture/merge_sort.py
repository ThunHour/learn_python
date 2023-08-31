def merge(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=merge(arr[:mid])
    right=merge(arr[mid:])
    return devide(left,right)

def devide(left1,right1):
    merge_arr=[]
    i=j=0
    while i < len(left1) and j < len(right1):
        if left1[i]<=right1[j]:
            merge_arr.append(left1[i])
            i+=1
        else:
            merge_arr.append(right1[j])
            j+=1
    merge_arr.extend(left1[i:])
    merge_arr.extend(right1[j:])
    return merge_arr

    

array=[3,44,38,5,47,15,36,26,27]
print(merge(array))



