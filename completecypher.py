def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():  # Encrypting uppercase letters
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:  # Encrypting lowercase letters
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():  # Decrypting uppercase letters
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:  # Decrypting lowercase letters
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

# Main program
print("1. Encryption\n2. Decryption") 
ch = int(input("Enter your choice (1 or 2): "))

# Handling encryption and decryption based on user choice
if ch == 1:
    text = input("Enter the text you want to encrypt: ")
    s = int(input("Enter the number by which you want to encrypt: "))
    print("Text  : " + text)
    print("Shift : " + str(s))
    print("Cipher: " + encrypt(text, s))
elif ch == 2:
    text = input("Enter the text you want to decrypt: ")
    s = int(input("Enter the number by which you want to decrypt: "))
    print("Text  : " + text)
    print("Shift : " + str(s))
    print("Plaintext: " + decrypt(text, s))
else:
    print("Invalid choice. Please choose 1 for encryption or 2 for decryption.")
