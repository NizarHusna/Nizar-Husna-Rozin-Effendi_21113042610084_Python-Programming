kamus = {
    'print': 'Untuk menampilkan teks ke layar.',
    'input': 'Untuk menerima masukan dari pengguna.',
    'if': 'Untuk memeriksa suatu kondisi.',
    'for': 'Untuk melakukan perulangan.',
    'list': 'Untuk menyimpan beberapa data dalam satu variabel.'
}

print("KAMUS PEMROGRAMAN PYTHON\n")

for kata, arti in kamus.items():
    print(kata + ":")
    print(arti + "\n")