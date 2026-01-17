```bash
import time

def deadlock_solution():
    # 1. DATASET: Kondisi Awal Terdeteksi Deadlock
    # Struktur: {Proses: [Resource_Held, Resource_Needed]}
    dapur = {
        "Koki Pasta (P1)": {"hold": "Panci (R1)", "need": "Kompor (R2)"},
        "Koki Steak (P2)": {"hold": "Kompor (R2)", "need": "Pisau (R3)"},
        "Koki Salad (P3)": {"hold": "Pisau (R3)", "need": "Panci (R1)"}
    }

    print("=== MONITORING DAPUR: STATUS AWAL ===")
    for koki, alat in dapur.items():
        print(f"[*] {koki} sedang memegang {alat['hold']} dan menunggu {alat['need']}")
    
    # 2. DETEKSI SIKLUS
    # Membangun wait-for graph: Siapa menunggu Siapa
    # P1 -> P2 (karena P2 pegang Kompor), dst.
    holder_map = {v['hold']: k for k, v in dapur.items()}
    wait_for_graph = {k: holder_map[v['need']] for k, v in dapur.items()}
    
    def find_cycle(start_node):
        visited = []
        curr = start_node
        while curr in wait_for_graph and curr not in visited:
            visited.append(curr)
            curr = wait_for_graph[curr]
            if curr == start_node: return visited
        return None

    cycle = find_cycle("Koki Pasta (P1)")

    # 3. IMPLEMENTASI SOLUSI (RESOURCE PREEMPTION)
    print("\n=== ANALISIS & SOLUSI ===")
    if cycle:
        print(f"!! ALERT: Terdeteksi Siklus Deadlock: {' -> '.join(cycle)} -> {cycle[0]}")
        
        # Langkah Solusi: Pilih satu koki untuk dipaksa mengalah (Preemption)
        korban = cycle[-1]
        alat_lepas = dapur[korban]['hold']
        target_koki = [k for k, v in dapur.items() if v['need'] == alat_lepas][0]
        
        print(f"[SOLUSI] Meminta {korban} untuk melepaskan {alat_lepas} sementara.")
        print(f"[ACTION] {alat_lepas} diberikan kepada {target_koki}...")
        
        # Simulasi Pemulihan Jalur
        time.sleep(1)
        print(f"\n[+] {target_koki} SELESAI memasak dan melepaskan semua alat.")
        print(f"[+] Jalur terbuka, koki lainnya sekarang dapat menyelesaikan tugas.")
        print("\nSTATUS: DEADLOCK BERHASIL DIATASI.")
    else:
        print("Sistem berjalan normal.")

if __name__ == "__main__":
    deadlock_solution()

```