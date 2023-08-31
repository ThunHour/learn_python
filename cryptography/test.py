# word= input("Inter the word")
# new_list=''
# for i in word:
#     if i =="a" or i =="A":
#         new_list+= "ក"
#     elif i =="b" or i == "B":
#         new_list+= "ខ"
#     elif i =="c" or i == "C":
#         new_list+= "គ"
#     elif i =="d" or i == "D":
#         new_list+= "ឃ"
#     elif i =="e" or i == "E":
#         new_list+= "ង"
#     elif i =="f" or i == "F":
#         new_list+= "ច"
#     elif i =="g" or i == "G":
#         new_list+= "ឆ"
#     elif i =="h" or i == "H":
#         new_list+= "ជ"
#     elif i =="i" or i == "I":
#         new_list+= "ឈ"
#     elif i =="j" or i == "J":
#         new_list+= "ញ"
#     elif i =="k" or i == "K":
#         new_list+= "ណ"
#     elif i =="l" or i == "L":
#         new_list+= "ត"
#     elif i =="m" or i == "M":
#         new_list+= "ន"
#     elif i =="n" or i == "N":
#         new_list+= "ម"
#     elif i =="o" or i == "O":
#         new_list+= "យ"
#     elif i =="p" or i == "P":
#         new_list+= "រ"
#     elif i =="q" or i == "Q":
#         new_list+= "ល"
#     elif i =="r" or i == "R":
#         new_list+= "វ"
#     elif i =="s" or i == "S":
#         new_list+= "ស"
#     elif i =="t" or i == "T":
#         new_list+= "ហ"
#     elif i =="u" or i == "U":
#         new_list+= "ឡ"
#     elif i =="v" or i == "V":
#         new_list+= "អ"
#     elif i =="w" or i == "W":
#         new_list+= "ឌ"
#     elif i =="x" or i == "X":
#         new_list+= "ធ"
#     elif i =="y" or i == "Y":
#         new_list+= "ភ"
#     elif i =="z" or i == "Z":
#         new_list+= "ផ"
    
# print(new_list)
# Hill Algorithm Decryption _ B9
from sympy import *
key_matrix=[[12,41,66],[5,10,55],[22,44,11]]
key = Matrix(key_matrix)

print(f"key:{key}")

adj = key.adjugate()

print(f"adj:{adj}")