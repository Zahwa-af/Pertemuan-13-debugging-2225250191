def hitung_total(daftar_angka):
    total = 0
    for item in daftar_angka:
        total += item  # Pasang Breakpoint di baris ini
    return total

angka = [10, 20, 30, 40]
hasil = hitung_total(angka)
print("Hasil total:", hasil)