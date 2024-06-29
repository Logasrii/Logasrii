def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
            elif char.isupper():
                start = ord('A')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
            
    return result

# Example usage
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print(f"Encrypted Text: {encrypted_text}")
