# evenSum = 0
# oddSum = 0
# num = input("Enter number: ")
# i = 0
# j = 1
# if num.isdecimal():
#     num = int(num)
#     while i <= num:
#         evenSum +=i
#         i+=2
#     print(f"Sum of even numbers = {evenSum}")
#     while j <= num:
#         oddSum +=j
#         j += 2
#     print(f"Sum of odd numbers = {oddSum}")
# else:
#     print("invalid Input")
#     print(f"Sum of odd numbers = {oddSum}")
#     print(f"Sum of even numbers = {evenSum}")

# oddSum = 0
# evenSum = 0
# n = input("Input a number: ")
# if n.isdecimal():
#     n = int(n)
#     if n%2 !=0: #Check odd number
#         n = int(n) #n = int
#         for i in range (1,n+1):
#             if i%2 !=0: #no need
#                 oddSum = oddSum + i
#             if i%2 ==0: #no need
#                 evenSum = evenSum + i #no need
#         print("Average of odd number=",2*oddSum/(n+1))
#         print("Average of even number=",2*evenSum/(n-1))
#
#     if n%2 ==0: #check even number
#         n = int(n) #n = int
#         for i in range (1,n+1):
#             if i%2 !=0:
#                 oddSum = oddSum + i
#             if i%2 ==0:
#                 evenSum = evenSum + i
#         print("Average of odd number=", oddSum/n)
#         print("Average of even number=",evenSum/n)
# else:
#     print("Invalid input")
