def test(nilai_dictionary):
    for key,val in nilai_dictionary.items():
        print("Untuk Mata Pelajaran {satu} and Anda mencetak nilai {dua}!".format(key,val))
tiga = {}
Nama = input("Nama : ")
while True:
    satu= input("Mat Pel: ")
    dua= int(input("Nilai : "))
    if dua == 100:
        grade = "A+"
    elif dua >= 90:
        grade = "A"
    elif dua >= 80:
        grade = "B"
    elif dua >= 70:
        grade = "C"     
    else:
        grade = "FAIL"
    extra = input("Input nilai lagi? y/n ")

    if extra == 'y':
        continue
    else:
        print(test)
        break
    
    print(tiga)
    test(tiga)