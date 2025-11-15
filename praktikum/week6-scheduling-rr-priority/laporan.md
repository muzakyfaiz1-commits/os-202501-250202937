
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling 
---

## Identitas
- **Nama**  : Faizal Muzaki  
- **NIM**   : 250202937
- **Kelas** : 1IKRB

---

## Tujuan
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  


---

## Dasar Teori
Penjadwalan CPU (CPU Scheduling) merupakan mekanisme dalam sistem operasi untuk memilih proses mana yang berhak menggunakan CPU pada suatu waktu tertentu. Tujuan utamanya adalah mengoptimalkan kinerja sistem dengan menjaga efisiensi, fairness, dan tingkat respons yang baik. Penjadwal CPU bekerja ketika proses berpindah dari running ke waiting, selesai, atau ketika terjadi interrupt.

Algoritma penjadwalan berbeda satu sama lain berdasarkan metode pemilihan proses berikutnya dan kebijakan preemption/non-preemption. Dua di antaranya adalah Round Robin dan Priority Scheduling.

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Penjadwalan CPU berfungsi mengatur proses agar penggunaan CPU berlangsung efisien, adil, dan responsif. Dua algoritma yang umum digunakan adalah Round Robin (RR) dan Priority Scheduling, masing-masing dengan karakteristik serta dampaknya terhadap performa sistem.

Round Robin menekankan fairness dengan memberikan setiap proses jatah waktu yang sama (time quantum). Pendekatan ini cocok untuk sistem time-sharing karena memberikan respons cepat bagi banyak proses secara bergantian. Namun performanya sangat dipengaruhi besar-kecilnya quantum. Quantum terlalu kecil menimbulkan overhead besar akibat context switching berlebihan, sementara quantum terlalu besar mengurangi responsiveness dan perilakunya mendekati FCFS. Dengan demikian, keseimbangan ukuran quantum menjadi faktor penting untuk menjaga efisiensi sekaligus kenyamanan pengguna.

Di sisi lain, Priority Scheduling berfokus pada pentingnya proses. CPU selalu memilih proses dengan prioritas tertinggi terlebih dahulu. Hal ini bermanfaat untuk sistem real-time atau proses kritis di mana beberapa tugas harus diproses secepat mungkin. Namun pendekatan ini menimbulkan risiko starvation, yaitu ketika proses prioritas rendah terus-menerus tertunda jika ada proses prioritas tinggi yang datang secara berurutan. Untuk mengatasi hal ini, sistem harus menerapkan teknik seperti aging untuk menaikkan prioritas proses yang terlalu lama menunggu.

Jika dibandingkan, RR lebih adil dan cocok untuk sistem interaktif, sedangkan Priority Scheduling lebih baik untuk kebutuhan kritis namun berisiko tidak adil. Keduanya menuntut pengaturan parameter yang tepat—RR membutuhkan quantum optimal, Priority membutuhkan mekanisme pencegah starvation.

Secara keseluruhan, kombinasi atau variasi dari kedua algoritma ini biasanya digunakan dalam sistem operasi modern agar mendapatkan keseimbangan antara respons cepat, efisiensi, dan penanganan proses penting tanpa mengorbankan proses lain. 

---

## Kesimpulan
Round Robin cocok untuk sistem interaktif karena memberi giliran yang adil pada semua proses, tetapi performanya sangat bergantung pada ukuran time quantum. Priority Scheduling efektif untuk menangani proses penting terlebih dahulu, namun dapat menyebabkan starvation bagi proses berprioritas rendah. Tidak ada algoritma yang sempurna—pemilihannya harus disesuaikan dengan kebutuhan sistem.

---

## Quiz
1.  Apa perbedaan utama antara Round Robin dan Priority Scheduling? 
   **Jawaban: - RR fokus pada keadilan dan berbagi waktu secara merata, tanpa memandang pentingnya proses.
   - Priority Scheduling fokus pada pentingnya proses, sehingga urutan eksekusi ditentukan oleh prioritas, bukan giliran.  **  
2.  Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?  
   **Jawaban: - Quantum terlalu kecil → sistem sangat responsif, tapi overhead tinggi karena banyak context switching.
   - Quantum terlalu besar → overhead rendah, tapi respons time buruk dan sistem terasa lambat.**  
3. Mengapa algoritma Priority dapat menyebabkan *starvation*?    
   **Jawaban: Algoritma Priority Scheduling dapat menyebabkan starvation karena proses berprioritas rendah terus tertunda dan tidak pernah mendapat giliran eksekusi jika selalu ada proses dengan prioritas lebih tinggi yang masuk ke sistem.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- saya mengalami kesulitan dalam perhitungan nya.  
- belajar lebih giat.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
