# Secure Login System

## Overview

This project demonstrates a secure login system using Python.

The program validates a username and password, stores passwords as salted hashes instead of plaintext, limits failed login attempts, and provides clear error messages. It was created to practise authentication, access control, defensive programming, password hashing, and error handling.

## Skills Demonstrated

- Python scripting
- Authentication
- Access control
- Password hashing
- Salted password storage
- Login attempt limiting
- Error handling
- User input validation
- Security-focused documentation

## Security Relevance

Authentication is an important part of protecting systems and user accounts.

This project demonstrates how a login system can:

1. Avoid storing plaintext passwords
2. Store salted password hashes
3. Compare password hashes during login
4. Reduce repeated failed login attempts
5. Deny access after too many incorrect attempts
6. Handle user input safely

## How The Program Works

The program:

1. Creates a sample user account
2. Hashes the password using PBKDF2 with a random salt
3. Stores the salt and password hash
4. Asks the user to enter a username and password
5. Hashes the entered password using the stored salt
6. Compares the generated hash with the stored hash
7. Allows a maximum number of failed login attempts
8. Denies access after too many failed attempts

## What I Learned

Through this project, I practised:

- Writing Python functions
- Using conditional logic
- Handling user input
- Creating basic authentication logic
- Hashing passwords instead of storing plaintext passwords
- Limiting failed login attempts
- Applying security thinking to code
- Explaining a technical project clearly

## Future Improvements

Future improvements could include:

- Password strength validation
- Account lockout timer
- Logging failed login attempts
- Reading users from a CSV file or database
- Adding a password reset function
- Adding multi-factor authentication simulation

## Author

Created and documented by Yalda.

## Disclaimer

This project is for learning and portfolio demonstration purposes only. It is not designed for production use.
