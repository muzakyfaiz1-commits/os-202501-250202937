
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF  

---

## Identitas
- **Nama**  : Faizal Muzaki  
- **NIM**   : 250202937
- **Kelas** : 1IKRB

---

## Tujuan
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.  
---

## Dasar Teori
Dasar teori penjadwalan CPU mencakup konsep-konsep inti mengenai bagaimana sistem operasi mengelola dan mengalokasikan CPU untuk proses-proses yang bersaing.

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
git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Penjadwalan First-Come, First-Served (FCFS) dan Shortest Job First (SJF) adalah dua algoritma dasar yang digunakan oleh Kernel Sistem Operasi untuk mengelola sumber daya CPU. FCFS adalah algoritma non-preemptive yang sangat sederhana, di mana proses yang tiba pertama akan dilayani pertama kali, mirip dengan antrean FIFO. Kelemahan utamanya adalah Convoy Effect, di mana proses yang membutuhkan waktu CPU burst panjang dapat menahan semua proses pendek yang tiba di belakangnya, sehingga menghasilkan Waktu Tunggu Rata-rata (AWT) yang tinggi dan tidak efisien. Sebaliknya, SJF menjadwalkan proses berdasarkan durasi CPU burst terpendek, dan secara teoritis terbukti optimal karena menghasilkan AWT terendah. Optimalitas ini dicapai karena SJF secara konsisten memilih proses yang paling cepat selesai, yang meminimalkan total waktu di mana proses lain harus menunggu. Namun, SJF memiliki masalah implementasi karena sulit untuk mengetahui durasi burst CPU di masa depan dan rentan terhadap Starvation, di mana proses yang sangat panjang mungkin tidak pernah mendapatkan giliran eksekusi jika aliran proses pendek terus-menerus tiba. Oleh karena itu, sistem operasi modern, seperti Linux dan Windows, menghindari kedua algoritma murni ini dan menggunakan penjadwal yang lebih kompleks (seperti Round Robin atau variannya) untuk mencapai keseimbangan antara efisiensi (AWT rendah seperti SJF) dan keadilan/responsivitas (menghindari Convoy Effect dan Starvation). 

---

## Kesimpulan
Kesimpulan utama adalah bahwa kriteria penjadwalan secara drastis memengaruhi metrik kinerja sistem. FCFS didasarkan pada waktu kedatangan (arrival time), yang sederhana dan adil tetapi rentan terhadap Convoy Effect, menghasilkan waktu tunggu rata-rata yang tinggi. Sebaliknya, SJF didasarkan pada durasi burst CPU terpendek, yang menjadikannya optimal karena meminimalkan total waktu tunggu dan waktu tunggu rata-rata, meskipun memiliki masalah implementasi dalam mengetahui waktu burst di masa depan.

---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?   
   **Jawaban: Perbedaan utama antara First-Come, First-Served (FCFS) dan Shortest Job First (SJF) terletak pada kriteria penentuan proses mana yang akan dieksekusi selanjutnya dan dampaknya terhadap efisiensi sistem (khususnya waktu tunggu rata-rata).**  
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?  
   **Jawaban: Algoritma Shortest Job First (SJF) terbukti secara teoritis sebagai algoritma penjadwalan yang optimal karena menghasilkan waktu tunggu rata-rata (Average Waiting Time / AWT) terpendek untuk sekumpulan proses yang diberikan.**  
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif? 
   **Jawaban: Kelemahan utama algoritma Shortest Job First (SJF) jika diterapkan pada sistem interaktif adalah buruknya waktu respons (response time) dan risiko tinggi terjadinya starvation (kelaparan) pada proses-proses panjang.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- dalam menghitung SJF terdapat sedikit kendala.  
- belajar lebih giat. 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
