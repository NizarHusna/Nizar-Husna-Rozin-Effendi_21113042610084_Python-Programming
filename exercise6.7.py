orang1 = {
    'nama_depan': 'Budi',
    'nama_belakang': 'Wahyudi',
    'umur': 33,
    'kota': 'Klaten'
}

orang2 = {
    'nama_depan': 'Gunawan',
    'nama_belakang': 'Santoso',
    'umur': 28,
    'kota': 'Bandung'
}

orang3 = {
    'nama_depan': 'Siti',
    'nama_belakang': 'Aminah',
    'umur': 19,
    'kota': 'Malang'
}

people = [orang1, orang2, orang3]

for orang in people:
    print("Nama:", orang['nama_depan'], orang['nama_belakang'])
    print("Umur:", orang['umur'])
    print("Kota:", orang['kota'])
    print()