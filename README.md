# Pertemuan 13 - Debugging, Tracing, Testing, dan Test Case

## Identitas
- **Nama:** Zahwa Ajmala Fitriani
- **NIM:** 2225250191
- **Kelas:** 3B

## Kasus
Program yang diuji adalah program pengolah data nilai yang memiliki 3 fungsi utama: `hitung_rata_rata`, `status`, dan `nilai_tertinggi`. Program awal memuat beberapa bug logika yang menghasilkan output salah.

## Test Case
| ID | Target Fungsi | Input | Expected | Actual Awal | Status Awal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T1** | `hitung_rata_rata` | `[80, 60, 90, 70]` | `75.0` | `60.0` | FAIL |
| **T2** | `hitung_rata_rata` | `[100, 80]` | `90.0` | `36.0` | FAIL |
| **T3** | `status` | `60` | `Lulus` | `Tidak lulus` | FAIL |
| **T4** | `status` | `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| **T5** | `nilai_tertinggi` | `[80, 60, 90, 70]` | `90` | `0` | FAIL |

## Bug Report
1. **B01 (`hitung_rata_rata`)**
   - **Gejala:** Hasil perhitungan rata-rata selalu salah (terlalu kecil).
   - **Lokasi:** Baris 2 pada kode awal.
   - **Akar Penyebab:** Angka pembagi di-*hardcode* menjadi `5`, padahal jumlah elemen pada data input bervariasi.
   - **Perbaikan:** Mengubah pembagi menjadi `len(nilai)` dan menambahkan penanganan untuk list kosong.

2. **B02 (`status`)**
   - **Gejala:** Nilai `60` dikategorikan sebagai "Tidak lulus".
   - **Lokasi:** Baris 5 pada kode awal.
   - **Akar Penyebab:** Operator perbandingan menggunakan `>` (lebih besar dari) alih-alih `>=` (lebih besar sama dengan).
   - **Perbaikan:** Mengubah kondisi `if nilai > 60:` menjadi `if nilai >= 60:`.

3. **B03 (`nilai_tertinggi`)**
   - **Gejala:** Nilai tertinggi yang dikembalikan adalah `0`, bukan `90`.
   - **Lokasi:** Baris 9–12 pada kode awal.
   - **Akar Penyebab:** Variabel `tertinggi` diinisialisasi `0` dan pembanding `if x < tertinggi` salah memilih elemen yang lebih kecil.
   - **Perbaikan:** Menginisialisasi `tertinggi = nilai[0]` dan mengubah operator menjadi `if x > tertinggi:`.

## Retest (Pengujian Ulang)
| ID | Target Fungsi | Input | Expected | Actual Akhir | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T1** | `hitung_rata_rata` | `[80, 60, 90, 70]` | `75.0` | `75.0` | PASS |
| **T2** | `hitung_rata_rata` | `[100, 80]` | `90.0` | `90.0` | PASS |
| **T3** | `status` | `60` | `Lulus` | `Lulus` | PASS |
| **T4** | `status` | `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| **T5** | `nilai_tertinggi` | `[80, 60, 90, 70]` | `90` | `90` | PASS |

## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py