# Author: Aviv Gafni
# Text Security Toolkit

import base64 #import library for base 64 encoding/decoding

def main_menu(): # Main menu function
    print("\nWelcome to the Text Security Toolkit\n")

    print("1. Encrypt a text message using Caesar Cipher")
    print("2. Decrypt a text message using Caesar Cipher")
    print("3. Encode a text message using base64")
    print("4. Decode a text message using base64")
    print("5. Exit program")

def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha(): # Check if character is a letter
            if char.isupper(): # Define starting point of string, based on upper/lower case letter
                start = ord('A') # 65 in ASCII decimal
            else:
                start = ord('a') # 97 in ASCII decimal

            # Convert letter to ASCII decimal number relative to 'start' letter
            letter_pos = ord(char) - start

            # Change letter position based on shift value
            shifted_pos = letter_pos + shift

            # Wrap around alphabet if letter goes past Z (total 26 letters)
            wrapped_pos = shifted_pos % 26 # use modulo operator - reminder after dividing by 26

            new_letter = chr(wrapped_pos + start) # convert ASCII number back to letter
            encrypted_text += new_letter
        else:
            # character is not a letter, add it unchanged
            encrypted_text += char

    return encrypted_text

def base64_encoded(text):
    try: # wrap in Try/Except to handle unusual characters (non-UTF-8)––
        encoded = base64.b64encode(text.encode("utf-8")).decode() # converts string into bytes using UTF-8
        return encoded
    except UnicodeEncodeError:
        print("\nError: Text contains characters that cannot be encoded")

def base64_decoded(text):
    try:
        decoded = base64.b64decode(text).decode("utf-8")
        return decoded
    except ValueError: # Catches errors when text input is not a valid base64
        print("\nInvalid base64 input, unable to decode. Please enter valid base encoded string")
    except UnicodeDecodeError: # Catch error if bytes are not matching valid UTF-8 text
        print("\nUnable to convert decoded bytes to text string")

# Main program code
program = True
while program:

    main_menu()
    choice = input("\nPlease choose from the above menu options: > ")

    if choice == "1":
        text = input("Please enter text to encrypt: ")
        try:
            shift = int(input("Please enter shift value for encryption: "))
            print("Encrypted text:", caesar_cipher(text, shift))
        except ValueError:
            print("\nShift must be a whole number.")

    elif choice == "2":
        text = input("Please enter text to decrypt: ")
        try:
            shift = int(input("Please enter shift value used in encryption: "))
            print("Decrypted text:", caesar_cipher(text, -shift))
        except ValueError:
            print("\nShift must be a whole number.")


    elif choice == "3":
        text = input("Please enter text to encode: ")
        print("Encoded text:", base64_encoded(text))

    elif choice == "4":
        text = input("Please enter text to decode: ")
        print("Decoded text:", base64_decoded(text))

    elif choice == "5":
        print("\nGoodbye, see you next time!")
        program = False

    else:
        print("\nInvalid input, please select a number from the main menu options\n")




