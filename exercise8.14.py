
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


# Membuat informasi mobil
car = make_car(
    'subaru',
    'outback',
    color='blue',
    tow_package=True
)

# Menampilkan dictionary mobil
print(car)
