import secrets
import string
from cryptography.fernet import Fernet
import os

def view_saved_passwords():
    """
    Decrypts and displays saved passwords securely.
    Includes improved error handling and optional secure debugging.
    """
    key_path = "secure_folder/encryption.key"
    encrypted_file_path = "secure_folder/passwords.enc"
    
    # Check if key or encrypted file exists
    if not os.path.exists(key_path) or not os.path.exists(encrypted_file_path):
        print("No passwords found or encryption key is missing.")
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
                    print("- Decrypted Password:", decrypted_password)
                except Exception as e:
                    print("- Error decrypting password:", str(e))
    except Exception as e:
        print("Error occurred while viewing passwords:", str(e))

# Call the function to view passwords
if __name__ == "__main__":
    view_saved_passwords()
