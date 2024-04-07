import random

print('''
MM"""""""`MM MP""""""`MM MMP"""""""MM 
MM  mmmm,  M M  mmmmm..M M' .mmmm  MM 
M'        .M M.      `YM M         `M 
MM  MMMb. "M MMMMMMM.  M M  MMMMM  MM 
MM  MMMMM  M M. .MMM'  M M  MMMMM  MM 
MM  MMMMM  M Mb.     .dM M  MMMMM  MM 
MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM
''')

# Function to calculate the greatest common divisor of two numbers using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate the modular inverse of a number 'a' modulo 'm' using extended Euclidean algorithm
def mod_inv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to generate a public-private key pair for RSA encryption
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = mod_inv(e, phi)

    return ((e, n), (d, n))

# Function to encrypt a plaintext message using the public key
def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

# Function to decrypt a ciphertext message using the private key
def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# Generate key pair with prime numbers p and q
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

# Encryption process
plaintext = input("Enter the message to encrypt: ")
cipher_text = encrypt(public_key, plaintext)
print("Encrypted message:", cipher_text)

# Decryption process
decrypted_text = decrypt(private_key, cipher_text)
print("Decrypted message:", decrypted_text)
