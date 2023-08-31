import random 
plain_text=input("Enter the Input String : ")
key=input("Enter the Key : ")
cipher_text=''
for char in plain_text:
    if char.islower():
        cipher_text+=chr(key.index(char)+ord('a'))
    elif char.isupper():
        cipher_text+=chr(key.index(char)+ord('A'))
    else:
        cipher_text+=char
print(f'This is your generated key {key}')
print(cipher_text)
