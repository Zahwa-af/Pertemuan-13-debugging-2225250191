def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon

bayar = hitung_diskon(200000, 10)
print(f"Total Bayar: {bayar}")