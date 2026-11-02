
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


# Membuat daftar pesan
messages = [
    "Halo, apa kabar?",
    "Selamat pagi!",
    "Jangan lupa untuk berolahraga.",
    "Semoga harimu menyenangkan!"
]

sent_messages = []

# Memanggil fungsi menggunakan salinan list
send_messages(messages[:], sent_messages)

# Menampilkan kedua list
print("\nDaftar messages:")
print(messages)

print("\nDaftar sent_messages:")
print(sent_messages)
