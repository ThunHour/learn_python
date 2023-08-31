# Binary Search in python

def binary_search(search_key,sorted_array):
    lower_bound=0
    upper_bound=len(sorted_array)-1

    while lower_bound <= upper_bound:
        mid=(lower_bound+upper_bound)//2
        print(f"Searching {sorted_array[lower_bound:upper_bound+1] } for {search_key}")

        if sorted_array[mid]==search_key:
            return mid
        elif sorted_array[mid]<search_key:
            lower_bound=mid+1
        elif sorted_array[mid]>search_key:
            upper_bound=mid-1
    return -1


# Sorted array
arr=[1,3,4,7,11,13,17,19,23,29,31,37,41,43,47,53,59,60]


# Search key
key=37

result=binary_search(key,arr)

if result==-1:
    print("Not found")
else:
    print(f"Element found at index {arr.index(result)}")  
