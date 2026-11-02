foods = ("mie ayam", "soto", "martabak", "nasi goreng", "bakso")
print("Menu makanan restoran:")
for food in foods:
    print(food)
    
#Mengubah salah satu makanan
try:
    foods[0] = "mie goreng"
except TypeError:
    print("Tuple tidak dapat diubah!.")
    
#Mengubah salah satu menu makanan dengan tuple baru
foods = ("mie goreng", "soto", "martabak", "nasi goreng", "bakso")
print("Menu makanan baru restoran:")
for food in foods:
    print(food)