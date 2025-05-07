def modular_addition(a, b, mod):
    """Performs modular addition: (a + b) % mod"""
    return (a + b) % mod

def modular_subtraction(a, b, mod):
    """Performs modular subtraction: (a - b) % mod"""
    return (a - b) % mod

def modular_multiplication(a, b, mod):
    """Performs modular multiplication: (a * b) % mod"""
    return (a * b) % mod

def modular_exponentiation(base, exp, mod):
    """Performs modular exponentiation: (base^exp) % mod"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

# Example usage
if __name__ == "__main__":
    a = 17
    b = 23
    mod = 5

    print("Modular Addition:", modular_addition(a, b, mod))
    print("Modular Subtraction:", modular_subtraction(a, b, mod))
    print("Modular Multiplication:", modular_multiplication(a, b, mod))
    print("Modular Exponentiation:", modular_exponentiation(a, b, mod))