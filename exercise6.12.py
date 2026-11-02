
favorite_places = {
    'Aris': {
        'tempat': ['Bali', 'Yogyakarta', 'Raja Ampat'],
        'negara': 'Indonesia',
        'kategori': 'Wisata alam',
        'alasan': 'Menyukai pemandangan alam yang indah.'
    },
    'Budi': {
        'tempat': ['Tokyo', 'Osaka', 'Kyoto'],
        'negara': 'Jepang',
        'kategori': 'Wisata budaya',
        'alasan': 'Tertarik dengan budaya dan teknologi Jepang.'
    },
    'Hatta': {
        'tempat': ['Paris', 'London', 'Roma'],
        'negara': ['Prancis', 'Inggris', 'Italia'],
        'kategori': 'Wisata sejarah',
        'alasan': 'Menyukai bangunan bersejarah dan arsitektur.'
    }
}

# Menampilkan informasi tempat favorit setiap orang
for nama, informasi in favorite_places.items():
    print("\n================================")
    print(f"Nama: {nama}")
    print(f"Negara favorit: {informasi['negara']}")
    print(f"Kategori wisata: {informasi['kategori']}")
    print("Tempat favorit:")

    for tempat in informasi['tempat']:
        print(f"- {tempat}")

    print(f"Alasan: {informasi['alasan']}")

