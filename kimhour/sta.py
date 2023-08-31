import statistics
listOdd=[]
listEven = []
num = int(input('Enter a number: '))

for i in range(1, num+1):
    if i%2 ==0:
        listEven.append(i)
    else:
        listOdd.append(i)

print('Odd Average: ', statistics.mean(listOdd))
print('Even Average: ', statistics.mean(listOdd))
