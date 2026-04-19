# 1. Deklarasi Variabel dan Tipe Data
nama = "David"          # string
umur = 20               # integer
tinggi = 170.5          # float
is_student = True       # boolean
hobi = ["coding", "trading", "gaming", "desain", "ngonten"]  # list

print("=== Deklarasi Variabel ===")
print(nama, umur, tinggi, is_student, hobi)


# 2. Manipulasi String
print("=== Manipulasi String ===")
teks1 = "Halo"
teks2 = "Dunia"

gabungan = teks1 + " " + teks2
print("Gabungan:", gabungan)

print("Panjang string:", len(gabungan))
print("Uppercase:", gabungan.upper())
print("Lowercase:", gabungan.lower())


# 3. Operasi Matematika Sederhana
print("=== Operasi Matematika ===")
a = 10
b = 3

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian bulat:", a // b)
print("Modulus:", a % b)


# 4. List dan Akses Elemen
print("=== List ===")
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]

print("List awal:", buah)
print("Elemen ke-2:", buah[1])

buah.append("melon")
print("Setelah ditambah:", buah)

buah.remove("apel")
print("Setelah remove apel:", buah)

buah.pop()
print("Setelah pop:", buah)


# 5. Input dari User
print("=== Input User ===")
nama_user = input("Masukkan nama kamu: ")
umur_user = input("Masukkan umur kamu: ")

print(f"Halo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
