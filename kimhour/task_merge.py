def merge(list1,list2):
    i=j=0
    merged=[]
    len_list1=len(list1)
    len_list2=len(list2)
    while i < len_list1 and j < len_list2:
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    while i < len_list1:
        merged.append(list1[i])
        i += 1
    while j < len_list2:
        merged.append(list2[j])
        j += 1
    print(merged)


list1 = [1,5,7,9]
list2 = [2,4,6,10]
merge(list1,list2)
