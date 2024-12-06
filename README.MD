# Password Gen

**Password Gen** is a Python-based tool for securely generating, encrypting, and managing passwords. It utilizes `cryptography` for encryption and ensures that passwords are safely stored.

## Features

- **Password Generation:** Generate highly secure and customizable passwords with options for length, character types, and exclusion of similar-looking characters.
- **Password Encryption:** Encrypt and save passwords securely using the Fernet encryption from `cryptography`.
- **Password Decryption:** View stored passwords by decrypting them securely.

## Files

- `main.py`: Contains the main functions for password generation, encryption, and secure storage.
- `de.py`: Handles the decryption and viewing of saved passwords.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Installation

1. Clone this repository:
```
git clone https://github.com/kernferm/password-gen.git
cd password-gen
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

## Usage

### Generating and Saving Passwords

1. Run the `main.py` script:

```
python main.py
```
- Run the `main-launcher.bat` to run the application.

2. A secure password will be generated, encrypted, and saved in the `secure_folder/passwords.enc` file.

### Viewing Saved Passwords

1. Run the `de.py` script:

```
python de.py
```
- Run the `decrypt.bat` to show your password.

2. The script will decrypt and display all stored passwords.


## Customization

You can customize password generation in `main.py` using the following parameters:

- `length`: Length of the password (default: 16).

- `use_uppercase`: Include uppercase letters (default: `True`).

- `use_digits`: Include digits (default: `True`).

- `use_special`: Include special characters (default: `True`).

- `exclude_similar`: Exclude visually similar characters like `O`, `0`, `l`, `1` (default: `False`).

**Example**:

```
generated_password = generate_password(length=20, exclude_similar=True)
```

## Security Considerations

- Ensure that the `secure_folder/encryption.key` file is stored securely. Losing this key will make it impossible to decrypt the stored passwords.
- Do not share the `passwords.enc` file without the corresponding encryption key.

## Requirements

- Python `3.11.6 +`

- Required Python packages:

    ```
    cryptography
    ```

## License

**This project is licensed under the MIT License.**
---
---
