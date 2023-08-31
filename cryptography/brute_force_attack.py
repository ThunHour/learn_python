import string

def decrypt(text):
    plain = ""

    for s in range(1,25): 

        for dchar in text:

            # Decrypt Upper Case
            if(dchar.isupper()):
                plain += chr((ord(dchar) - s - 65) % 26 + 65)
                
            elif(dchar.isspace()):
              plain += dchar

            elif(dchar.isdigit()):
                y = 0
                y = int(dchar)
                y = ((10 - s) + y)%10
                # P = 9 , 3 = 12%10 Cipher = 2 =y
                # (10 -3) + 2 = 7 +2 = 9
                plain += str(y)

            else:
                plain += chr((ord(dchar) - s - 97) % 26 + 97)

        plain += "\n"

    return plain

# Decryption Function Ends Here

# Capture the Plain Text

text = str(input("Enter the Cipher Text to be cracked: "))

plain_text = decrypt(text)

print("The Decrypted Plain Texts are : " + plain_text)