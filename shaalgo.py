import hashlib

def generate_sha256_hash(data):
    """Generates a SHA-256 hash for the given data."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))  # Encode the data to bytes
    return sha256_hash.hexdigest()

def generate_sha512_hash(data):
    """Generates a SHA-512 hash for the given data."""
    sha512_hash = hashlib.sha512()
    sha512_hash.update(data.encode('utf-8'))  # Encode the data to bytes
    return sha512_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    data = "InformationSecurity"
    print("Original Data:", data)
    print("SHA-256 Hash:", generate_sha256_hash(data))
    print("SHA-512 Hash:", generate_sha512_hash(data))