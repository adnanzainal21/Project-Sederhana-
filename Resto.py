# daftar makanan
menu = {
    "1": {"nama": "Nasi Goreng", "harga": 25000},
    "2": {"nama": "Mie Ayam", "harga": 20000},
    "3": {"nama": "Sate Ayam", "harga": 30000},
    "4": {"nama": "Ayam Bakar", "harga": 35000},
    "5": {"nama": "Gado-Gado", "harga": 15000}
}

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("Menu Makanan:")
    for key, value in menu.items():
        print(key + ". " + value["nama"] + " - Rp" + str(value["harga"]))

# Fungsi untuk menghitung total harga pesanan
def hitung_total_harga(pesanan):
    total = 0
    for item in pesanan:
        harga = menu[item]["harga"]
        total += harga
    return total

# Program Utama
pesanan = []
selesai = False

print("Selamat datang di Program Pemesanan Makanan!")

while not selesai:
    tampilkan_menu()
    nomor_pesanan = input("Masukkan nomor makanan yang ingin dipesan (0 untuk selesai): ")

    if nomor_pesanan == "0":
        selesai = True
    elif nomor_pesanan in menu:
        pesanan.append(nomor_pesanan)
        print(menu[nomor_pesanan]["nama"] + " telah ditambahkan ke pesanan.")
    else:
        print("Nomor makanan tidak valid. Silakan pilih nomor makanan yang tersedia.")

total_harga = hitung_total_harga(pesanan)

print("Pesanan Anda:")
for item in pesanan:
    print(menu[item]["nama"])

print("Total Harga: Rp" + str(total_harga))
print("Terima kasih telah menggunakan layanan kami. Selamat menikmati makanan Anda!")
