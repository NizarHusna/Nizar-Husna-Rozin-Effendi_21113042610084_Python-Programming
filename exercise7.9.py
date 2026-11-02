
sandwich_orders = [
    "tuna",
    "pastrami",
    "ayam",
    "pastrami",
    "keju",
    "pastrami"
]

finished_sandwiches = []

print("Maaf, sandwich pastrami sedang habis.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Saya membuat sandwich {sandwich} Anda.")

    finished_sandwiches.append(sandwich)

print("\nSandwich yang sudah dibuat:")

for sandwich in finished_sandwiches:
    print(sandwich)
