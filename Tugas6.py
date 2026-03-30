# Sebelum melakukan import wajib "pip install pandas"
# IMPORT & SETUP


import numpy as np
import pandas as pd
import os

np.random.seed(42)  # biar konsisten



# NUMPY – DATA & STATISTIK

nilai_ujian = np.random.randint(50, 100, size=10)

rata2 = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std_dev = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)


# PANDAS – DATAFRAME

data = {
    "nama": ["Andi", "Budi", "Citra", "Dewi", "Eka"],
    "nim": ["23001", "23002", "23003", "23004", "23005"],
    "nilai": nilai_ujian[:5]  # ambil 5 dari numpy
}

df = pd.DataFrame(data)

# tambah kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")



# FILE I/O – SIMPAN RINGKASAN

def write_summary_txt(path):
    with open(path, "w") as f:
        f.write("=== RINGKASAN STATISTIK ===\n")
        f.write(f"Rata-rata     : {rata2:.2f}\n")
        f.write(f"Median        : {median:.2f}\n")
        f.write(f"Std Dev       : {std_dev:.2f}\n")
        f.write(f"Nilai Minimum : {nilai_min}\n")
        f.write(f"Nilai Maksimum: {nilai_max}\n\n")

        f.write("=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah data   : {len(df)}\n")
        f.write(f"Jumlah lulus  : {(df['status'] == 'LULUS').sum()}\n")
        f.write(f"Tidak lulus   : {(df['status'] == 'TIDAK LULUS').sum()}\n")



# OOP – CLASS GRADEBOOK

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df["nilai"].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        lulus = (self.df["nilai"] >= threshold).sum()
        return (lulus / total) * 100

    def save_summary(self, path: str):
        with open(path, "a") as f:  # append biar gabung
            f.write("\n=== RINGKASAN DARI CLASS ===\n")
            f.write(f"Rata-rata nilai : {self.average():.2f}\n")
            f.write(f"Pass rate       : {self.pass_rate():.2f}%\n")

    def __str__(self):
        return f"GradeBook: {len(self.df)} data | Rata-rata: {self.average():.2f}"



# DEMO

if __name__ == "__main__":

    print("=== NUMPY ===")
    print("Data:", nilai_ujian)
    print("Rata-rata:", rata2)
    print("Median:", median)
    print("Std Dev:", std_dev)
    print("Min:", nilai_min)
    print("Max:", nilai_max)

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)

    print(gb)
    print("Average:", gb.average())
    print("Pass Rate:", gb.pass_rate())

    # simpan file
    file_path = "ringkasan_tugas6.txt"
    write_summary_txt(file_path)
    gb.save_summary(file_path)

    print(f"\nRingkasan berhasil disimpan di {file_path}")