Algorithm:
1. Key Matrix Generation: Define an n×nn \times nn×n matrix as the
key, where nnn is the block size. The matrix should have an inverse
modulo 26 for decryption.
2. Prepare Plaintext: Break the plaintext into blocks of size nnn. If the
length is not a multiple of nnn, pad it with extra characters (e.g.,
"X").
3. Encrypt: Multiply each plaintext vector (converted to numeric
form) by the key matrix and apply modulo 26 to get the ciphertext
vector.
4. Decrypt: Multiply each ciphertext vector by the inverse of the key
matrix (modulo 26) to retrieve the plaintext.

CODE

import numpy as np

def process_key(key, n):
    key = key.upper().replace(" ", "")
    if len(key) < n * n:
        raise ValueError("Key must be at least n * n characters long.")
    
    key_matrix = []
    for i in range(n):
        row = [ord(key[j]) - 65 for j in range(i * n, (i + 1) * n)]
        key_matrix.append(row)
    return np.array(key_matrix)


def process_message(message, n):
    message = message.upper().replace(" ", "")
    if len(message) % n != 0:
        message += "X" * (n - (len(message) % n))  # Add padding if necessary
    return [ord(char) - 65 for char in message]


def hill_encrypt(message, key_matrix, n):
    message_vector = np.array(message).reshape(-1, n)
    encrypted_vector = (message_vector @ key_matrix) % 26
    encrypted_message = "".join(chr(num + 65) for num in encrypted_vector.flatten())
    return encrypted_message


def hill_decrypt(encrypted_message, key_matrix, n):
    determinant = int(round(np.linalg.det(key_matrix))) % 26
    if determinant == 0 or np.gcd(determinant, 26) != 1:
        raise ValueError("Key matrix is not invertible in mod 26.")

    key_inverse = np.linalg.inv(key_matrix) * determinant
    key_inverse = np.round(key_inverse).astype(int) * pow(determinant, -1, 26)
    key_inverse %= 26

    encrypted_vector = np.array([ord(char) - 65 for char in encrypted_message]).reshape(-1, n)
    decrypted_vector = (encrypted_vector @ key_inverse) % 26
    decrypted_message = "".join(chr(num + 65) for num in decrypted_vector.flatten())
    return decrypted_message


# User input
n = int(input("Enter the size of the key matrix (e.g., 2 for 2x2): "))
key = input("Enter the key (at least n*n characters): ")
message = input("Enter the message: ")

# Process key and message
key_matrix = process_key(key, n)
message_vector = process_message(message, n)

# Encrypt and decrypt the message
encrypted_message = hill_encrypt(message_vector, key_matrix, n)
decrypted_message = hill_decrypt(encrypted_message, key_matrix, n)

# Display results
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
