"""
Secure Login System

This project demonstrates:
- Salted password hashing using PBKDF2-HMAC-SHA256
- Hash-based password verification
- Failed login attempt limiting
- Basic error handling

For learning and portfolio demonstration purposes only.
"""

import hashlib
import hmac
import os


MAX_ATTEMPTS = 3
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


def verify_password(entered_password: str, stored_salt: bytes, stored_hash: bytes) -> bool:
    """
    Verify an entered password by hashing it with the stored salt
    and comparing it with the stored hash.
    """

    _, entered_hash = hash_password(entered_password, stored_salt)

    return hmac.compare_digest(entered_hash, stored_hash)


def create_sample_user():
    """
    Create one sample user account.

    The sample plaintext password is used only to generate the hash.
    Only the salt and hash are stored in the user record.
    """

    username = "admin"
    salt, password_hash = hash_password("Password123")

    return {
        "username": username,
        "salt": salt,
        "password_hash": password_hash
    }


def login(user):
    """
    Prompt the user for login details and allow a limited number of attempts.
    """

    attempts = 0

    print("=== Secure Login System ===")
    print("Demo account: username = admin, password = Password123")
    print()

    while attempts < MAX_ATTEMPTS:
        entered_username = input("Username: ").strip()
        entered_password = input("Password: ").strip()

        username_matches = entered_username == user["username"]
        password_matches = verify_password(
            entered_password,
            user["salt"],
            user["password_hash"]
        )

        if username_matches and password_matches:
            print("\nAccess granted. Login successful.")
            return True

        attempts += 1
        remaining_attempts = MAX_ATTEMPTS - attempts

        print("\nInvalid username or password.")

        if remaining_attempts > 0:
            print(f"Attempts remaining: {remaining_attempts}\n")

    print("\nAccess denied. Too many failed login attempts.")
    return False


def main():
    """
    Main program function.
    """

    try:
        sample_user = create_sample_user()
        login(sample_user)

    except KeyboardInterrupt:
        print("\nProgram exited by user.")

    except EOFError:
        print("\nInput ended unexpectedly.")

    except Exception:
        print("\nAn unexpected error occurred. Please try again later.")


if __name__ == "__main__":
    main()
