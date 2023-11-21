import cv2
import os
import hashlib
import secrets

# Encryption
img = cv2.imread("internship.jpg")

# Input secret message and password
msg = input("Enter your secret message: ")
password = input('Enter password: ')

# Use hashlib to securely store and compare passwords
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Use secrets module for cryptographic use
secure_random = secrets.SystemRandom()

d = {}  # Dictionary to initialize pixel
c = {}

for i in range(256):  # The range should be 256
    d[chr(i)] = i
    c[i] = chr(i)

m = 0  # Initialize RGB
n = 0
z = 0

for i in range(len(msg)):
    img[m, n, z] = d[msg[i]]
    n = n + 1
    m = m + n
    z = (z + 1) % 3

cv2.imwrite("stegofile.jpg", img)
os.system("start stegofile.jpg")

# Decryption
message = ""  # Declared as string
n = 0
m = 0
z = 0

# Password verification using hashed password
pas = input('Enter your password: ')
if hashed_password == hashlib.sha256(pas.encode()).hexdigest():
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + n
        z = (z + 1) % 3
    print('Decrypted message:', message)
else:
    print("Password not valid")
