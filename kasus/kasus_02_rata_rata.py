def rata_rata(data):
    # Bug awal: membagi dengan 5 secara konstan tanpa peduli jumlah elemen
    total = sum(data)
    return total / 5

if __name__ == "__main__":
    print("Rata-rata [80, 90, 70]:", rata_rata([80, 90, 70]))