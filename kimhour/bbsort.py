def bbsort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        print(list)

    print(list)


bbsort([3,6,2,4])
