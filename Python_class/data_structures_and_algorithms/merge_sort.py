# 1 big list 
def merge_sorted(lst):
    len_list = len(lst)

    #If the list is having only one elements ==> the list is sorted
    if len_list == 1:
        return lst
    #find the middle elements to split the list
    mid = len_list //2
    #To make it become a sepreate list [2,3,4,5,6,7,8,9] ==> [[2],[3],[4],[5],[6],[7],[8],[9]]
    left_lst = merge_sorted(lst[:mid])
    right_lst = merge_sorted(lst[mid:])
    return merge(left_lst,right_lst)

def merge(lst1,lst2):
    i = j = 0 #To point to index 0 in both list
    results = [] #To store results

    len_lst1 = len(lst1)
    len_lst2 = len(lst2)

    while i < len_lst1 and j < len_lst2:
        if lst1[i] <= lst2[j]:
            results.append(lst1[i])
            i +=1
        else:
            results.append(lst2[j])
            j +=1
    results.extend(lst1[i:])
    results.extend(lst2[j:])
    return results

lst = [5,7,13,18,21,23,24,7,11,14,18,19]
res = merge_sorted(lst)
print(res)




# Two diffrent list
def merge(list1, list2):
    i = j = 0
    mergedList = []
    len_list1 = len(list1)
    len_list2 = len(list2)

    while i < len_list1 and j < len_list2:
        if list1[i] < list2[j]:
            mergedList.append(list1[i])
            i += 1
        else:
            mergedList.append(list2[j])
            j += 1
    mergedList.extend(list1[i:])
    mergedList.extend(list2[j:])

    return mergedList

list1 = [5,12,13,18,21,22]
list2 = [7,11,14,18,19,29]

print(merge(list1,list2))
print(merge([5,12,13,18],[7,11,14,18,19,20,21]))
print(merge([5,7,13,18,21,23,24,111],[7,11,14,18,19]))
print(merge([5,12,13,18,20],[7,11,14,18,21]))