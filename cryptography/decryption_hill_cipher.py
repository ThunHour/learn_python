import string
import numpy as np
from sympy import *
plainText = input("Enter The Cipher plain text: ").replace(" ", "").upper()

matrix_input = int(input("Enter 2 for matrix 2x2 and 3 for matrix 3x3:"))

keyLetter = input("Enter the key letter: ").replace(" ", '').upper()

english_characters = string.ascii_uppercase

key_matrix = []

# check key_matrix

if len(key_matrix) < matrix_input**2:

    for letter in range(len(key_matrix), matrix_input**2+1):

        keyLetter += english_characters[letter]

# convert key to number

countIndex = 0

for row in range(matrix_input):

    row_matrix = []

    for column in range(matrix_input):

        findIndex = english_characters.find(keyLetter[countIndex])

        row_matrix.append(findIndex)

        countIndex += 1

    key_matrix.append(row_matrix)
print(f"key_matrix{key_matrix}")
# convert plainText
time = len(plainText)//matrix_input

checkTimePlaintext = 0

textMatrix = []

for i in range(0, time):

    arrPlaintext = []

    for j in range(0, matrix_input):
        arrPlaintext.append(english_characters.find(
            plainText[checkTimePlaintext]))
        checkTimePlaintext += 1
    textMatrix.append(arrPlaintext)
print(f"Text Matrix{textMatrix}")

# mutilate Plain_text_matrix with key_matrix
detM = int(np.linalg.det(key_matrix))

print(f"detM :{detM}")

mod_det = np.mod(detM, 26)

print(f"mod_det {mod_det}:")

key = Matrix(key_matrix)

print(f"key:{key}")

adj = key.adjugate()

print(f"adj:{adj}")

adj_mod = np.mod(adj, 26)

print(f"adj_mod:{adj_mod}")

x= 0

while (mod_det*x)%26 != 1%26:
    x += 1
   
inverse = np.mod(np.dot(x, adj_mod), 26)

print(f"inverse:{inverse}")

cipherText = ''

for element in textMatrix:
    multiplyMatrix = np.mod(np.dot(element,inverse), 26)
    print(f"multiplyMatrix: {multiplyMatrix}")
    for letterChange in multiplyMatrix:
        print(f"letterChange: {letterChange}")
        print(f"english_characters[letterChange]: {english_characters[letterChange]}")

        cipherText += english_characters[letterChange]


print(cipherText)
