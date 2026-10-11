# Sistem Penilaian Akhir Mahasiswa

Proyek perancangan algoritma sistem akademik untuk menghitung nilai akhir mahasiswa berdasarkan 3 komponen bobot (Tugas 30%, UTS 30%, UAS 40%) dan menentukan huruf mutu kelulusan (Grade A - E) secara otomatis, dilengkapi dengan kontrol perulangan (*looping*).

---

## 📁 Struktur Berkas

Berikut adalah daftar berkas yang tersedia di dalam paket ini:

| Nama Berkas | Jenis | Keterangan |
| :--- | :--- | :--- |
| **`PROGAM NYA.exe`** | Executable Windows | Program aplikasi siap pakai (dapat langsung dijalankan tanpa instalasi Python). |
| **`hitung_nilai.py`** | Source Code Python | Kode program resmi implementasi algoritma menggunakan Python 3. |
| **`pseudocode.txt`** | Notasi Teks | Rancangan algoritma murni dalam format pseudocode standar akademik. |
| **`Laporan_Tugas_Algoritma.pdf`** | Dokumen Laporan | Dokumen laporan lengkap format A4 (mencakup IPO, Pseudocode, Flowchart, Uji Kasus, dan Kesimpulan). |
| **`hasil_pengujian.png`** | Tangkapan Layar | Bukti otentik pengujian langsung eksekusi terminal dengan 3 set data (Grade A, C, dan E). |
| **`Flowchart/`** | Folder Diagram | Berisi diagram alir visual format `flowchart.png`, `flowchart_dark.png`, vektor `flowchart.svg`, dan penampil web `flowchart_viewer.html`. |

---

## ⚙️ Ketentuan Bobot & Kriteria Kelulusan

### 1. Pembobotan Nilai Akhir (NA)
$$\text{Nilai Akhir} = (0.30 \times \text{Nilai Tugas}) + (0.30 \times \text{Nilai UTS}) + (0.40 \times \text{Nilai UAS})$$

### 2. Standar Kriteria Grade
* **Grade A** : Nilai Akhir $\ge 81$
* **Grade B** : Nilai Akhir $\ge 70$ (dan $< 81$)
* **Grade C** : Nilai Akhir $\ge 60$ (dan $< 70$)
* **Grade D** : Nilai Akhir $\ge 50$ (dan $< 60$)
* **Grade E** : Nilai Akhir $< 50$

---

## 🚀 Panduan Menjalankan Program

### Cara 1: Menggunakan File Executable (.EXE) — Paling Praktis
1. Klik ganda (*double-click*) pada file **`PROGAM NYA.exe`**.
2. Masukkan nilai Tugas, UTS, dan UAS saat diminta di layar.
3. Program akan menampilkan hasil Nilai Akhir dan Grade Mutu, lalu menanyakan apakah ingin mengulang kembali (`Y`) atau keluar (`T`).

### Cara 2: Menjalankan Source Code Python
Buka terminal pada direktori ini, lalu jalankan perintah:
```bash
python hitung_nilai.py
```

---

## 🧪 Hasil Uji Validasi Logika (3 Data Berbeda)

| Skenario Uji | Nilai Tugas | Nilai UTS | Nilai UAS | Nilai Akhir | Grade | Status Validasi |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Kasus 1** | 85 | 80 | 90 | **85.50** | **A** | **VALID (Grade A)** |
| **Kasus 2** | 65 | 60 | 68 | **64.70** | **C** | **VALID (Grade C)** |
| **Kasus 3** | 40 | 45 | 40 | **41.50** | **E** | **VALID (Grade E)** |

Bukti visual jalannya pengujian terminal dapat dilihat pada berkas **`hasil_pengujian.png`**.
