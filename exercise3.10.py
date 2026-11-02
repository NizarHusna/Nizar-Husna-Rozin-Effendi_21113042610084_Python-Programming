negara = ["Indonesia", "Jepang", "Brasil", "Kanada", "Prancis"]

# Menampilkan daftar awal
print("Daftar negara awal:")
print(negara)

# Mengakses elemen
print("\nNegara pertama:")
print(negara[0])

# Mengubah elemen
negara[0] = "Spanyol"
print("\nSetelah mengubah elemen:")
print(negara)

# Menambahkan elemen menggunakan append()
negara.append("Jerman")
print("\nSetelah menggunakan append():")
print(negara)

# Menambahkan elemen menggunakan insert()
negara.insert(1, "Swiss")
print("\nSetelah menggunakan insert():")
print(negara)

# Menghapus elemen menggunakan del
del negara[1]
print("\nSetelah menggunakan del:")
print(negara)

# Menghapus elemen menggunakan pop()
negara_dihapus = negara.pop()
print("\nNegara yang dihapus:")
print(negara_dihapus)

# Menghapus elemen menggunakan remove()
negara.remove("Brasil")
print("\nSetelah menggunakan remove():")
print(negara)

# Mengurutkan daftar
negara.sort()
print("\nUrutan alfabet:")
print(negara)

# Membalik urutan daftar
negara.reverse()
print("\nSetelah dibalik:")
print(negara)

# Menghitung jumlah elemen
print("\nJumlah negara:")
print(len(negara))