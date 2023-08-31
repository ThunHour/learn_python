# import math

# name = "Hello"

# print(name[0:5])
# print(name[:4])

# print(name[2:])


# msg = "Monirith"

# print(msg[0:8:2])
# print(msg[0:8])


# a = "hello"
# print(a[:])


# my_list = [1,2,3,4,5,6,7]
# print(my_list[0])


# userInput = int(input("Enter number:"))
#
# if userInput % 2 == 0:
#     pass
# else:
#     print("ODD")

# i = 0
# while i < 5:
#     print("Hello world")
#     i += 1
#
#     if i == 2:
#         break


# a = "Python"
#
# for i in a :
#     if i == "h":
#         continue #skip
#     print(i)
# print("==============")
# a = "Python"

# import sys
# mylist = [25,65,95,87.52,62,"hello"]
# myTuple = (25,65,95,87.52,62,"hello")
# mylset = {25,65,95,87.52,62,"hello"}
#
# sizeOfList = sys.getsizeof(mylist)
# sizeOfTuple = sys.getsizeof(myTuple)
# sizeOfset = sys.getsizeof(mylset)
#
# if sizeOfList > sizeOfTuple and sizeOfList > sizeOfset:
#     print("Elephan")
# elif sizeOfTuple > sizeOfset:
#     print("Lion")
# else:
#     print("Cheetah")



def rgb(r,g,b):
    if r == 0 :
        return "000000"
    else:
        results = ""
        colorcode = {10:"A",11:"B",12: "C",13: "D",14: "E",15: "F"}
        #Red
        if r < 255:
            #First_digit
            firstDigit = r // 16
            if firstDigit in colorcode:
                results += colorcode[r//16]
            else:
                results += str(firstDigit)
            #Second_digit
            secondDigit = int((r / 16 - r //16)*16)
            if secondDigit in colorcode:
                results += colorcode[int((r / 16 - r //16)*16)]
            else:
                results += str(secondDigit)
        elif r < 0:
            results += ("00")
        else:
            results += ("FF")

        #Green
        if g < 255:
            thirdDigit = g // 16
            if thirdDigit in colorcode:
                results += colorcode[g//16]
            else:
                results += str(thirdDigit)
            fourthDigit  = int((g / 16 - g //16)*16)
            if fourthDigit in colorcode:
                results += colorcode[int((g / 16 - g //16)*16)]
            else:
                results += str(fourthDigit)
        elif r < 0:
            results += ("00")
        else:
            results += ("FF")

        #Black
        if b < 255:
            fifthDigit = b // 16
            if fifthDigit in colorcode:
                results += colorcode[b//16]
            else:
                results += str(fifthDigit)

            sixthDigit = int((b / 16 - b //16)*16)
            if sixthDigit in colorcode:
                results += colorcode[int((b / 16 - b //16)*16)]
            else:
                results += str(sixthDigit)
        elif b < 0:
            results += ("00")
        else:
            results += ("FF")

        return results

print(rgb(150,255,255))
