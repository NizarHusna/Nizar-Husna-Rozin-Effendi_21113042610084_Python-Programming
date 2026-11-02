def make_shirt(size="Large", message="I love Python"):
    print("Ukuran kaos: " + size)
    print("Tulisan pada kaos: " + message)

# Kaos ukuran besar dengan pesan default
make_shirt()

# Kaos ukuran sedang dengan pesan default
make_shirt(size="Medium")

# Kaos dengan ukuran bebas dan pesan berbeda
make_shirt("Small", "Aku Cinta Kalkulus")