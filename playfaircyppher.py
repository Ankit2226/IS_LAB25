def create_table(key):
    table = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    key = ''.join(sorted(set(key), key=lambda x: key.index(x))) 
    

    for char in key:
        if char not in table:
            table.append(char)
    
    for char in alphabet:
        if char not in table:
            table.append(char)
    
    return [table[i:i+5] for i in range(0, 25, 5)]

def find_position(c, table):
    for i, row in enumerate(table):
        if c in row:
            return i, row.index(c)
    return None, None

def prepare_text(text):
    text = text.upper().replace("J", "I")  
    pairs = []
    
    
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i+1]:
            pairs.append(text[i] + 'X')  
            i += 1
        else:
            pairs.append(text[i:i+2])
            i += 2
            
    if len(pairs[-1]) == 1: 
        pairs[-1] += 'X'
    
    return pairs

def playfair_encrypt(text, key):
    table = create_table(key)
    pairs = prepare_text(text)
    ciphertext = []
    
    for pair in pairs:
        r1, c1 = find_position(pair[0], table)
        r2, c2 = find_position(pair[1], table)
        
        # Same row
        if r1 == r2:
            ciphertext.append(table[r1][(c1 + 1) % 5])
            ciphertext.append(table[r2][(c2 + 1) % 5])
        # Same column
        elif c1 == c2:
            ciphertext.append(table[(r1 + 1) % 5][c1])
            ciphertext.append(table[(r2 + 1) % 5][c2])
        # Rectangle rule
        else:
            ciphertext.append(table[r1][c2])
            ciphertext.append(table[r2][c1])
    
    return ''.join(ciphertext)

# Example usage

plaintext = input("enter the plaintext: ")
key =input("enter the key : ")
ciphertext = playfair_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
