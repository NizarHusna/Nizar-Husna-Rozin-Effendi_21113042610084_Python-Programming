sungai = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'gangga': 'india'
}

for nama, negara in sungai.items():
    print(f"Sungai {nama.title()} mengalir melalui {negara.title()}.")

print("\nNama-nama sungai:")

for nama in sungai.keys():
    print(nama.title())

print("\nNama-nama negara:")

for negara in sungai.values():
    print(negara.title())
