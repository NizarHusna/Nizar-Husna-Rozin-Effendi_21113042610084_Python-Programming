
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


# Membuat profil pengguna
my_profile = build_profile(
    'Hatta',
    'Santoso',
    umur=20,
    pekerjaan='Mahasiswa',
    hobi='Membaca'
)

# Menampilkan profil
print(my_profile)
