pengguna = ['admin', 'gunawan', 'budi', 'aris', 'siti']

for nama in pengguna:
    if nama == 'admin':
        print("Halo admin, apakah kamu ingin melihat laporan status?")
    else:
        print(f"Halo {nama}, terima kasih sudah login kembali.")