num = int(input("Enter a rows of star: "))

row = 0
print("Right Triangle Shape Using while loop: ")
while row < num:
    star = row +1
    while star > 0:
        print("*",end=" ")
        star = star - 1
    row += 1
    print()

row = 0
print("Left Triangle Shape Using while loop: ")
while row < num:
    star = num
    star -= row
    while star > 0:
        print("*",end=" ")
        star -= 1
    row += 1
    print()

row = 0
print("Left Triangle Shape Using while loop: ")
while row < num:
    blank = 1
    while blank < num-row:
        print(" ",end=" ")
        blank += 1
    star = 0
    while star <= row:
        print("*",end=" ")
        star +=1
    print()
    row +=1

row = 0
print("Pyramid Using while loop: ")
while row < num:
    blank = 0
    while blank <num-row:
        print(" ",end="")
        blank += 1
    star = 0
    while star <= row:
        print("*",end=" ")
        star +=1
    print()
    row +=1

print("Pyramid reverse  Using while loop: ")
row = 0
while row < num:
    print(" "* row, end = " ")
    star = 0
    while star < num - row:
        print("*", end= ' ')
        star += 1
    print()
    row +=1


print("diamond Using while loop: ")
row = 0
while row < num:
    blank = 0
    while blank < num-row:
        print(" ",end= "")
        blank +=1
        star = 0
    while star <= row:
        print("*",end=" ")
        star +=1
    # while row < num:
    #     print(" "*row, end= "")
    #     star= 0
    #     while star < num - row:
    #         print("*",end= " ")
    #         star +=1
    print()
    row+=1

