# A message
# A shift for each letter
# Final result will be the encoded message after shifting all letters

import string
from cipher_ascii_art import caesar_cipher_ascii

alphabet = string.ascii_lowercase

def caesar_cipher(message: str, shift: int) -> str:
    
    encode_message = []

    for letter in message:
        
        if any([letter in string.punctuation, letter in string.whitespace]):
            encode_message += letter
            continue

        index_in_alphabet = alphabet.index(letter.lower())

        new_index = (index_in_alphabet + shift) % len(alphabet)

        shift_letter = alphabet[new_index]

        encode_message.append(shift_letter if letter.islower() else shift_letter.upper())
    
    return "".join(encode_message)

def get_user_input():
    
    while True:
        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n--> ")

        message: str = input("Type your message:\n--> ")

        shift: int = int(input("Type your shift number:\n--> "))

        if choice == 'encode':
            print(f"Here is the encoded result: {caesar_cipher(message, shift)}")
        elif choice == 'decode':
            print(f"Here is the decoded result: {caesar_cipher(message, -shift)}")
        else:
            print("ERROR: Input must be 'encode' or 'decode'")

        keep_going = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n--> ")

        if keep_going == 'yes':
            continue
        
        break

def main():
    print(caesar_cipher_ascii)
    get_user_input()

if __name__ == "__main__":
    main()
