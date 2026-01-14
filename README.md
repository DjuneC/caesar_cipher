# Caesar Cipher

This project implements a basic Caesar cipher for encrypting and decrypting text.

## Description

The Caesar cipher is a simple substitution cipher where each letter in the plaintext is replaced by a letter some fixed 
number of positions down the alphabet. This project takes user input to determine whether to encode or decode, the message 
to process, and the shift value (key).

## How to Use

1.  **Run the Code:**  Execute the Python script (e.g., `python caesar.py`).
2.  **Choose Mode:** The program will prompt you to select `encode` or `decode`.
3.  **Enter Message:**  Type the message you want to encrypt or decrypt.
4.  **Enter Shift Value:**  Enter the integer shift value (key).

## Example

Let's say you want to encode the message "hello" with a shift of 3:

```
Enter mode (encode/decode): encode
Enter message: hello
Enter shift value: 3
Encoded message: khoor
```

## Code

https://github.com/DjuneC/caesar_cipher.git

## Notes

*   This is a simplified implementation and does handle upper-case letters or spaces.
*   The shift value is applied modulo 26 to wrap around the alphabet.

## Author

Arana
