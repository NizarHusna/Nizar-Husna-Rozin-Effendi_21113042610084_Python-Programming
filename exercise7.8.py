
sandwich_orders = ["tuna", "ayam", "daging sapi", "keju"]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Saya membuat sandwich {sandwich} Anda.")

    finished_sandwiches.append(sandwich)

print("\nSandwich yang sudah dibuat:")

for sandwich in finished_sandwiches:
    print(sandwich)
