def make_shirt(size, message):
    print("Ukuran kaos: " + size)
    print("Tulisan pada kaos: " + message)

# Menggunakan positional arguments
make_shirt("Large", "I Love Enggineering")

# Menggunakan keyword arguments
make_shirt(size="Medium", message="Never Give Up")