# Kode Setelah Diinvestigasi dan Diperbaiki (Fix)

def hitung_rata_rata(nilai):
    """Memperbaiki bug pembagi tetap dan menangani list kosong."""
    if len(nilai) == 0:
        return 0.0
    return sum(nilai) / len(nilai)

def status(nilai):
    """Memperbaiki operator batas kelulusan (>= 60)."""
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    """Memperbaiki inisialisasi dan logika pembanding elemen maksimum."""
    if len(nilai) == 0:
        return None
    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi

if __name__ == "__main__":
    data_nilai = [80, 60, 90, 70]
    print("Rata-rata:", hitung_rata_rata(data_nilai))
    print("Status 60:", status(60))
    print("Tertinggi:", nilai_tertinggi(data_nilai))