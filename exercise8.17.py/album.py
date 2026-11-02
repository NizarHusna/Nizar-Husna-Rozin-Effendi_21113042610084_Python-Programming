def buat_album(nama_artis, judul_album, jumlah_lagu=None):
    """Membuat dictionary yang berisi informasi album musik."""
    album = {
        "artis": nama_artis,
        "judul": judul_album
    }

    if jumlah_lagu is not None:
        album["jumlah_lagu"] = jumlah_lagu

    return album


album1 = buat_album("Taylor Swift", "1989")
album2 = buat_album("Ed Sheeran", "Divide")
album3 = buat_album("Adele", "25")
album4 = buat_album("Bruno Mars", "24K Magic", jumlah_lagu=9)

print(album1)
print(album2)
print(album3)
print(album4)