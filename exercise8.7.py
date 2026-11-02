
def make_album(nama_artis, judul_album, jumlah_lagu=None):
    album = {
        'artis': nama_artis,
        'album': judul_album
    }

    if jumlah_lagu:
        album['jumlah_lagu'] = jumlah_lagu

    return album


# Membuat tiga dictionary album
album1 = make_album('Noah', 'Seperti Seharusnya')
album2 = make_album('Sheila on 7', 'Kisah Klasik')
album3 = make_album('Barasuara', 'Jalaran Sadrah')

# Menampilkan hasil
print(album1)
print(album2)
print(album3)

# Memanggil fungsi dengan jumlah lagu
album4 = make_album('Oasis', "(What's the Story) Morning Glory?", 12)
print(album4)
