#RSA Decryption at the Receiver End

#Step 3 : Decryption : C^d mod n = M

C = input("Enter the Cipher Text : ")

print("Enter the Private Key of Receiver { d , n } : ")

d = int(input("Enter the value of [d] : "))

n = int(input("Enter the value of [n] : "))

print("Private Key of Receiver is { " + str(d) + " , " + str(n) + " } ")

M = '' # Original Plain Text

for char in C :

    M += chr(pow(ord(char) , d , n))


print("The Original Message (M) = C^d mod n = " , M)
