def status_lulus(nilai):
    # Bug awal: nilai > 60 menyebabkan nilai 60 dianggap "Tidak lulus"
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"

if __name__ == "__main__":
    print("Uji 60:", status_lulus(60))