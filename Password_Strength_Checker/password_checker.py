# Author: Aviv Gafni
# Password Strength Checker

import string # import string module - Pre-built strings for character validation

print("Welcome to the password strength checker")
print("Password security rules:\n")
print("1. Password must be minimum 12 characters long")
print("2. Password must contain at least one lower case and upper case letter, one digit and one special character")

SPECIAL_CHARS = "!@#$%^&*()" # Valid special characters - at least one required

while True: # Loop until a strong password is entered
    password = input("Please enter your password: ").strip()
    errors = [] # Empty list for storing error messages regarding password requirements
    if len(password) < 12: # Check length of password
        errors.append("- Password is too short, must be minimum 12 characters")
    if not any(char in string.ascii_lowercase for char in password): # Check for at least one lowercase letter
        errors.append("- Password must contain at least one lower case letter")
    if not any(char in string.ascii_uppercase for char in password): # Check for at least one uppercase letter
        errors.append("- Password must contain at least one upper case letter")
    if not any(char in string.digits for char in password): # Check for at least one digit
        errors.append("- Password must contain at least one digit")
    if not any(char in SPECIAL_CHARS for char in password): # Check for at least one special characters
        errors.append("- Password must contain at least one special character: !@#$%^&*()")

    if not errors: # If list is empty, meaning no errors - password is strong
        print("\nYour password is strong and meeting all security requirements")
        break
    else:
        print("\nYour password is weak, please fix the following:")
        for error in errors: # List which password rule is not met and go back to input new password
            print(error)
