import string

def create_cipher(key):
    alphabet = string.ascii_lowercase
    cipher_dict = {}
    
    shifted_alphabet = alphabet[key:] + alphabet[:key]

    for i in range(len(alphabet)):
        cipher_dict[alphabet[i]] = shifted_alphabet[i]
    
    return cipher_dict

def encrypt(plaintext, key):
    cipher_dict = create_cipher(key)
    ciphertext = []

    for char in plaintext:
        if char.isalpha():
            char_lower = char.lower()
            encrypted_char = cipher_dict[char_lower]

            if char.isupper():
                encrypted_char = encrypted_char.upper()
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)

    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    cipher_dict = create_cipher(key)
    reverse_cipher_dict = {v: k for k, v in cipher_dict.items()}
    
    plaintext = []

    for char in ciphertext:
        if char.isalpha():
            char_lower = char.lower()
            decrypted_char = reverse_cipher_dict[char_lower]

            if char.isupper():
                decrypted_char = decrypted_char.upper()
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)

    return ''.join(plaintext)

if __name__ == "__main__":
    key = 3 
    plaintext = "Hello, World!"
    
    
    encrypted_message = encrypt(plaintext, key)
    print(f"Encrypted: {encrypted_message}")
    
    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted: {decrypted_message}")
