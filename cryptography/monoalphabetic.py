import random
plain_text = input("Enter the Input String : ")
key = []
while True:
    x = chr(random.randint(ord('a'), ord('z')))
    if len(key) == 26:
        break
    elif x not in key:
        key.append(x)
key = ''.join(key)
key_num = []
cipher_text = ''
for char in plain_text:
    if char.islower():
        index = ord(char)-ord('a')
        cipher_text = cipher_text+key[index]
    elif char.isupper():
        index = ord(char)-ord('A')
        cipher_text = cipher_text+key[index]
    elif char.isdecimal():
        t = 0
        t = int(char)
        rand_om = random.randint(0, 10)
        t = (t-rand_om) % 10
        key_num.append(t)
        cipher_text += str(t)
    else:
        cipher_text += char
print(f'This is your generated key {key}')
print(cipher_text)
