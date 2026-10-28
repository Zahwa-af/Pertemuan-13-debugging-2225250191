def baca_dan_hitung(nama_file):
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    data.append(float(baris))
        return sum(data) / len(data)
    except (FileNotFoundError, ZeroDivisionError) as e:
        print(f"Error diproses: {e}")
        return 0

if __name__ == "__main__":
    baca_dan_hitung("data_kosong.txt")