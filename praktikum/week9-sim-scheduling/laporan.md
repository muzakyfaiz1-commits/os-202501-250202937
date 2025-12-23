
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU 

---

## Identitas
- **Nama**  : Faizal Muzaki 
- **NIM**   : 250202937 
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
-  Tujuan Utama: Menjamin efisiensi sistem dengan memaksimalkan CPU  Utilization (menjaga CPU tetap sibuk) dan meminimalkan Waiting Time (waktu tunggu proses di antrean).
-  Kriteria Metrik: Keberhasilan algoritma diukur melalui Turnaround Time (total waktu dari proses masuk hingga selesai) dan Throughput (jumlah proses yang diselesaikan per satuan waktu).
-  Burst Time & Quantum: Burst Time adalah durasi yang dibutuhkan proses pada CPU, sedangkan Time Quantum adalah batas waktu maksimal sebuah proses boleh menggunakan CPU sebelum dipindahkan kembali ke antrean (khusus Round Robin).

---

## Langkah Praktikum
1. Siapkan folder kerja praktikum/week9-sim-scheduling/.
2. Membuat file dataset.csvyang berisi daftar proses (P1, P2, P3, P4) lengkap dengan Arrival Time dan Burst Time .
3. Membuat program Python sederhana yang membaca file CSV, mengurutkan data berdasarkan waktu kedatangan, dan menghitung waktu tunggu secara berurutan.
4. Jangkauan program di terminal dan membandingkan hasilnya dengan hitungan manual.
5. Mendokumentasikan seluruh hasil simulasi, perhitungan, dan analisis dalam file laporan.md. 
6. Melakukan commit dan push hasil praktikum ke repositori GitHub.
   
```bash
git add .
git commit -m "Minggu 9 - Simulasi Scheduling CPU"
git push origin main
```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](./screenshots/ss.png)

![screenshots hasil](./screenshots/ss2.png)

perintah:
```bash
python code/scheduling_simulation.py

```

---

## Analisis
Berikut adalah keluaran program saat dijalankan dengan dataset uji:

![screenshot hasil](./screenshots/ss3.png)

1. Alur Program (Workflow)
   
   Program penjadwalan ini bekerja dengan alur linear sebagai berikut:

   1. Inisialisasi Data: Program menyimpan daftar proses, Arrival Time (AT), dan Burst Time (BT) ke dalam struktur data (seperti array atau list).
   2. pengurutan (sorting): program memastikan proses diurutkan berdasarkan AT terkecil. pada kasus data ini, proses sudah urut (0, 1, 2, 3).
   3. pertungan waktu selesai (CT): proses pertama selesai pada saat AT+BT.
   4. perhitungan metrik:
   - TAT: dihitung dengan CT-AT.
   - WT: dihitung dengan TAT-BT.
   5. Output: program merangkum semua data ke dalam format tabel agar mudah di baca oleh pengguna.

2. Perbedaan Hasil simulasi vs manual
   Berdasarkan dataset dari gambar:

   - P1:AT=0,BT=6
   - P2:AT=1,BT=8
   - P3:AT=2,BT=7
   - P4:AT=3,BT=3

3. Kelebihan dan Kerbatasan simulasi

   Kelebisan:
   -  Kecepatan: Simulasi dapat menghitung ratusan hingga ribuan proses dalam hitungan milidetik, jauh lebih cepat daripada menghitung manual dengan kertas.
   -  Minim Human Error: Menghindari kesalahan hitung (akritmatika) yang sering terjadi pada perhitungan manual yang panjang.
   -  Fleksibilitas: Kita bisa dengan mudah mengubah data input (misal: mengganti Burst Time) dan melihat hasilnya secara instan tanpa menghitung ulang dari awal.
  
   keterbatasan:
    - Statik (Non-Real Time): Simulasi ini bersifat matematis. Dalam sistem operasi nyata, ada faktor luar seperti overhead perpindahan konteks (context switch) dan interupsi yang tidak sepenuhnya terpotret dalam simulasi sederhana ini.
    - Kelemahan Algoritma (Convoy Effect): Simulasi FCFS menunjukkan kelemahan algoritma itu sendiri; jika proses pertama sangat lama (BT besar), proses pendek di belakangnya harus menunggu lama, meskipun simulasi berjalan "sukses".
    - Ketergantungan Input: Jika data input (AT/BT) salah dimasukkan, hasil simulasi akan tetap keluar namun secara logika sistem operasi menjadi tidak valid.
   ---

## Kesimpulan
- Efektivitas Algoritma FCFS: Berdasarkan hasil simulasi, algoritma First-Come, First-Served sangat mudah diimplementasikan karena logikanya yang sederhana (sesuai urutan kedatangan). Namun, praktikum ini menunjukkan bahwa FCFS cenderung menghasilkan Waiting Time yang tinggi jika proses awal memiliki Burst Time yang besar, sebagaimana terlihat pada P2 yang harus menunggu selesainya P1.
- Akurasi Perhitungan Sistem: Simulasi program membuktikan bahwa perhitungan Turnaround Time (TAT) dan Waiting Time (WT) dapat dilakukan secara otomatis dengan hasil yang identik dengan perhitungan manual. Hal ini menunjukkan bahwa logika pemrograman dapat menggantikan kalkulasi manual untuk menghindari human error pada dataset yang lebih besar.


---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?
   
   **Jawaban**: Simulasi sangat krusial dalam pengembangan sistem operasi karena menjembatani teori matematis dengan implementasi nyata.
   
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
   **Jawaban**:
   1. Skalabilitas dan Kecepatan
   - Manual: Perhitungan manual memiliki keterbatasan fisik. Menghitung Waiting Time untuk 1.000 proses secara manual sangat tidak mungkin dilakukan karena membutuhkan waktu berhari-hari dan ruang kertas yang sangat luas.
   - Simulasi: Program komputer dapat memproses ribuan data dalam hitungan milidetik. Komputer menggunakan struktur data seperti Linked List atau Queue yang sangat efisien untuk menangani volume data besar.
   2. Akurasi (Human Error vs. Precision)
   - Manual: Semakin besar dataset, semakin tinggi probabilitas kesalahan manusia (human error). Kesalahan kecil pada penjumlahan Burst Time di awal (proses ke-5 misalnya) akan mengakibatkan kesalahan beruntun pada seluruh perhitungan proses berikutnya (proses ke-6 hingga ke-1000).
   - Simulasi: Program memiliki presisi matematis yang konsisten. Selama logika kodenya benar, hasil untuk proses ke-1 maupun proses ke-1.000 akan memiliki tingkat akurasi yang sama.
  
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
    
   **Jawaban**: 

   1. Logika Sederhana (Prinsip Antrean)
      
      FCFS bekerja persis seperti antrean di kasir supermarket. Program hanya perlu memproses siapa yang datang lebih dulu tanpa perlu mempertimbangkan variabel lain. Tidak ada kriteria rumit yang harus diperiksa oleh CPU.

   2. Tanpa Pengurutan Ulang (No Re-sorting)
   
      Dalam FCFS, urutan eksekusi bersifat statis. Sekali proses masuk ke antrean, posisinya tidak akan berubah. Bandingkan dengan algoritma lain (seperti SJF atau Priority) di mana program harus terus-menerus membandingkan dan mengurutkan ulang isi antrean setiap kali ada proses baru yang datang.
   
   3. Kode Program Minimalis
      
      Karena alurnya linear, struktur kode FCFS sangat pendek. Program hanya membutuhkan satu perulangan (loop) sederhana untuk menghitung waktu penyelesaian, tanpa memerlukan fungsi pencarian nilai minimum atau manajemen antrean prioritas yang kompleks.
         
  
  ---

## Refleksi Diri
Tuliskan secara singkat:
- hal yang paling menantang yaitu; mengimplementasikan algoritma 
- solusi: belajar lebih giat dan mencari referensi atau bertanya kepada teman yang lebih paham. 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
