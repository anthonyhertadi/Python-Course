operation = input("(+),(-),(*),(/) ")
angka_1 = int(input("Angka 1 : "))
angka_2 = int(input("Angka 2 : "))
print(angka_1, operation, angka_2)
hasil = 0

if operation == "+":
    hasil = angka_1 + angka_2
elif operation == "-":
    hasil = angka_1 - angka_2
elif operation == "*":
    hasil = angka_1 * angka_2
elif operation == "/":
    hasil = angka_1 / angka_2

print(hasil)