
# Laporan Praktikum Minggu [1]
Topik: [Arsitektur Sistem Operasi]

---

## Identitas
- **Nama**  : [Faizal Muzaki]  
- **NIM**   : [250202937]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.    
1. Menjelaskan peran sistem operasi dalam arsitektur komputer.
2. Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
3. Membandingkan model arsitektur OS (monolithic, layered, microkernel).
4. Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).

---

## Dasar Teori
a.Pada praktikum minggu ini, mahasiswa akan mempelajari **arsitektur dasar sistem operasi**: bagaimana komponen OS bekerja, serta bagaimana interaksi antara user, aplikasi, kernel, dan hardware terjadi.  

Mahasiswa juga diperkenalkan pada:
- Perbedaan mode eksekusi **kernel mode** dan **user mode**.
- Mekanisme **system call** (panggilan sistem).
- Perbandingan model arsitektur OS seperti **monolithic kernel**, **layered approach**, dan **microkernel**.

Eksperimen akan dilakukan menggunakan perintah dasar Linux untuk melihat informasi kernel dan modul aktif.


---

## Langkah Praktikum
1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```

2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```

5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main
   ```

---

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Hasil percobaan memperlihatkan perbedaan antara perintah di user space (yang dilakukan oleh aplikasi) dan aksi di kernel space (yang dijalankan oleh sistem operasi).

Setiap operasi yang terlihat “sederhana” di level pengguna (misalnya membuka file atau mencetak ke layar) sebenarnya melibatkan pemanggilan system call yang dijalankan di kernel.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Perbedaan *monolithic kernel*, *microkernel*, dan *layered architecture*.]  
   **Monolithic Kernel,Semua komponen inti sistem operasi dijalankan di satu ruang kernel (kernel space) dan berinteraksi langsung satu sama lain.
   Kelebihan,Kinerja tinggi — komunikasi antar komponen cepat karena tidak ada batas antar proses, dan Implementasi relatif sederhana untuk sistem kecil.
   Kekurangan,Sulit dipelihara — perubahan kecil bisa memengaruhi seluruh sistem,dan Rentan bug — satu error bisa menyebabkan seluruh sistem crash.
   
   Microkernel, Hanya fungsi-fungsi inti (minimum) yang dijalankan di ruang kernel,
   kelebihan,Lebih stabil dan aman — jika satu layanan rusak, kernel utama tetap berjalan.
   kekurangan,Kinerja lebih lambat — karena komunikasi antar proses lebih mahal dibanding monolithic.
   
   Layered Architecture,Sistem operasi dibangun dalam lapisan (layer), di mana setiap layer hanya berinteraksi dengan layer di atas dan di bawahnya.
   kelebihan,Desain terstruktur — mudah untuk memahami dan memelihara.
   kekurangan,Bisa terjadi overhead jika interaksi antar layer terlalu banyak.**  
2. [Jelaskan perbedaan antara *kernel mode* dan *user mode*.]  
   **kernel mode,Mode eksekusi di mana CPU memiliki akses penuh ke semua sumber daya sistem, termasuk memori, perangkat keras, dan instruksi privileged.
   user mode,Mode eksekusi untuk program aplikasi biasa, di mana akses ke sumber daya sistem dibatasi oleh sistem operasi.:**  
3. [Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.]  
   **Monolithic Kernel dan Microkernel
   **  

---

## Refleksi Diri
Tuliskan secara singkat:
- bagian paling menantabg itu ketika memahami dan membuat diagram arsitektur sistem operasi.
- belajar dengan giat.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
