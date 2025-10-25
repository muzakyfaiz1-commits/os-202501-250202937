
# Laporan Praktikum Minggu [3]
Topik: [anajemen File dan Permission di Linux ]

---

## Identitas
- **Nama**  : [Faizal Muzaki]  
- **NIM**   : [250202937]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
.Tujuan utama dari praktikum ini adalah agar mahasiswa mampu **mengoperasikan perintah Linux dasar dengan benar**, memahami sistem izin (permission), dan mendokumentasikan hasilnya dalam format laporan Git.


---

## Dasar Teori
**pengelolaan file dan direktori menggunakan perintah dasar Linux**, serta konsep **permission dan ownership**. 
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
-
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
-   
- hubungan dengan kernel:Variasi waktu eksekusi ini adalah bukti langsung dari fungsi Kernel Scheduler. Kernel secara aktif mengatur dan membagi waktu CPU di antara proses-proses yang bersaing, sehingga memengaruhi latensi (waktu tunggu) dan throughput (jumlah pekerjaan yang diselesaikan). Hasil Anda mengukur efektivitas atau overhead dari proses scheduling Kernel tersebut.
  hubungan dengan arsitektur system call: ubungan dengan Teori: Perbedaan waktu yang signifikan antara kedua jenis operasi tersebut secara langsung disebabkan oleh overhead System Call. Operasi I/O memerlukan transisi dari user space ke kernel space melalui System Call (seperti read() atau write()). Transisi ini mahal secara komputasi karena melibatkan perubahan mode CPU dan validasi parameter. Hasil Anda mengukur biaya dari komunikasi user-kernel ini. 
- Linux umumnya memiliki latensi System Call yang lebih rendah karena sebagian besar layanan berada di ruang Kernel yang sama. Windows memiliki lapisan abstrak yang dapat menambah overhead.
---

## Kesimpulan
1.Hubungan Variabel: Bagaimana variabel independen memengaruhi variabel dependen (hipotesis terbukti atau ditolak).

2.Hasil Utama: Temuan paling signifikan atau tidak terduga dari data.

3.Implikasi/Penerapan: Pentingnya hasil eksperimen tersebut bagi bidang studi terkait.

---

## Quiz
1. [Apa fungsi dari perintah `chmod`?]  
   **jawaban: untuk mengubah mode izin pada berkas dan direktori.**  
2. [Apa arti dari kode permission `rwxr-xr--`? ]  
   **Jawaban: rwx: membaca,mengubah,dan menjalankan. r-x:membaca dan menjalankan tugas tapi tidak dapat di modifikasi. r--:menjalankan tapi tidak dapat dimodifikasi.**  
3. [Jelaskan perbedaan antara `chown` dan `chmod`. ]  
   **Jawaban:Perbedaan utama antara chown dan chmod terletak pada fungsi yang mereka tangani dalam sistem operasi mirip Unix (seperti Linux). Keduanya adalah perintah baris yang digunakan untuk mengelola perizinan dan kepemilikan berkas atau direktori.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- bagian tersulit bagi saya itu pada eksperimennya.  
- cara mengatasinya yaitu terus mencoba dan bertanya kepada orang yang lebih mengerti.  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
