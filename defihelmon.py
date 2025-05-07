from sympy import isprime, nextprime
import random

def encrypt(msg, shift):
    encrypted_msg = []
    for ch in msg:
        if ch.isupper():
            enc = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            encrypted_msg.append(enc)
        else:
            encrypted_msg.append(ch)  # skip non-alphabet
    return ''.join(encrypted_msg)

def decrypt(msg, shift):
    decrypted_msg = []
    for ch in msg:
        if ch.isupper():
            dec = chr((ord(ch) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_msg.append(dec)
        else:
            decrypted_msg.append(ch)
    return ''.join(decrypted_msg)

def main():
    # Step 1: Input p, g, a, b
    p = int(input("Enter prime number (p): "))
    g = int(input("Enter primitive root (g): "))
    
    # Ensure p is prime
    if not isprime(p):
        print("Error: p must be a prime number.")
        return

    # Generate private keys for Alice and Bob
    a = random.randint(1, p - 1)  # Alice's private key
    b = random.randint(1, p - 1)  # Bob's private key

    # Step 2: Generate public keys
    A = pow(g, a, p)  # Alice's public key
    B = pow(g, b, p)  # Bob's public key

    # Step 3: Generate shared secret
    shared_secret = pow(B, a, p)  # (g^b)^a mod p

    print(f"\nShared Secret: {shared_secret}")

    # Step 4: Encrypt message using Caesar cipher with shared_secret as key
    message = input("\nEnter message to encrypt (uppercase letters only): ").upper()

    shift = shared_secret % 26  # keep within alphabet
    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    # Step 5: Output
    print(f"\nEncrypted Message: {encrypted}")
    print(f"Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
