def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Leave other characters unchanged
        else:
            result += char

    return result

# Input text
text = "Hello, World!"
shift = 3

# Encrypt the text
encrypted_text = caesar_cipher(text, shift, mode='encrypt')
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the text
decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print(f"Decrypted Text: {decrypted_text}")

