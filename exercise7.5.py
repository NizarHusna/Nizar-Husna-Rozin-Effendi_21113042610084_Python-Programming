while True:
    umur = input("Masukkan umur Anda (ketik 'selesai' untuk keluar): ")
    
    if umur == 'selesai':
        break

    umur = int(umur)

    if umur < 3:
        harga = 0
    elif umur <= 12:
        harga = 10
    else:
        harga = 15

    print(f"Harga tiket untuk umur {umur} tahun adalah ${harga}.")