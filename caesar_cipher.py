# CAESAR CIPHER FUNCTION


def caesar_encrypt(text, shift):
    """encrypts with a caesar cipher user input with a shift"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""

    for letter in text.lower():
        if letter in alphabet:
            current_index = alphabet.index(letter)
            new_index = (current_index + shift) % 26
            ciphertext += alphabet[new_index]
        elif letter is not alphabet:
            print("ERROR:CAN ONLY CONTAIN LETTERS!")
            return
        else:
            ciphertext += letter
    return ciphertext


# Calling your function
ciphering = input("Input phrase to be ciphered: ")
secret_msg = caesar_encrypt(ciphering, 3)
print(f"The encrypted message is: {secret_msg}")


# CAESAR CIPHER DECRYPTION
def caesar_decrypt(ciphertext, shift):
    """Decrypts caesar_cipher encrypted message."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""

    for cipher in ciphertext.lower():
        if cipher in alphabet:
            current_index = alphabet.index(cipher)
            new_index = (current_index - shift) % 26
            plaintext += alphabet[new_index]
        elif cipher is not alphabet:
            print("ERROR: CIPHER TO DECRYPT MUST CONTAIN LETTERS ONLY!")
            return None
        else:
            plaintext += cipher
    return plaintext


# Calling decrypter
decrypter = input("Enter cipher to be decrypted: ")
decoded_msg = caesar_decrypt(decrypter, 3)
print(f"Decrypted Message: {decoded_msg}")
