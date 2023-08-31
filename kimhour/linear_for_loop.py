def linear(list,searching):
    for key,value in enumerate(list):
        if value == searching :
            return key
    return False


list = [1, 2, 4, 8, 23, 25, 44, 78, 89, 100]
searching = 44
print(linear(list,searching))
