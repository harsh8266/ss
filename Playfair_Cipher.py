Algorithm:
1. Step 1: Create the 5x5 key matrix.
2. Step 2: Prepare the text into pairs, adding "X" where
necessary.
3. Step 3: Locate each letter's row and column in the matrix.
4. Step 4: Process each pair based on the mode (encryption
or decryption) following Playfair rules.
5. Main Logic: Combine all processed pairs to get the final
encrypted or decrypted text.


def create_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is omitted in Playfair Cipher
    matrix = []
    used = set()

    # Remove duplicates from the key and add to matrix
    for char in key.upper():
        if char not in used and char in alphabet:
            matrix.append(char)
            used.add(char)

    # Fill the rest of the matrix with remaining letters
    for char in alphabet:
        if char not in used:
            matrix.append(char)
            used.add(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]  # Split into a 5x5 grid


def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None


def preprocess_message(message):
    message = message.upper().replace("J", "I")  # Replace 'J' with 'I'
    processed = ""

    # Insert filler 'X' for repeated pairs
    i = 0
    while i < len(message):
        processed += message[i]
        if i + 1 < len(message) and message[i] == message[i + 1]:
            processed += "X"
        else:
            i += 1
        i += 1

    if len(processed) % 2 != 0:  # Add filler if odd length
        processed += "X"

    return processed


def encrypt_playfair(message, matrix):
    message = preprocess_message(message)
    encrypted = ""

    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i + 1]
        row1, col1 = find_position(char1, matrix)
        row2, col2 = find_position(char2, matrix)

        if row1 == row2:  # Same row
            encrypted += matrix[row1][(col1 + 1) % 5]
            encrypted += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted += matrix[(row1 + 1) % 5][col1]
            encrypted += matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle swap
            encrypted += matrix[row1][col2]
            encrypted += matrix[row2][col1]

    return encrypted


def decrypt_playfair(ciphertext, matrix):
    decrypted = ""

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(char1, matrix)
        row2, col2 = find_position(char2, matrix)

        if row1 == row2:  # Same row
            decrypted += matrix[row1][(col1 - 1) % 5]
            decrypted += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted += matrix[(row1 - 1) % 5][col1]
            decrypted += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle swap
            decrypted += matrix[row1][col2]
            decrypted += matrix[row2][col1]

    return decrypted


# User input
key = input("Enter the key: ").replace(" ", "").upper()
message = input("Enter the message: ").replace(" ", "")

# Generate key matrix
key_matrix = create_key_matrix(key)

# Encrypt and decrypt the message
encrypted_message = encrypt_playfair(message, key_matrix)
decrypted_message = decrypt_playfair(encrypted_message, key_matrix)

# Display results
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
