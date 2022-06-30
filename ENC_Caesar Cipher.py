from re import A

def encrypt(text,s):
    result = ""
        # transverse uppercase characters in plain text
    for i in range(len(text)):
        char = text[i]
            # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        #elif (char.isdigit()):
        #    result += chr((ord(char) + s - 48) % 10 + 48)
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
            # Space Transform to space
        elif (char.isspace()):
            result += chr((ord(char) + s + 32) % 1 + 32)
            # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
            
    return result

# Check the above function 
text = "TEKS YANG AKAN DIENCRYPT"
s = 13
print ('Plain text : ' + text)
print ('Shift pattern : ' + str(s))
print ('Cipher : ' + encrypt(text,s))
