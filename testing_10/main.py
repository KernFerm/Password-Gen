import secrets
import string
from cryptography.fernet import Fernet
import os

# Generate and save a key for encryption
def generate_encryption_key():
    key_path = "secure_folder/encryption.key"
    os.makedirs("secure_folder", exist_ok=True)
    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
    else:
        with open(key_path, "rb") as key_file:
            key = key_file.read()
    return key

# Save password securely
def save_password_securely(password):
    key = generate_encryption_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    with open("secure_folder/passwords.enc", "ab") as encrypted_file:
        encrypted_file.write(encrypted_password + b"\n")
    print("Password saved securely in 'secure_folder/passwords.enc'.")

# Generate a secure password
def generate_password(
    length=16, use_uppercase=True, use_digits=True, use_special=True, exclude_similar=False
):
    """
    Generate a secure and customizable password.
    
    Args:
        length (int): Length of the password.
        use_uppercase (bool): Include uppercase letters.
        use_digits (bool): Include digits.
        use_special (bool): Include special characters.
        exclude_similar (bool): Exclude visually similar characters (e.g., 'O', '0', 'l', '1').
    
    Returns:
        str: The generated password.
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = "!@#$%^&*()-_=+[]{}|;:,.<>?/" if use_special else ''
    
    if exclude_similar:
        similar_chars = "O0l1I"
        lower = ''.join(c for c in lower if c not in similar_chars)
        upper = ''.join(c for c in upper if c not in similar_chars)
        digits = ''.join(c for c in digits if c not in similar_chars)
        special = ''.join(c for c in special if c not in similar_chars)
    
    all_chars = lower + upper + digits + special
    if not all_chars:
        raise ValueError("At least one character type must be enabled.")
    
    password = []
    if use_uppercase:
        password.append(secrets.choice(upper))
    if use_digits:
        password.append(secrets.choice(digits))
    if use_special:
        password.append(secrets.choice(special))
    
    while len(password) < length:
        password.append(secrets.choice(all_chars))
    
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    generated_password = generate_password(length=20, exclude_similar=True)
    print("Generated Password:", generated_password)
    save_password_securely(generated_password)
