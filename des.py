from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# Function to pad data to be a multiple of 8 bytes
def pad(data):
    while len(data) % 8 != 0:
        data += b' '
    return data

# Single DES encryption/decryption
def single_des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    return cipher.encrypt(padded_text)

def single_des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(ciphertext).rstrip(b' ')

# Double DES encryption/decryption
def double_des_encrypt(plaintext, key1, key2):
    first_pass = single_des_encrypt(plaintext, key1)
    second_pass = single_des_encrypt(first_pass, key2)
    return second_pass

def double_des_decrypt(ciphertext, key1, key2):
    first_pass = single_des_decrypt(ciphertext, key2)
    second_pass = single_des_decrypt(first_pass, key1)
    return second_pass

# Triple DES encryption/decryption
def triple_des_encrypt(plaintext, key1, key2, key3):
    first_pass = single_des_encrypt(plaintext, key1)
    second_pass = single_des_decrypt(first_pass, key2)
    third_pass = single_des_encrypt(second_pass, key3)
    return third_pass

def triple_des_decrypt(ciphertext, key1, key2, key3):
    first_pass = single_des_decrypt(ciphertext, key3)
    second_pass = single_des_encrypt(first_pass, key2)
    third_pass = single_des_decrypt(second_pass, key1)
    return third_pass

# Example usage
if __name__ == "__main__":
    plaintext = b"Hello123"
    key1 = b"12345678"
    key2 = b"87654321"
    key3 = b"A1B2C3D4"
    
    # Single DES
    enc1 = single_des_encrypt(plaintext, key1)
    dec1 = single_des_decrypt(enc1, key1)
    print("Single DES Encryption:", binascii.hexlify(enc1))
    print("Single DES Decryption:", dec1)
    
    # Double DES
    enc2 = double_des_encrypt(plaintext, key1, key2)
    dec2 = double_des_decrypt(enc2, key1, key2)
    print("Double DES Encryption:", binascii.hexlify(enc2))
    print("Double DES Decryption:", dec2)
    
    # Triple DES
    enc3 = triple_des_encrypt(plaintext, key1, key2, key3)
    dec3 = triple_des_decrypt(enc3, key1, key2, key3)
    print("Triple DES Encryption:", binascii.hexlify(enc3))
    print("Triple DES Decryption:", dec3)
