
responses = {}

while True:
    name = input("Siapa nama Anda? ")

    place = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")

    responses[name] = place

    repeat = input("Apakah ada orang lain yang ingin ikut? (ya/tidak) ")

    if repeat == "tidak":
        break

print("\n=== DATA HASIL LIBURAN IMPIAN ===")

for name, place in responses.items():
    print(f"{name} ingin berlibur ke {place}.")
