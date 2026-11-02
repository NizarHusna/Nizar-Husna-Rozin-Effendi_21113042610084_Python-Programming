pengguna_sekarang = ['hatta', 'gunawan', 'budi', 'aris', 'siti']
pengguna_baru = ['HATTA', 'joko', 'sri', 'Budi', 'wahyu']

Pengguna_sekarang_lower = [nama.lower() for nama in pengguna_sekarang]

for nama in pengguna_baru:
    if nama.lower() in Pengguna_sekarang_lower:
        print(f"Nama pengguna '{nama}' sudah digunakan, silakan pilih nama lain.")
    else:
        print(f"Nama pengguna '{nama}' tersedia.")