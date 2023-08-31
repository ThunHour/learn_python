# Implementation of Digital Signature -DS Usig RSA Encryption - B9

import math as m
import random as rm
import hashlib as hlib

#Create hash function H(M)

def H(M):

##    bits = ''
##
##    for char in M:
##
##        bits += format(ord(char) , '08b')
##
##    print()
##
##    hash_code = bits

    hash_code = hlib.sha512(M.encode())

    print("Hash Code (M) using SHA-1 = " , hash_code)

    hash_digest = hash_code.hexdigest()

    return(str(hash_digest))

#generate Keys function : returns e , d

def Generate_Keys(p , q):

    n = p * q

    print(" n = p*q = " , n)

    f_n = (p - 1) * (q - 1)

    print("O(n) = (p-1)*(q-1) = " , f_n)

    public_key_chain = []

    #Find 'e' = Pub Key s.t. 1 < e < O(n)

    for e in range(f_n):

        if(m.gcd(e , f_n) == 1):

            public_key_chain.append(e)

    print("Public Key List : ")

    print(public_key_chain)

    e = rm.choice(public_key_chain)

    print("The Public Key [e] = " , e)

    #Calculate the value of 'd' = private key s.t. d --> { ed mod f_n = 1 } && 1 < d < f_n

    d = 2

    while(d < f_n):

        if((e*d) % f_n == 1):

            break

        else:

            d = d + 1


    print("Private Key [d] = " , d)

    return (e , d , n)


# Encrypt the hash digest / h using private key of the sender

def Encrypt_hash(plianText , Pr_S , n):

    # encryption using RSA in digital signature : m^d mod n

    S = ''

    for char in plianText:

        S += chr(pow(ord(char) , Pr_S , n))

    return S


#Decryption Function

def Decrypt_Signature(signature_received , Pb_S , n):

    decr_sign = ''

    for char in signature_received:

        decr_sign += chr(pow(ord(char) , Pb_S , n))

    return(decr_sign)

##Step 1  : Enter the actual message M

M = input("Enter the message to be signed (M) : ")

##Step 2 : Create a fairly secure hash function and calculate the hash digest (h) = H(M)

h = H(M)

print("Hash(M) = h = " , h)

##Step 3 : Encrypt the hash digest (h) using RSA / any other public key crypto system
##         and create the digital signature (s) = E(h , Pr_S)

#Input prime numbers p and q for key generation

p = int(input("Enter the 1st Prime number [p] : "))

q = int(input("Enter he 2nd Prime Number [q] : "))

Pb_S , Pr_S , n = Generate_Keys(p , q)

print("Public Key (Pb_S) : { "+str(Pb_S)+" , " + str(n) + " }")

print("Private Key (Pr_S) : { "  +str(Pr_S)+ " , " + str(n) + " }")

digital_signature = Encrypt_hash(h , Pr_S , n)

print("Digital Signature [s] = " , digital_signature)

##Step 4 : Send (M , S) —> receiver

print("*************************************************************************")
print("RECEIVER SIDE")

print("*************************************************************************")

M_received = input("Enter the message received : ")

##Step 5 : Calculates H (M_received) = h_received (by receiver)

h_received = H(M_received)

print("Hash value of the received message h` = " , h_received)

signature_received = input("Enter the received Signature : ")


##Step 6 : Decrypts the D(s , Pub_S , n) = sig_decrypt

sign_decrypted = Decrypt_Signature(signature_received , Pb_S , n)

##Step 7 : if (h = h_received) then digital signature verified else not verified

if(h_received == sign_decrypted):

    print("Sinature Verified. Message is Authentic")

else:

    print("Authentication Failed !!!")
    

    