import secrets
import string
from cryptography.fernet import Fernet
import os

def view_saved_passwords():
    """
    Securely decrypts and displays saved passwords with enhanced error handling.
    Provides clear feedback on missing files and decryption errors.
    """
    key_path = "secure_folder/encryption.key"
    encrypted_file_path = "secure_folder/passwords.enc"

    # Check if key or encrypted file exists
    if not os.path.exists(key_path):
        print("Encryption key not found. Please ensure 'secure_folder/encryption.key' exists.")
        return
    if not os.path.exists(encrypted_file_path):
        print("No saved passwords found. Please ensure 'secure_folder/passwords.enc' exists.")
        return

    try:
        # Read the encryption key
        with open(key_path, "rb") as key_file:
            key = key_file.read()
        cipher = Fernet(key)
        
        # Decrypt and display saved passwords
        print("Saved Passwords:")
        with open(encrypted_file_path, "rb") as encrypted_file:
            for line in encrypted_file:
                encrypted_password = line.strip()
                try:
                    decrypted_password = cipher.decrypt(encrypted_password).decode()
                    print(f"- Decrypted Password: {decrypted_password}")
                except Exception:
                    print("- Error decrypting a password. Skipping...")
    except Exception as e:
        print(f"Error occurred while viewing passwords: {e}")

# Call the function to view passwords
if __name__ == "__main__":
    view_saved_passwords()
