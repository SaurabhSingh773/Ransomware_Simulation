#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet, InvalidToken

# Let's find some files
files = []
for file in os.listdir():
    if file == "rans.py" or file == "mykey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# Read the key from the file
with open("mykey.key", "rb") as mykey:
    key = mykey.read()

for file in files:
    try:
        with open(file, "rb") as thefile:
            contents_encrypted = thefile.read()

        # Decrypt the contents using the key
        contents_decrypted = Fernet(key).decrypt(contents_encrypted)

        # Write the decrypted contents back to the file
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

    except InvalidToken:
        print(f"Error decrypting {file}: InvalidToken. Make sure the key matches the one used for encryption.")
    except Exception as e:
        print(f"Error decrypting {file}: {e}")
 
