
def make_sandwich(*items):
    print("\nSandwich yang dipesan:")
    for item in items:
        print("- " + item)


# Memanggil fungsi tiga kali
make_sandwich('Roti', 'Keju', 'Daging')

make_sandwich('Roti', 'Telur', 'Selada', 'Tomat')

make_sandwich('Roti', 'Ayam', 'Keju', 'Saus', 'Mayones')
