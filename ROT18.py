print("ALGHORITMA ROTWOLULAS")
rotwolulas = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                           'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyz%bcdevghijklm5678901234')

#function to translate plain text
def rot18(text):
    return text.translate(rotwolulas)

def main():
    layang = input("Pesan Rahasia = ")
    Decrypt = (rot18(layang))
    print("Hasil         : " + Decrypt)
    
if __name__ == "__main__":
    main()