import os
import base64

# Function to decrypt a base64 encoded file
def decrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Fix base64 padding if it's incorrect
    missing_padding = len(file_data) % 4
    if missing_padding:
        file_data += b'=' * (4 - missing_padding)

    try:
        decrypted_data = base64.b64decode(file_data)
    except Exception as e:
        print(f"Error during decryption: {e}")
        return

    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"Decrypted: {file_path}")

# Directory containing the files to decrypt
directory = "/home/immortal/ransomware_test"

# Decrypt the files
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    # Skip decryption of encryption.py and decryption.py
    if os.path.isfile(file_path) and filename not in ['encryption.py', 'decryption.py']:
        decrypt_file(file_path)
