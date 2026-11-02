#Menggunakan kondisi While

topping = ""

while topping != "selesai":
    topping = input("Masukkan topping pizza (ketik 'selesai' untuk selesai): ")

    if topping != "selesai":
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")

print("Pesanan pizza selesai!")


#Menggunakan active variable

aktif = True

while aktif:
    umur = input("Masukkan umur Anda (ketik 'selesai' untuk selesai): ")

    if umur == "selesai":
        aktif = False
    else:
        umur = int(umur)

        if umur < 3:
            print("Harga tiket gratis.")
        elif umur <= 12:
            print("Harga tiket $10.")
        else:
            print("Harga tiket $15.")

print("Program selesai!")


#Menggunakan break statement
while True:
    topping = input("Masukkan topping pizza (ketik 'quit' untuk selesai): ")

    if topping == "quit":
        break

    print(f"Saya akan menambahkan {topping} ke pizza Anda.")

print("Pesanan pizza selesai!")

