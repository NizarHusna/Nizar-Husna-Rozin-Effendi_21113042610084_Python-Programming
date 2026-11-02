# 1. Pengujian kesamaan string
name = 'budi'

print("Apakah nama == 'budi'?")
print(name == 'budi')

# 2. Pengujian ketidaksamaan string
print("\nApakah nama != 'aris'?")
print(name != 'aris')

# 3. Menggunakan lower()
city = 'KLATEN'

print("\nApakah city.lower() == 'klaten'?")
print(city.lower() == 'klaten')

print("\nApakah city.lower() == 'bandung'?")
print(city.lower() == 'bandung')

# 4. Pengujian angka
number = 20

print("\nApakah angka == 20?")
print(number == 20)

print("\nApakah angka != 20?")
print(number != 20)

print("\nApakah angka > 10?")
print(number > 10)

print("\nApakah angka < 10?")
print(number < 10)

print("\nApakah angka >= 20?")
print(number >= 20)

print("\nApakah angka <= 10?")
print(number <= 10)

# 5. Menggunakan and
age = 20

print("\nApakah umur > 15 dan umur < 25?")
print(age > 15 and age < 25)

print("\nApakah umur > 25 dan umur < 30?")
print(age > 25 and age < 30)

# 6. Menggunakan or
print("\nApakah umur == 20 atau umur == 25?")
print(age == 20 or age == 25)

print("\nApakah umur == 30 atau umur == 35?")
print(age == 30 or age == 35)

# 7. Memeriksa item dalam list
foods = ['nasi goreng', 'bakso', 'soto']

print("\nApakah bakso ada dalam list?")
print('bakso' in foods)

print("\nApakah pizza ada dalam list?")
print('pizza' in foods)

# 8. Memeriksa item yang tidak ada dalam list
print("\nApakah pizza tidak ada dalam list?")
print('pizza' not in foods)

print("\nApakah soto tidak ada dalam list?")
print('soto' not in foods)