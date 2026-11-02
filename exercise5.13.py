#Progam Data Siswa
data_siswa = []

while True:
    nama = input("Masukkan nama siswa (atau ketik 'selesai' untuk berhenti): ")
    if nama.lower() == 'selesai':
        break
    nilai = int(input("Masukkan nilai siswa:"))
    
    if nilai >= 70:
        status = "Lulus"
    else:
        status = "Tidak Lulus"
        
siswa = {
    "nama": nama,
    "nilai": nilai,
    "status": status
    }
data_siswa.append(siswa)

print("\nData Siswa:")
for siswa in data_siswa:
    print(f"Nama : {siswa['nama']}")
    print(f"Nilai : {siswa['nilai']}")
    print(f"Status : {siswa['status']}")
    print("--------------------")