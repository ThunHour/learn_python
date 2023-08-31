# num = int(input("Enter a row:  "))
#
# row = 0
# while row < num:
#     star = row +1
#     while star > 0:
#         print("*", end= " ")
#         star = star -1
#     row +=1
#     print()


# num = int(input("Enter a row: "))
# row = 0
#
# while row < num:
#     star = row +1
#     while star > 0:
#         print("*", end= " ")
#         star = star -1
#     row += 1
#     print()
#

num = int(input("Enter a row: "))
row = 0 #row1 =1
while row < num: #row < num ==> contiune
    star = 0 #
    star = row + 1 #star 2
    print(star)
    while star > 0:
        star = star -1
        print("*",end = " ")
    row +=1
    print()
