
```bash
def deadlock_detection():
    # 1. MENYIAPKAN DATASET (Membaca data proses dan resource)
    # P1-P3: Koki, R1-R3: Alat Masak
    dataset = [
        {"proses": "Koki Pasta (P1)", "allocation": "Panci (R1)", "request": "Kompor (R2)"},
        {"proses": "Koki Steak (P2)", "allocation": "Kompor (R2)", "request": "Pisau (R3)"},
        {"proses": "Koki Salad (P3)", "allocation": "Pisau (R3)", "request": "Panci (R1)"}
    ]

    print("=== DATASET PRODUKSI DAPUR ===")
    print(f"{'Proses':<18} | {'Allocation':<12} | {'Request':<12}")
    print("-" * 50)
    for d in dataset:
        print(f"{d['proses']:<18} | {d['allocation']:<12} | {d['request']:<12}")

    # 2. MENENTUKAN KONDISI DEADLOCK
    # Mapping: Siapa yang memegang resource apa
    resource_owner = {d['allocation']: d['proses'] for d in dataset}
    
    # Membangun Wait-For Graph (Siapa menunggu Siapa)
    wait_for_graph = {}
    for d in dataset:
        pengirim = d['proses']
        target_res = d['request']
        if target_res in resource_owner:
            wait_for_graph[pengirim] = resource_owner[target_res]

    # Fungsi untuk mendeteksi siklus melingkar
    def find_cycle(start_node):
        visited = []
        current = start_node
        while current in wait_for_graph and current not in visited:
            visited.append(current)
            current = wait_for_graph[current]
            if current == start_node:
                return visited
        return None

    # Mencari proses yang terjebak dalam siklus
    deadlocked_processes = set()
    for d in dataset:
        cycle = find_cycle(d['proses'])
        if cycle:
            for p in cycle:
                deadlocked_processes.add(p)

    # 3. MENAMPILKAN HASIL
    print("\n=== HASIL DETEKSI ===")
    if deadlocked_processes:
        print("STATUS: SISTEM DEADLOCK!")
        print("Proses yang terlibat:")
        for i, p in enumerate(sorted(deadlocked_processes), 1):
            print(f"{i}. {p}")
    else:
        print("STATUS: SISTEM AMAN")

if __name__ == "__main__":
    deadlock_detection()

```