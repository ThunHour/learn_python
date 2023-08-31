# Key Generation Python Program

import math as m

# Step 1 : Key Generation ( for the receiver) can be done at both ends

# Receiver Generate both Public Key & Private Key

# Shares the public key to the world (sender encrypts using this)

# Keeps the Private Key Secret to himself (receiver decrypts using this)

p = int(input("Enter the 1st prime number (p) : "))

q = int(input("Enter the 2nd prime number (q) : "))

n = p*q


print("n = p*q = ", str(n))

f_n = (p-1)*(q-1)

print("0(n) = (p-1)*(q-1) = ", str(f_n))


# Find 1 < e < 0(n)

e = 2
while(e < f_n):

    if(m.gcd(e, f_n) == 1):  # e and 0(n) are relatively prime

        print(e)

    e += 1

e = int(input("Select the value of Public Key (e) from above : "))

# Find d such that : ed mod 0(n) = 1 and 1 < d < 0(n)
print("Value of d --> { ed mod 0(n) = 1 } and 1 < d < 0(n)")


d = 2
while(d < f_n):

    if((e*d) % f_n == 1):

        print(d)

    d = d+1

d = int(input("Select the value of Private Key (d) from above : "))

print("Public Key - Pb = { " + str(e) + " , " + str(n) + " } ")

print("Private Key - Pr = { " + str(d) + " , " + str(n) + " } ")


# Encryption RSA Algorithm


# Encryption RSA Algorithm


# Step 2 : Encryption : M^e mod n = C (at the Sender Side)

print()

M = input("Enter the plain text message : ")

print()

print("Enter the Public Key of Receiver { e , n } : ")
print()

e = int(input("Enter the value of [e] : "))

print()

n = int(input("Enter the value of [n] : "))

print()

print("Public Key of Receiver is { " + str(e) + " , " + str(n) + " } ")

C = ""

for char in M:

    C += chr(pow(ord(char), e, n))

print()

print("The Cipher Text C = M^e mod n = ["+C+"]")

print()
