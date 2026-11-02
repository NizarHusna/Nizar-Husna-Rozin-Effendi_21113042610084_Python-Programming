bahasa_favorit = {
    'aris': 'python',
    'budi': 'java',
    'hatta': 'javascript',
    'gunawan': 'c++'
}

daftar_peserta = ['aris', 'budi', 'hatta', 'gunawan', 'wahyu']

for nama in daftar_peserta:
    if nama in bahasa_favorit:
        print(f"Terima kasih {nama.title()} sudah mengikuti polling.")
    else:
        print(f"Halo {nama.title()}, tolong isi polling bahasa favorit.")
