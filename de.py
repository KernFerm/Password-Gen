import secrets
import string
from cryptography.fernet import Fernet
import os

def view_saved_passwords():
    key_path = "secure_folder/encryption.key"
    encrypted_file_path = "secure_folder/passwords.enc"
    
    if not os.path.exists(key_path) or not os.path.exists(encrypted_file_path):
        print("No passwords found.")
        return
    
    with open(key_path, "rb") as key_file:
        key = key_file.read()
    cipher = Fernet(key)
    
    with open(encrypted_file_path, "rb") as encrypted_file:
        for line in encrypted_file:
            encrypted_password = line.strip()
            print("Decrypted Password:", cipher.decrypt(encrypted_password).decode())

view_saved_passwords()