import math

def encrypt(plaintext, key):
    num_cols = math.ceil(len(plaintext) / key)
    
    matrix = ['' for _ in range(num_cols)]

    for i, char in enumerate(plaintext):
        column = i % num_cols
        matrix[column] += char

    ciphertext = ''.join(matrix)
    return ciphertext

def decrypt(ciphertext, key):
    num_cols = math.ceil(len(ciphertext) / key)
    num_rows = key

    num_shaded_boxes = num_cols * num_rows - len(ciphertext)
    
    matrix = ['' for _ in range(num_rows)]

    col = 0
    row = 0
    for char in ciphertext:
        matrix[row] += char
        row += 1
        if row == num_rows or (col == num_cols and row >= num_shaded_boxes):
            row = 0
            col += 1

    plaintext = ''.join(matrix)
    return plaintext


if __name__ == "__main__":
    key = 4  
    plaintext = "This is a transposition cipher example."

    encrypted_message = encrypt(plaintext, key)
    print(f"Encrypted: {encrypted_message}")
    
    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted: {decrypted_message}")
