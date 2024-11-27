ALGO
1. Define a function Caesar_cipher with the text and shift value as 
parameters. 
2. Initialize an empty string to store the final result. 
3. Use a for loop to traverse the text. a. If character in the text is 
uppercase result += chr((ord(char) + s - 65) % 26 + 65) b. If 
char is lowercase result += chr((ord(char) + s - 97) % 26 + 97) c. 
Else append the character as it is to the result. 
4. Return the final result. 
5. Take input from the user for plain or cipher text. 
6. Take input from the user for the shift value. For encryption: +ve 
shift value and for decryption: -ve shift value. 
7. Call function Caesar_cipher().

CODE
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
