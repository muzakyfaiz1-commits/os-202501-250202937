
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Identitas
- **Nama**  : Faizal Muzaki
- **NIM**   : 250202937
- **Kelas** : 1IKRB

---

## Judul 
Analisis dan Simulasi Deteksi Deadlock pada Alokasi Sumber Daya Dapur
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## 1. INTRODUCTION (Pendahuluan)

1.1 Latar Belakang
---
Dalam sistem operasi, pengelolaan sumber daya merupakan aspek yang krisual untuk menjaga kelancaran proses. Salah satu hambatan utama yang sering terjadi adalah deadlock, yaitu kondisi dimana sekumpulan proses berhenti secara permanen karena saling menunggu sumber daya yang dikuasai oleh proses lain dalam kelompok tersebut. Simulasi ini menggunakan analogi dapur restoran untuk mempermudah pemahaman mekanisme deadlock pada sistem nyata.

1.2 Rumusaan Masalah 
---
Berdasarkan latar belakang masalah yang telah di uraikan, maka rumusan masalah dalam pratikum ini adalah sebagai berikut:

1. bagaimana cara mengidentifikasi kondisi deadlock pada sistem sumber daya instansi tunggal menggunakan algoritma wait-For Graph?
2. Bagaimana mekanisme terjadinya ketergantungan melingkar pada skenario alokasi sumber daya di dapur restoran?
3. Sejauh mana efektivitas metode Resource Preemption (pengambilalihan paksa) dalam memulihkan sistem dari kondisi deadlock?

1.3 Tujuan Praktikum
---
Praktikum ini bertujuan untuk:
1. mengimplementasikan algoritma deteksi deadlock berbasis wait-For Graph menggunakan bahasa python.
2. Menganalisis skenario alokasi sumber daya dapur untuk membuktikan terjadinya circular wait.
3. Mensimulasikan strategi pemulihan melalui metode Resource Preemption.

---

## 2. METHODS (Metodologi Penelitian)
---

2.1 Lingkungan uji
---
Praktikum dilakukan pada lingkungan perangkat lunak sebagai berikut:
- Sistem Operasi: Windows 11 (Host).
- Bahasa Pemrograman: Python 3.10.
- Alur Bantu: Visual Studi Code/Terminal.

2.2 Dataset dan Parameter 
---
Dataset menggunakan analogi operasional dapur dengan 3 proses (koki) dan 3 sumber daya (alat masak). Kondisi diatur sedemikian rupa agar memenuhi syarat mutlak deadlock.

### Tabel 1. Parameter Alokasi dan Permintaan Sumber Daya

| Proses (Proses) | Alokasi (Allocation) | Permintaan (Request) |
| :--- | :--- | :--- |
| **Koki Pasta (P1)** | Panci (R1) | Kompor (R2) |
| **Koki Steak (P2)** | Kompor (R2) | Pisau (R3) |
| **Koki Salad (P3)** | Pisau (R3) | Panci (R1) |


2.3 Langkah Eksperimen 
---
1. Deteksi: menjalankan skrip ```deadlock_detection.py``` untuk membangun graf ketergantungan dan mencari siklus melingkat.
2. Analisis: Memverivikasi hasil deteksi dengan teori empat syarat Coffman (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait).
3. Pemulihan: Menjalankan skrip ```deadlock_solution.py``` untuk melakukan preemption pada salah satu proses agar siklus terputus.

---
## 3. RESULT (hasil)

3.1 Ringkasan Temuan 
---
Berdasarkan eksekusi program, sistem berhasil mendeteksi adanya kebuntuan total pada ketiga koki yang terlibat. Program mendeteksi rantai ketergantungan:

P1->P2->P3->P1

### Tabel 2. Hasil Status Eksekusi Sistem

| Nama Program | Temuan Utama | Status Akhir |
| :--- | :--- | :--- |
| `deadlock_detection.py` | Terdeteksi Siklus: P1, P2, P3 | **Sistem Deadlock** |
| `deadlock_solution.py` | Preemption pada Koki Salad (P3) | **Sistem Aman** |



3.2 Bukti Eksekusi
---
1. Hasil Eksekusi kode ```Deadlock_Detection.py```

![Screenshot hasil](screenshots/detection.png)

- Interpretasi Dataset:
   - P1 (koki pasta) memegang panci, tapi butuh kompor.
   - P2 (koki steak) memegang kompor, tapi butuh pisau.
   - P3 (koki salad) memegang pisau, tapi butuh panci.
- Temuan Algoritma: program berhasil mendeteksi adanya siklus ketergantungan melingkar (Circular Wait). Karena setiap koki memegang alat yang dibutuhkan koki lain dan tidak ada yang mau melepasnya (Hold and Wait), sistem terkunci secara permanen.
- Hasil akhir: status dinyatakan SISTEM DEADLOCK! dengan melibatkan ketiga koki tersebut.


   
2. Hasil Eksekusi ```deadlock_solution.py```

![Screenshot hasil](screenshots/solution.png)

- Langkah Solusi: Sistem melakukan intervensi dengan memilih satu "korban", yaitu koki salad (P3), untuk dipaksa melepaskan pisau (R3) secara sementara.

- Proses Pemulihan:
   1. Pisau (R3) diberikan kepada koki steak (P2).
   2. P2 dapat menyelesaikan tugasnya dan melepaskan semua alat (kompor & pisau).
   3. Setelah alat-alat tersebut bebas, koki lainnya (P1 dam P3) dapat bergantian menyelesaikan tugasnya.

- Hasil Akhir: Status dinyatakan DEADLOCK BERHASIL DIATASI, membuktikan bahwa pengambilan paksa sumber daya dapat memutuskan rantai kebuntuan sistem.




---
### 4. Discussion (Pembahasan)

4.1 Interpretasi Hasil
---
Hasil eksperimen menunjukan bahwa deadlock terjadi karena terpenuhinya kondisi Circular Wait. Koki Salad (P3) tidak dapat melepaskan pisau karena menunggu panci yang dibawa koki pasta (P1). Hal ini membuktikan bahwa pada sistem dengan single-instance resource, adanya siklus pada wait-For Graph adalah indikator mutlak terjadinya deadlock.

4.2 Perbandingan Teori dan Implementasi Solusi
---
Secara teori, deadlock dapat diatasi dengan membatalkan proses atau merampas sumber daya (preemption). Dalam simulasi ini, sistem memilih P3 sebagai "korban" untuk melepaskan sumber daya. Meskipun efektif, metode ini memiliki keterbatasan berupa hilangnya proses kerja pada proses yang dipaksa berhenti (preemption). hal ini sesuai dengan literatur yang menyatakan bahwa deteksi dan pemulihan sering kali menyebabkan overhead pada sistem.

---
### 5. Kesimpulan

Algoritma deteksi berbasis graf berhasil mengidentifikasi deadlock dengan melacak jalur melingkar antar proses koki.
Kondisi deadlock di dapur secara sempurna memenuhi empat syarat Coffman, terutama Circular Wait dan Hold and Wait.
Strategi Resource preemption terbukti mampu memulihkan sistem ke kondisi aman, meskipun memerlukan intervensi eksternal untuk memilih proses yang dikorbankan.


---

## Daftar pustaka

Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts. 10th Edition. John Wiley & Sons.

Tanenbaum, A. S., & Bos, H. (2014). Modern Opera

---










---

## Quiz
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?  
   **Jawaban:**  
   - Struktur Logis: Memandu pembaca memahami alur pikir peneliti, mulai dari latar belakang masalah hingga kesimpulan yang diambil.
   - Standarisasi: Dengan format yang seragam, dosen atau evaluator dapat langsung menemukan informasi spesifik (misalnya mencari data di bagian Results) tanpa harus membaca keseluruhan teks.
   - Reproduksibilitas: Bagian Methods yang terpisah memastikan percobaan dapat diulang oleh orang lain, yang merupakan syarat utama sebuah penelitian dianggap ilmiah.
   - Objektivitas: Memisahkan antara data mentah (Hasil) dengan interpretasi subjektif (Pembahasan), sehingga pembaca bisa menilai apakah kesimpulan penulis didukung oleh data yang ada.
   
2. Apa perbedaan antara bagian Hasil dan Pembahasan?  
   **Jawaban:** 
   - hasil adalah sebuah proses akhir dalah sebuah eksperimen.
   - pembahasan adalah sebuah proses inti dalam eksperimen. 
3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?  
   **Jawaban:**
   - Menghindari Plagiarisme: Memberikan kredit kepada penulis asli atas ide, teori, atau data yang kita kutip.
   - Landasan Teori yang Kuat: Menunjukkan bahwa praktikan memahami dasar ilmiah di balik percobaan dan tidak sekadar "mengarang" asumsi.
   - alidasi Data: Memungkinkan pembaca atau dosen untuk melacak sumber asli jika mereka ingin memverifikasi informasi atau mendalami topik tersebut.  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
