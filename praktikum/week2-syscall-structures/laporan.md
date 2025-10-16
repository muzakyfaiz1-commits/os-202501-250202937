
# Laporan Praktikum Minggu [2]
Topik: [Struktur System Call dan Fungsi Kernel  
"]

---

## Identitas
- **Nama**  : [Faizal Muzaki]  
- **NIM**   : [250202937]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.


---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **mekanisme system call dan struktur sistem operasi**.  
System call adalah antarmuka antara program aplikasi dan kernel yang memungkinkan aplikasi berinteraksi dengan perangkat keras secara aman melalui layanan OS.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

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
- Percobaan mengenai system call dan peran kernel memperlihatkan secara nyata bagaimana sistem operasi bekerja sebagai penghubung antara program pengguna dan perangkat keras. Dalam sistem komputer modern, program tidak memiliki izin untuk mengakses perangkat keras secara langsung karena alasan keamanan dan kestabilan sistem. Untuk itu, diperlukan mekanisme perantara berupa system call, yaitu layanan yang disediakan oleh kernel agar aplikasi di ruang pengguna dapat meminta bantuan sistem, seperti membuka file, mengelola proses, atau mengakses perangkat input/output.

Berdasarkan hasil percobaan, terlihat bahwa setiap kali program melakukan operasi seperti membaca (read()), menulis (write()), atau membuat proses baru (fork()), terjadi perpindahan dari user mode ke kernel mode. Perpindahan ini disebut context switch, yaitu momen di mana sistem operasi mengambil alih kendali untuk mengeksekusi instruksi yang memerlukan hak akses lebih tinggi. Hasil ini mendukung teori dasar bahwa kernel berperan sebagai pengendali utama seluruh sumber daya sistem, sedangkan user mode hanya memiliki izin terbatas untuk menjalankan aplikasi.

Dari sisi fungsi, kernel memiliki beberapa tanggung jawab utama: mengatur proses, memori, sistem berkas, serta perangkat I/O. Saat system call dijalankan, kernel menanganinya sesuai dengan kebijakan dan struktur internal sistem operasi. Misalnya, pada pemanggilan fork() di Linux, kernel menduplikasi proses induk untuk membuat proses anak yang identik, menunjukkan bahwa kernel mengontrol penuh daur hidup proses. Begitu pula pada operasi read() dan write(), kernel bertugas mengatur komunikasi dengan perangkat keras melalui device driver yang relevan. Hasil ini menunjukkan peran kernel sebagai inti koordinasi antara perangkat keras dan perangkat lunak.

Dari perspektif arsitektur sistem operasi, perbedaan hasil antara Linux dan Windows dapat dijelaskan melalui desain kernel masing-masing. Linux menggunakan monolithic kernel, di mana seluruh komponen inti seperti manajemen memori, file system, dan driver berada dalam satu ruang kernel. Karena semua layanan dijalankan di tingkat kernel yang sama, system call pada Linux cenderung lebih cepat dan efisien. Hasil percobaan biasanya menunjukkan waktu tanggapan yang lebih rendah dibandingkan sistem lain.

Sebaliknya, Windows memakai hybrid kernel, yaitu perpaduan antara konsep monolithic dan microkernel. Beberapa fungsi dijalankan di ruang pengguna untuk menjaga stabilitas dan keamanan sistem. Walaupun lebih aman, pendekatan ini menambah sedikit overhead dalam pemanggilan system call. Selain itu, Windows membatasi akses langsung terhadap system call mentah dan lebih sering menggunakan Windows API (Win32) sebagai lapisan komunikasi.

Secara keseluruhan, hasil percobaan membuktikan teori bahwa kernel berfungsi sebagai pengatur utama interaksi antara aplikasi dan perangkat keras, dengan system call sebagai mekanisme komunikasinya. Perbedaan arsitektur kernel antara Linux dan Windows menghasilkan variasi performa, namun keduanya memiliki tujuan yang sama: menciptakan sistem yang efisien, aman, dan stabil bagi pengguna.
---

## Kesimpulan
Berdasarkan hasil praktikum yang telah dilakukan, dapat disimpulkan bahwa kernel memiliki peran sentral dalam sistem operasi sebagai pengelola utama seluruh sumber daya komputer, meliputi prosesor, memori, sistem berkas, dan perangkat input/output. Proses komunikasi antara program pengguna dan kernel berlangsung melalui system call, yang berfungsi sebagai pintu masuk resmi agar aplikasi dapat meminta layanan sistem dengan aman tanpa mengakses perangkat keras secara langsung.

Hasil pengamatan menunjukkan bahwa setiap kali terjadi pemanggilan system call, sistem berpindah dari user mode ke kernel mode untuk mengeksekusi instruksi dengan hak akses penuh. Hal ini membuktikan bahwa kernel mode memiliki kontrol penuh terhadap perangkat keras, sedangkan user mode dibatasi untuk menjaga keamanan dan stabilitas sistem. Dengan demikian, system call menjadi mekanisme penting dalam memastikan bahwa operasi sistem berjalan terkendali dan terproteksi.

Dari hasil perbandingan lingkungan sistem operasi, ditemukan bahwa perbedaan arsitektur kernel berpengaruh terhadap kinerja dan cara sistem menangani system call. Pada Linux, yang menggunakan monolithic kernel, semua komponen inti berada di dalam ruang kernel, sehingga proses system call dapat dijalankan lebih cepat dan efisien. Sementara pada Windows, yang menerapkan hybrid kernel, sebagian fungsi dijalankan di ruang pengguna untuk meningkatkan keamanan dan stabilitas, meskipun menyebabkan sedikit peningkatan overhead saat pemanggilan layanan sistem.

Secara keseluruhan, praktikum ini membuktikan bahwa teori mengenai fungsi kernel dan mekanisme system call terbukti nyata melalui hasil percobaan. Kernel tidak hanya berperan sebagai pengatur utama sumber daya, tetapi juga sebagai jembatan yang memastikan komunikasi antara perangkat lunak dan perangkat keras berlangsung aman, efisien, serta terstruktur. Perbedaan hasil antara Linux dan Windows menunjukkan bahwa setiap sistem operasi memiliki pendekatan desain yang berbeda, namun keduanya memiliki tujuan yang sama: menciptakan sistem yang stabil, aman, dan optimal bagi pengguna.

---

## Quiz
1. [Apa fungsi utama system call dalam sistem operasi? ]  
   **sebagai jembatan interaksi antara pengguna dengan kernel:**  
2. [Sebutkan 4 kategori system call yang umum digunakan.  ]  
   **pengendalian proses,manajemen berkas,manajemen perangkat,dan pemeliharaan informasi sistem.**  
3. [Mengapa system call tidak bisa dipanggil langsung oleh user program?]  
   **karena alasan keamanan,stabilitas, dan kontrol sistem operasi**  

---

## Refleksi Diri
Tuliskan secara singkat:
- memahami system call dan fungsi kernel,karena ini menjadi suatu hal yang saya pahami.  
- dengan memahami lebih dalam tentang system call dan fungsi kernel

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
