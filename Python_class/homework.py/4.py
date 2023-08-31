def linear_search(list,s_no):
    i = 0
    pos = -1
    while i < len(list):
        if s_no == list[i]:
            return i 
        i += 1
    return pos


print(linear_search([50,65,123,23,12],12))
print(linear_search([50,65,123,23,12],541))