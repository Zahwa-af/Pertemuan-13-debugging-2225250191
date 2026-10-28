def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

# Pengujian Sederhana
print("Uji 75:", status_lulus(75))  # Normal -> Lulus
print("Uji 60:", status_lulus(60))  # Batas -> Lulus
print("Uji 59:", status_lulus(59))  # Di bawah batas -> Tidak lulus