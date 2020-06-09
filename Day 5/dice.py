import random
angka = random.randint(1,7)
angka = 10

for x in range (1,4): 
    tebakan = int(input("Guess the Number! 1-6 "))
    if tebakan == angka:
        print('benar')
        break
    else: 
        print('Salah')
        lanjut = input("Tebak Ulang? y/n ")
        if lanjut == "n":
            break
print('Selesai')