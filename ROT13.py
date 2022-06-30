print("ALGHORITMA ROTTELULAS")
rottelulas = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdevghijklm')

#function to translate plain text
def rot13(text):
    return text.translate(rottelulas)

def main():
    layang = input("Pesan       : ")
    Decrypt = (rot13(layang))
    print("Hasil       : " + Decrypt)
    
if __name__ == "__main__":
    main()