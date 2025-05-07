
def encrypt(text,s):
    result = ""

    
    for i in range(len(text)):
        char = text[i]

       
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

       
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result
print("1. encryption : \n 2.Decryption : \n")

text= input("enter the text you want to encrypt")
#text = "ATTACKATONCE"
s= int(input("enter the number by wich you want t encrypt"))
#s = 4
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))

