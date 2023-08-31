import string

import numpy as np

plainText = input("Enter The plain text: ").replace(" ", "").upper()

matrix_input =input("Enter 2 for matrix 2x2 and 3 for matrix 3x3:")

if matrix_input.isdecimal():
    matrix_input=int(matrix_input)
    if matrix_input ==2 or matrix_input ==3:
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

        checknumTime = len(plainText) % matrix_input

        time = len(plainText)//matrix_input

        if checknumTime != 0:

            time += 1;

        checkTimePlaintext = 0

        textMatrix = []

        for i in range(0, time):

            arrPlaintext = []

            for j in range(0, matrix_input):
                if checkTimePlaintext < len(plainText):
                    arrPlaintext.append(english_characters.find(plainText[checkTimePlaintext]))
                    checkTimePlaintext+=1

                elif checkTimePlaintext==len(plainText):

                    for x in range(matrix_input-j):

                        arrPlaintext.append(english_characters.find("X"))
                    checkTimePlaintext+=1


            textMatrix.append(arrPlaintext)
        print(f"Text Matrix{textMatrix}")

        # mutilple Plain_text_matrix with key_matrix
        ciperText=''

        for element in textMatrix:

            mutipleMatrix=np.mod(np.dot(element,key_matrix),26)

            for letterChnage in mutipleMatrix:

                ciperText+= english_characters[letterChnage]

        print(ciperText)
    else:
        print("we are can only handle 2x2 or 3x3 matrices")
else:
    print("You need to input as the number 2 or 3 .It must not as a String")





            




