def linear_search(list, check):
    inDex = 0
    false='Your number in being in list.'
    while inDex <len(list):
        if list[inDex]==check:
            return inDex
        else:
            inDex=inDex+1
    return false

print (linear_search([11, 12, 13, 14, 15, 18, 19, 25, 35, 41, 41, 45], 12))
