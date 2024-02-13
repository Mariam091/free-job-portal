# User Registration and Login System
This repository contains a simple user registration and login system implemented in Python. Users can register with their name, surname, and email, and log in securely using their credentials

## Features

    Registration: Users can register by providing their name, surname, email, and a secure password.
    Login: Registered users can log in using their email and password.
    Password Security: Passwords are hashed using the SHA-256 algorithm for secure storage.

## Descriptors
validmail.py,validname.py,validpassword.py,validsurname.py: Contains descriptor classes for validating user inputs (e.g., NameValidator, SurnameValidator, EmailValidator, PasswordValidator).

## Files
main.py: Contains the main functionality for user interaction.
register.py: Module for validating user registration data.
login.py: Module for user login functionality.

## Dependencies

    Python 3.x
    getpass: A Python library for getting passwords from the user without displaying them on the screen.
    hashlib: A Python library for secure hash and message digest algorithms.
    
## Usage

    Run the program by executing python main.py in your terminal.
    Follow the prompts to register, login, or exit the program.
    When registering, you will be asked to provide your name, surname, email, and password.
    When logging in, you will be prompted to enter your email and password.
    After successful login, you will be presented with a menu to perform various actions (e.g., set name, set surname, set password).
