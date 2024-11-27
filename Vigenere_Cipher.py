 Algorithm:
1. Generate the Key: Repeat the keyword to match the length
of the plaintext.
2. Encryption: For each letter in the plaintext, shift it by the
corresponding letter in the key (both letters are converted to
numbers, then shifted modulo 26).
3. Decryption: Reverse the shift for each letter of the ciphertext
using the corresponding letter in the key.



def vigenere_encrypt(message, key):
    encrypted = ""
    key_index = 0
    key = key.upper()

    for char in message:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            key_index += 1  # Move to the next letter in the key
        else:
            encrypted += char  # Non-alphabetic characters are unchanged
    return encrypted


def vigenere_decrypt(encrypted_message, key):
    decrypted = ""
    key_index = 0
    key = key.upper()

    for char in encrypted_message:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted += chr((ord(char) - ord(base) - shift) % 26 + ord(base))
            key_index += 1  # Move to the next letter in the key
        else:
            decrypted += char  # Non-alphabetic characters are unchanged
    return decrypted


# User input
message = input("Enter the message: ")
key = input("Enter the key: ")

# Encrypt and decrypt the message
encrypted_message = vigenere_encrypt(message, key)
decrypted_message = vigenere_decrypt(encrypted_message, key)

# Display results
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
