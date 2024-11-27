def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) - shift) % 26 + ord(base))
        else:
            result += char
    return result


# User input
text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Encrypt and decrypt the message
encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

# Display results
print("Encrypted message:", encrypted_text)
print("Decrypted message:", decrypted_text)
