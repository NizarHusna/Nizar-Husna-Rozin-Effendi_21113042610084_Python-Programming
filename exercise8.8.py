
def make_album(nama_artis, judul_album, jumlah_lagu=None):
    album = {
        'artis': nama_artis,
        'album': judul_album
    }

    if jumlah_lagu:
        album['jumlah_lagu'] = jumlah_lagu

    return album


while True:
    print("\nMasukkan informasi album:")
    print("(Ketik 'quit' untuk keluar)")

    nama_artis = input("Masukkan nama artis: ")

    if nama_artis.lower() == 'quit':
        break

    judul_album = input("Masukkan judul album: ")

    if judul_album.lower() == 'quit':
        break

    album = make_album(nama_artis, judul_album)

    print("\nInformasi album:")
    print(album)

print("Program selesai")
