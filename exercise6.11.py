
cities = {
    'Bandung': {
        'country': 'Indonesia',
        'population': '2,61 juta jiwa',
        'fact': 'Bekas danau purba raksasa.'
    },
    'Tokyo': {
        'country': 'Jepang',
        'population': '14 juta jiwa',
        'fact': 'Memiliki sistem transportasi kereta yang sangat maju.'
    },
    'Paris': {
        'country': 'Prancis',
        'population': '2,1 juta jiwa',
        'fact': 'Terkenal dengan Menara Eiffel.'
    }
}

for city, information in cities.items():
    print(f"\nNama Kota: {city}")
    print(f"Negara: {information['country']}")
    print(f"Populasi: {information['population']}")
    print(f"Fakta: {information['fact']}")

