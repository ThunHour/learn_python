import random as rm
import sympy as sp
p = sp.randprime(0, 1000)
print("prime number :"+str(p))

a = sp.randprime(0, 200)

print("primitive number :"+str(a))

private_Key_Alive = int(input("Enter the private key (X) of Alice :"))

private_Key_Bob = int(input("Enter the private key (Y) of Bob :"))

pb_A = pow(a, private_Key_Alive, p)

pb_B=pow(a, private_Key_Bob, p)

print("public key of Alice :"+str(pb_A))

print("public key of Bob :"+str(pb_B))

sk_A=pow(pb_B, private_Key_Alive,p)

print(f"Session Key of Alice: {sk_A}")

sk_B=pow(pb_A, private_Key_Bob, p)

print(f"Session Key of Alice: {sk_B}")

