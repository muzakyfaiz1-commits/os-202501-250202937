
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux  

---

## Identitas
- **Nama**  : Faizal Muzaki
- **NIM**   : 250202937
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.

---

## Dasar Teori
Dasar Teori: Linux sebagai Sistem Operasi Sistem operasi linux dibangun di atas kernel yang mengikuti arsitektur monolitik dan dirancang untuk sistem multi-user dan multi-task . Kedua prinsip ini membentuk dasar teori manajemen proses user. 1. Teori Multi-Tasking Proses Tujuan : Sistem mengizinkan menjalanankan banyak program kali proses secara bersamaan di satu-sama. Broadcast : Sistem mendefinisikan sebuah kolom proses sebagai instance program yang sedang berjalan. Bukan sekadar kode, ia mencakup kode program, data saat ini, tumpukan eksekusi , dan sejumlah sumber daya lainyang dialokasi..getline memori..ENDIF

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
whoami
id
groups

sudo adduser praktikan
sudo passwd praktikan

ps aux | head -10
top -n 1

sleep 1000 &
ps aux | grep sleep

kill <PID>

pstree -p | head -20


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil]()

---

## Analisis
- Penekanan Analisis: Linux (melalui kernel) berhasil menciptakan ilusi konkurensi (simultan) meskipun CPU mungkin hanya menjalankan satu instruksi pada satu waktu (pada core tunggal). Keefektifan manajemen proses terletak pada penjadwal yang adil dan efisien (seperti CFS) yang meminimalkan latency (waktu tunda) dan memaksimalkan throughput (jumlah pekerjaan yang diselesaikan).Aspek Lanjutan: Konsep Zombie Process adalah titik kegagalan manajemen proses yang penting untuk dianalisis. Proses yang mati tetapi masih ada (belum di-reap) menunjukkan leak (kebocoran) pada tabel proses, yang jika berlebihan, dapat menghabiskan sumber daya kernel, bukan memori biasa.2. User & Izin Akses: Keamanan Melalui PemisahanPoin Kunci: Analisis Anda tepat mengenai UID, GID, dan kepemilikan sebagai pilar identitas dan keamanan di Linux.Penekanan Analisis: Mekanisme keamanan Linux didasarkan pada model Discretionary Access Control (DAC). Analisis harus menekankan bahwa DAC memiliki kelemahan: pemilik dapat (secara diskresioner) memberikan izin yang terlalu longgar. Ini yang membuat implementasi Prinsip Hak Istimewa Minimum (Least Privilege) menjadi kritikal.Aspek Lanjutan: Perintah sudo tidak hanya alat administrasi, tetapi secara teoritis adalah implementasi cerdas dari Least Privilege. Ini memungkinkan pembagian tugas (Separation of Duties)—seorang pengguna dapat menjalankan tugas sebagai admin tanpa harus masuk full-time sebagai root.???? Kesimpulan dan Dampak SistemikKonsepTujuan TeoritisDampak pada SistemMulti-Tasking (Proses)Memaksimalkan utilitas CPU dan throughput sistem.Kestabilan: Proses yang gagal tidak akan menjatuhkan seluruh sistem.

---

## Kesimpulan
1. Fungsi Inti: Manajemen Proses (Efisiensi & Stabilitas)Manajemen Proses adalah tulang punggung dari Multi-Tasking.Tujuan Utama: Menciptakan ilusi konkurensi (berjalan secara simultan) melalui penjadwalan CPU (Time-Sharing), yang memungkinkan pemanfaatan sumber daya dan throughput sistem secara maksimal.Mekanisme Kunci: Isolasi proses (setiap proses berjalan di ruang memorinya sendiri), identifikasi unik (PID), dan komunikasi/kontrol melalui sinyal.Dampak: Memastikan bahwa jika satu program crash (gagal), program tersebut tidak akan menjatuhkan seluruh sistem; hal ini menjamin stabilitas sistem.2. Keamanan Inti: Manajemen User & Grup (Keamanan & Akuntabilitas)Manajemen User adalah fondasi dari sistem Multi-User dan lapisan keamanannya.Tujuan Utama: Sumber daya dan tugas dipisahkan di antara pengguna yang berbeda untuk memastikan integritas dan kerahasiaan data.Mekanisme Kunci: Model DAC (Discretionary Access Control), yang diwujudkan melalui kombinasi UID/GID, Kepemilikan (Ownership), dan Izin Akses (Permissions: $r, w, x$).Dampak: Menerapkan Prinsip Hak Istimewa Minimum (Principle of Least Privilege)—yang diperkuat oleh sudo—yang memastikan bahwa setiap pengguna hanya dapat memodifikasi sumber daya yang diizinkan; hal ini menjamin keamanan sistem.Kesimpulan AkhirKeandalan dan dominasi Linux di lingkungan server disebabkan oleh interaksi antara manajemen proses yang efisien (yang menjaga sistem tetap berjalan) dan manajemen user yang ketat (yang menjaga sistem tetap aman).

---

## Quiz
1.  Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?  
   **Jawaban: fungsi utama proses init—atau systemd untuk distribusi modern—pada sistem Linux adalah sebagai proses pertama yang dijalankan oleh kernel. Proses init merupakan cikal bakal dari setiap proses lainnya, dan perannya adalah untuk mempersiapkan sistem agar siap digunakan.**  
2.  Apa perbedaan antara `kill` dan `killall`? 
   **Jawaban:Perbedaan utama antara perintah kill dan killall adalah bahwa kill menargetkan suatu proses berdasarkan nomor ID uniknya, PID, sementara killall menargetkan semua contoh proses sekaligus, berdasarkan nama yang dapat dieksekusi.**  
3.  Mengapa user `root` memiliki hak istimewa di sistem Linux?
   **Jawaban: Pengguna root dalam sistem Linux memiliki hak istimewa khusus karena ia adalah akun Administrator Sistem atau Pengguna Super, yang dimaksudkan untuk memiliki wewenang tak terbatas untuk menjalankan fungsi manajemen dan kontrol penuh atas sistem operasi.**  

---

## Refleksi Diri
biasa saja,syukur saya bisa mengatasinya dengan belajar lebih giat.  

---

**Credit:**   
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
