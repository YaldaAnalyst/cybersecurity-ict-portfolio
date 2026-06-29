"""
Password Reset System

This project demonstrates:
- Username validation
- One-time reset code generation using secrets
- Reset-code attempt limiting
- Basic password strength checking
- Salted password hashing using PBKDF2-HMAC-SHA256
- Safe comparison using hmac.compare_digest
- Hidden password input using getpass

For learning and portfolio demonstration purposes only.
"""

import getpass
import hashlib
import hmac
import os
import secrets


MAX_RESET_CODE_ATTEMPTS = 3
ITERATIONS = 600_000


def hash_password(password: str, salt: bytes = None):
    """
    Hash a password using PBKDF2-HMAC-SHA256.

    A random salt is generated if one is not provided.
    The plaintext password is never stored.
    """

    if salt is None:
        salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS
    )

    return salt, password_hash


def is_strong_password(password: str):
    """
    Check whether a password meets basic strength requirements.

    Requirements:
    - At least 8 characters
    - At least one letter
    - At least one number
    """

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    has_letter = any(character.isalpha() for character in password)
    has_number = any(character.isdigit() for character in password)

    if not has_letter:
        return False, "Password must contain at least one letter."

    if not has_number:
        return False, "Password must contain at least one number."

    return True, "Password meets the basic strength requirements."


def create_sample_users():
    """
    Create sample user data.

    The plaintext password is used only to generate the initial hash.
    Only the salt and password hash are stored.
    """

    salt, password_hash = hash_password("OldPassword123")

    users = {
        "admin": {
            "salt": salt,
            "password_hash": password_hash
        }
    }

    return users


def generate_reset_code():
    """
    Generate a one-time reset code.

    secrets.token_hex(3) creates a 6-character hexadecimal code.
    This is used as a learning simulation of a reset code.
    """

    return secrets.token_hex(3)


def verify_reset_code(expected_code: str):
    """
    Ask the user to enter the reset code.

    The user has a limited number of attempts.
    hmac.compare_digest is used for safer comparison.
    """

    attempts = 0

    while attempts < MAX_RESET_CODE_ATTEMPTS:
        entered_code = input("Enter reset code: ").strip()

        if hmac.compare_digest(entered_code, expected_code):
            print("\nReset code verified.")
            return True

        attempts += 1
        remaining_attempts = MAX_RESET_CODE_ATTEMPTS - attempts

        print("\nInvalid reset code.")

        if remaining_attempts > 0:
            print(f"Attempts remaining: {remaining_attempts}\n")

    print("\nPassword reset denied. Too many incorrect reset-code attempts.")
    return False


def reset_password(users):
    """
    Run the password reset workflow.
    """

    print("=== Password Reset System ===")
    print()

    username = input("Enter username: ").strip()

    if username not in users:
        print("\nIf the account exists, password reset instructions will be sent.")
        return False

    reset_code = generate_reset_code()

    print("\nReset code generated.")
    print("Simulation: this code would be sent to the account owner.")
    print(f"Demo reset code: {reset_code}")
    print()

    code_verified = verify_reset_code(reset_code)

    if not code_verified:
        return False

    new_password = getpass.getpass("Enter new password: ")

    is_valid, message = is_strong_password(new_password)

    if not is_valid:
        print(f"\nPassword reset failed. {message}")
        return False

    new_salt, new_hash = hash_password(new_password)

    users[username]["salt"] = new_salt
    users[username]["password_hash"] = new_hash

    print("\nPassword reset successful.")
    print("The new password has been hashed and stored securely.")
    return True


def main():
    """
    Main program function.
    """

    try:
        users = create_sample_users()
        reset_password(users)

    except KeyboardInterrupt:
        print("\nProgram exited by user.")

    except EOFError:
        print("\nInput ended unexpectedly.")

    except Exception:
        print("\nAn unexpected error occurred. Please try again later.")


if __name__ == "__main__":
    main()
