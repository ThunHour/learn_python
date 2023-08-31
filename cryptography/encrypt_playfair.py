import string

plain_text = str(input("enter string:")).replace(" ", "").replace('j', 'i')

english_alphabet = string.ascii_lowercase

english_alphabet = english_alphabet.replace('j', '.')
# capture keyword

keyword = input("Enter keyword:")

# create the key matrix 5x5 - list
key_matrix = ['' for k in range(5)]

# populate the 5x5 key matrix with value
row = 0  # row variable 0<=row<5

column = 0  # column variable 0<=column<5

# Traverse teh keyword and if the char is not present in key matrix add it to the key matrix

for char in keyword:

    if char in english_alphabet:

        key_matrix[row] += char

        english_alphabet = english_alphabet.replace(char, '.')

        column += 1

        if column > 4:

            row += 1

            column = 0

for char in english_alphabet:

    if char != '.':

        key_matrix[row] += char

        column += 1

        if column > 4:

            row += 1

            column = 0

print(key_matrix)

plaintext_digrams = []

i = 0

while i < len(plain_text):

    char1 = plain_text[i]

    char2 = ''

    if i+1 == len(plain_text):

        char2 = 'x'

    else:

        char2 = plain_text[i+1]

    if char1 != char2:

        plaintext_digrams.append(char1+char2)

        i += 2

    else:

        plaintext_digrams.append(char1+'x')

        i += 1

print(plaintext_digrams)

index_diagram = []

for i in range(len(plaintext_digrams)):

    for j in range(2):

        list_index = []

        # j refer to elements of diagram
        for x in range(0, len(key_matrix)):

            # x refter to row for key_matrix
            for y in range(0, len(key_matrix[x])):

                # y refer to column for key_matrix
                if plaintext_digrams[i][j] == key_matrix[x][y]:

                    list_index.extend([x, y])

        index_diagram.append(list_index)

print(index_diagram)
change_index = ""

for t in range(0, len(index_diagram)//2):

    evenIndex = index_diagram[2*t]

    oddIndex = index_diagram[2*t+1]

    if evenIndex[0] == oddIndex[0]:

        change_index += (key_matrix[evenIndex[0]][(evenIndex[1]+1) % 5])

        change_index += (key_matrix[oddIndex[0]][(oddIndex[1]+1) % 5])

    elif evenIndex[1] == oddIndex[1]:

        change_index += (key_matrix[(evenIndex[0]+1) % 5][evenIndex[1]])

        change_index += (key_matrix[(oddIndex[0]+1) % 5][oddIndex[1]])

    else:

        change_index += (key_matrix[evenIndex[0]][oddIndex[1]])

        change_index += (key_matrix[oddIndex[0]][evenIndex[1]])

print(f"chipher text:{change_index}")
