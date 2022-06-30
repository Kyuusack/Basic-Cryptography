print("ALGHORITMA REVERSE")
suratcinta = input("Pesan       : ")
reti = "" #cipher text is stored in this variable
x = len(suratcinta) - 1
while x >= 0:
        reti = reti + suratcinta[x]
        x = x - 1

print("Hasil       : " + reti)
