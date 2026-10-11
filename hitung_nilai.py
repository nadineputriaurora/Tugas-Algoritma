"""
Implementasi Algoritma Sistem Penilaian Akhir Mahasiswa
Sesuai rancangan pseudocode dan spesifikasi bobot.
Dilengkapi perulangan (looping) agar pengguna bisa mengulang atau keluar.
"""

def hitung_nilai_akhir(tugas: float, uts: float, uas: float):
    # Bobot: Tugas 30%, UTS 30%, UAS 40%
    nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)
    
    # Penentuan grade
    if nilai_akhir >= 81:
        grade = 'A'
    elif nilai_akhir >= 70:
        grade = 'B'
    elif nilai_akhir >= 60:
        grade = 'C'
    elif nilai_akhir >= 50:
        grade = 'D'
    else:
        grade = 'E'
        
    return nilai_akhir, grade

def main():
    while True:
        print("\n========================================")
        print("=== SISTEM PENILAIAN AKHIR MAHASISWA ===")
        print("========================================")
        try:
            tugas = float(input("Masukkan Nilai Tugas (0-100) : "))
            uts   = float(input("Masukkan Nilai UTS   (0-100) : "))
            uas   = float(input("Masukkan Nilai UAS   (0-100) : "))
        except ValueError:
            print("\n[!] Input tidak valid: Harap masukkan angka yang benar.")
            continue

        # Cek batas validitas rentang nilai 0-100
        if not (0 <= tugas <= 100 and 0 <= uts <= 100 and 0 <= uas <= 100):
            print("\n[!] Nilai harus berada dalam rentang 0 s.d. 100.")
            continue

        na, grade = hitung_nilai_akhir(tugas, uts, uas)
        
        print("----------------------------------------")
        print("HASIL PENILAIAN AKHIR:")
        print(f"Nilai Tugas : {tugas:.2f}")
        print(f"Nilai UTS   : {uts:.2f}")
        print(f"Nilai UAS   : {uas:.2f}")
        print("----------------------------------------")
        print(f"Nilai Akhir : {na:.2f}")
        print(f"Grade       : {grade}")
        print("========================================")

        # Opsi pengulangan (kembali atau keluar)
        pilihan = input("\nApakah ingin menghitung nilai lagi? (Y/T): ").strip().upper()
        if pilihan != 'Y':
            print("\nTerima kasih telah menggunakan sistem ini. Program selesai.")
            break

if __name__ == "__main__":
    main()
