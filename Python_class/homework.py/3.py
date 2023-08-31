def sumOfString(string):
    listOfInt = []

    for i in string:
        if i.isdigit():
            listOfInt.append(i)
    return sum(map(int,listOfInt))
    
print(sumOfString("123456789Hello"))

print(sumOfString("12Hello"))