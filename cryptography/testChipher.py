#Implement Hill Algorithm - Encryption

import string
import numpy as np

 #Step 1 : Generation of Key Matrix
 # Taking the input dimensions - no. rows and col of key matrix

rk = int(input("Enter the no. of rows of key matrix : ")) #no.rows of key matrix
ck = int(input("Enter the no. of columns of the key matrix : "))

key = []

# populate the key matrix

print()
print("Enter the elements of the key matrix row wise : ")

#user input for key matrix

for i in range(rk):

    a = []

    for j in range(ck):

        a.append(int(input()))

    key.append(a)

print("the key matrix is : ")

key_matrix = np.array(key)

print(key_matrix)
print()

print(type(key_matrix))

#Step 2 : Accepting the plain text, add filler characters to match the D(key_matrix)

plain_text = input("Enter the plain Text : ")

plain_text = plain_text.replace(" " , "")

print("Plain Text without spaces : ")
print(plain_text)
print()
print("Length of the plain text : " + str(len(plain_text)))

print()

#add filler characters to match the D(key_matrix)
while((len(plain_text) % rk != 0)):

      plain_text += 'x'

print("The Plain Text after adding fillers : " + plain_text)
#Split the plain text col(PT_ Matrix) = row(key_matrix)

print()

print("the list of plain text characters : ")

plain = list(plain_text)
print()
print(plain)

# Covert List of PT Characters to Numbers

plain_text_index = []

for char in plain:

    plain_text_index.append(ord(char) - ord('a'))

print()
print("The Indexes of all the Plain Text Characters is : ")
print(plain_text_index)
print()

#creating the plain text matrix = numerical values of the characters

#Remember that no. col of the plain text matrix = no. rows of key matrix

plain_text_matrix = np.array(plain_text_index)

rp = int(len(plain_text_matrix) / rk ) # length(pT) = 12 / 3 = 4
cp = rk
plain_text_matrix.resize(rp , cp)

print("The plain Text Matrix is : ")
print()
print(plain_text_matrix)
print()
print(key_matrix)

#Encryption : C = E(PT Matrix ,Key (3x3)) = [matrix mul of matrices (P.K)] % 26
# O/ P = Cipher Text 

encryption_matrix = np.matmul(plain_text_matrix , key_matrix)

print("Matrix before performing Mod 26 :")
print(encryption_matrix)
print()

#Never ever forget mod 26 in Hill Cipher

encryption_matrix = np.mod(encryption_matrix , 26)

print("Cipher Matrix after Mod 26 : ")
print(encryption_matrix)

#Dimension of CT = no. rows(PT Matrix) X no.col.(Key_matrix)

print()

cipher_text_matrix = []

for i in range(rp):

    a = []

    for j in range(ck):

        a.append(chr(int(encryption_matrix[i][j]) + ord('a')))

    cipher_text_matrix.append(a)


print()

print("The Cipher Text Character Matrix is : ")
print(cipher_text_matrix)
print()
cipher_text_matrix = np.array(cipher_text_matrix)
cipher_text_matrix.resize(1 , len(plain_text))
print(cipher_text_matrix)


print("List of plain text characters : ")
print(plain)
