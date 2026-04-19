# LIST – AKSES & MANIPULASI
print("=== LIST ===")
data = ["apel", 10, "jeruk", 25, "mangga", 50]

print("List awal:", data)
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])
print("Slicing [1:5:2]:", data[1:5:2])

# sebelum manipulasi
print("\nSebelum manipulasi:", data)

# append
data.append("pisang")

# insert
data.insert(2, "anggur")

# extend
data.extend([100, "melon"])

# pop
data.pop()

# remove
data.remove(10)

# setelah manipulasi
print("Sesudah manipulasi:", data)

# TUPLE – IMMUTABILITY & UNPACKING
print("\n=== TUPLE ===")
tup = ("A", "B", "C", "D", "E")

print("Tuple:", tup)
print("Panjang tuple:", len(tup))
print("Akses indeks ke-2:", tup[2])

# unpacking
a, b, *rest = tup
print("Unpacking:")
print("a =", a)
print("b =", b)
print("rest =", rest)



# SET – OPERASI HIMPUNAN

print("=== SET ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# duplikat otomatis hilang
set_duplikat = {1, 1, 2, 2, 3, 3}
print("Set dengan duplikat:", set_duplikat)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)



# DICTIONARY

print("=== DICTIONARY ===")
mahasiswa = {
    "nama": "David",
    "nim": "123456",
    "angkatan": 2023,
    "kota": "Batam"
}

print("Data awal:", mahasiswa)

# tambah key
mahasiswa["jurusan"] = "Informatika"

# ubah nilai
mahasiswa["kota"] = "Tanjung Balai"

# hapus key
del mahasiswa["angkatan"]

print("Setelah update:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("Iterasi:")
for k, v in mahasiswa.items():
    print(f"{k}: {v}")


# =========================
# NESTED STRUCTURES
# =========================
print("=== NESTED STRUCTURES ===")
buku = [
    {"judul": "Python Dasar", "penulis": "Andi", "tahun": 2020},
    {"judul": "AI Modern", "penulis": "Budi", "tahun": 2023},
    {"judul": "Machine Learning", "penulis": "Caca", "tahun": 2022},
    {"judul": "Deep Learning", "penulis": "Dodi", "tahun": 2024}
]

print("Semua judul buku:")
for b in buku:
    print("-", b["judul"])

# filter tahun >= 2022
buku_baru = [b for b in buku if b["tahun"] >= 2022]
print("Buku tahun >= 2022:", buku_baru)



# COMPREHENSION

print("=== COMPREHENSION ===")

angka = list(range(1, 21))

genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("Angka genap:", genap)
print("Kuadrat:", kuadrat)

# dict comprehension
dict_angka = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("Dict genap/ganjil:", dict_angka)

# set comprehension
kalimat = "Belajar Python Itu Seru"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("Huruf unik:", huruf_unik)


# KEANGGOTAAN & PENCARIAN

print("\n=== KEANGGOTAAN & PENCARIAN ===")

# cek keanggotaan
print("Apakah 'apel' ada di list?", "apel" in data)
print("Apakah 10 ada di set?", 10 in set1)

# index / pencarian
if "jeruk" in data:
    print("'jeruk' ada di index:", data.index("jeruk"))
else:
    print("'jeruk' tidak ditemukan")
