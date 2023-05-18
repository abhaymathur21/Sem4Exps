p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))

n = p * q
phi_n = (p - 1) * (q - 1)

e = 7

d = pow(e, -1, phi_n)

M = int(input("Data to encrypt: "))

C = pow(M, e, n)

M_decrypted = pow(C, d, n)

print(f"Public key: ({e}, {n})")
print(f"Private key: ({d}, {n})")
print(f"Encrypted message: {C}")
print(f"Decrypted message: {M_decrypted}")
