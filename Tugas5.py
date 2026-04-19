# IMPORT & SETUP
import numpy as np
import pandas as pd
import os

np.random.seed(42)



# NUMPY – DATA & STATISTIK


# buat data nilai ujian (10 data)
nilai_array = np.random.randint(50, 100, size=10)

# hitung statistik
rata_rata_np = np.mean(nilai_array)
median_np = np.median(nilai_array)
std_np = np.std(nilai_array)
min_np = np.min(nilai_array)
max_np = np.max(nilai_array)



# PANDAS – DATAFRAME


data = {
    "nama": ["Andi", "Budi", "Citra", "Dewi", "Eka"],
    "nim": ["001", "002", "003", "004", "005"],
    "nilai": nilai_array[:5] 
}

df = pd.DataFrame(data)


df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")



# FILE I/O – TULIS KE TXT


def tulis_ringkasan_awal(path):
    with open(path, "w") as f:
        f.write("=== RINGKASAN NUMPY ===\n")
        f.write(f"Rata-rata   : {rata_rata_np}\n")
        f.write(f"Median      : {median_np}\n")
        f.write(f"Std Dev     : {std_np}\n")
        f.write(f"Nilai Min   : {min_np}\n")
        f.write(f"Nilai Max   : {max_np}\n\n")

        f.write("=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah Data : {len(df)}\n")
        f.write(f"LULUS       : {(df['status'] == 'LULUS').sum()}\n")
        f.write(f"TIDAK LULUS : {(df['status'] == 'TIDAK LULUS').sum()}\n\n")



# OOP – GRADEBOOK


class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df["nilai"].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = (self.df["nilai"] >= threshold).sum()
        total = len(self.df)
        return (lulus / total) * 100

    def save_summary(self, path: str):
        with open(path, "a") as f:  # append
            f.write("=== RINGKASAN GRADEBOOK ===\n")
            f.write(f"Rata-rata nilai : {self.average()}\n")
            f.write(f"Pass rate       : {self.pass_rate()}%\n\n")

    def __str__(self):
        return f"GradeBook: {len(self.df)} data | Rata-rata = {self.average():.2f}"



# DEMO


if __name__ == "__main__":

    print("=== NUMPY ===")
    print("Data nilai:", nilai_array)
    print("Rata-rata:", rata_rata_np)
    print("Median:", median_np)
    print("Std Dev:", std_np)
    print("Min:", min_np)
    print("Max:", max_np)

    print("\n=== PANDAS ===")
    print(df.head())

    # tulis file awal
    file_path = "ringkasan_tugas6.txt"
    tulis_ringkasan_awal(file_path)

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)

    print(gb)
    print("Average:", gb.average())
    print("Pass rate:", gb.pass_rate(), "%")

    gb.save_summary(file_path)

    print(f"\nRingkasan disimpan ke: {file_path}")
