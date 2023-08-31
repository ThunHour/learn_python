import string

# digits = string.digits => 0 not in 0123456789
# ascii_letter = string.ascii_letters
# hex_digits = string.hexdigits
# oct_digit = string.octdigits
# printables = string.printable
# lowercase_letters = string.ascii_lowercase
# uppercase_letters = string.ascii_uppercase
#
# print(digits)
# print(ascii_letter)
# print(hex_digits)
# print(oct_digit)
# print(printables)
# print(lowercase_letters)
# print(uppercase_letters)


def find_num(n):
    non_numbers=[]
    if n.isdigit():
        num = int(n)
        print(num*10)
    else:
        for i in n:
            if i not in string.digits:
                   non_numbers.append(i)
        print("The following are not numbers and can't be convered...", non_numbers)

find_num("10")
