
"""
Spyder Editor

This is a temporary script file.
"""
text = input("Enter A Encrypt Text To Show Decrypt Message\n")
shift = 3

def encrypt(text,shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        
        if (char.islower()):
            result += chr((ord(char) + shift - 97) % 26 + 97)
 
        else:
            result += chr((ord(char) + shift - 65) % 26 + 65)
 
    return result
 

print("Actual  : " + text)
#print("Shift : " + str(shift))
print("Encoded: " + encrypt(text,shift))
