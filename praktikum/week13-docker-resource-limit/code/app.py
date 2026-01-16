import time
import os

def stress_test():
    print("--- Memulai Stress Test Resource ---")
    print(f"PID: {os.getpid()}")
    
    # List untuk menampung data (Stress Memori)
    memory_hog = []
    
    try:
        for i in range(1, 11):
            print(f"\nIterasi ke-{i}")
            
            # Simulasi penggunaan CPU (Perhitungan berat)
            start_time = time.time()
            while time.time() - start_time < 2: # Lakukan loop selama 2 detik
                _ = 1000 * 1000
            
            # Simulasi penggunaan Memori (Menambah 50MB setiap iterasi)
            data = ' ' * (50 * 1024 * 1024) 
            memory_hog.append(data)
            
            print(f"Status: CPU bekerja, Memori bertambah ~{i * 50}MB")
            
    except MemoryError:
        print("\n[ERROR] Out of Memory! Container kehabisan RAM.")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    stress_test()