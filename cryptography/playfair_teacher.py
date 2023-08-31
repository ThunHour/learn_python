import string


# ===============================Step 0: create key matrix(5x5)


# Generate English alphabet (a-z) by replace j with .
englishAlphabet = string.ascii_lowercase.replace("j",".")

#Get keyword from user
keyword = input("Enter keyword: ")


#Create key matrix[5x5]
keyMatrix = ["" for i in range(5)]

# Populate 5x5 key matrix with values keywords and other English alphabets
row = 0 #0 < row <5
column = 0 #0 <column < 5



# Loop for each char in keyword in English alphabets
for char in keyword:

    if char in englishAlphabet:
        keyMatrix[row] += char #if it is in, put it in key matrix 

        englishAlphabet = englishAlphabet.replace(char,".")

        #One char for one column 
        column += 1 


        if column >4:
            row += 1
            column = 0 #

#Add the rest of the characters in English alphabets into Keymatrix
for char in englishAlphabet:
    if char != ".":
        
        keyMatrix[row] += char 
        column += 1  

        if column > 4:
            row += 1 
            column = 0 

print(keyMatrix)
# ===============================Step 1: create diagram 

# get plain text by remove space and replace j with i
plainText = input("Enter a plain text: ").replace(" ","").replace("j","i")


# create/ split the modified plain_text to diagram 

plainText_diagram = []

i = 0 

while i < len(plainText):

    #char1char2 
    char1 = plainText[i] #char1 represents first character 
    char2 = "" #char2 represents second character 

    #================= To check if len of the text is odd or even

    # If there is only one char at the end of the text (len(plainText) = odd)
    if (i+1) == len(plainText):
        char2 = "x"

    else:
        char2 = plainText[i+1]

    #=========================================

    if char1 != char2:

        plainText_diagram.append(char1 + char2)

        i += 2 #because they take 2 chars so we need to skip 2 

    else:

        plainText_diagram.append(char1 + "x")
        i += 1 #because it also take 1 chars so we need to skip only 1 

print(plainText_diagram)


# ===============================Step 2: change char with others key matrix  

cipherTextPairs = []

# when both chars stay in the same row

for pair in plainText_diagram:
    
    applied_rule = False 

    for row in keyMatrix:

        if pair[0] in row and pair[1] in row: #to check if both of them are the same row 

            # captured the column numbers of both characters in plain text diagram
            colum0 = row.find(pair[0])

            colum1 = row.find(pair[1])


            rowPair = row[(colum0 + 1) % 5] + row[(colum1 + 1) % 5]

            cipherTextPairs.append(rowPair)

            applied_rule = True 

    if applied_rule:
        continue


# when both chars stay in the same column
    for column in range(5):

        col = "".join([keyMatrix[row][column] for row in range(5)]) #each row for a particular column 

        if pair[0] in col and pair[1] in col:

            row0 = col.find(pair[0])     
            row1 = col.find(pair[1])


            columnPair = col[(row0 + 1) % 5] + col[(row1 + 1) % 5]

            cipherTextPairs.append(columnPair)

            applied_rule = True 

    if applied_rule:
        continue
        

    # row and column of first chars
    row0 = 0 
    colum0 = 0 

    # row and column of second chars
    row1 = 0 
    colum1 = 0 

    for i in range(5):

        row = keyMatrix[i]

        if pair[0] in row: 
            row0 = i 
            colum0 = row.find(pair[0]) 

        if pair[1] in row: 

            row1 = i 
            colum1 = row.find(pair[1])

    keyPair = keyMatrix[row0][colum1] + keyMatrix[row1][colum0]
    
    cipherTextPairs.append(keyPair)

print(cipherTextPairs)