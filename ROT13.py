print("ALGHORITMA ROT13")
rotthirteen = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdevghijklm')

#function to translate plain text
def rot13(text):
    return text.translate(rotthirteen)

def main():
    message = input("Pesan       : ")
    Decrypt = (rot13(message))
    print("Hasil       : " + Decrypt)
    
if __name__ == "__main__":
    main()
