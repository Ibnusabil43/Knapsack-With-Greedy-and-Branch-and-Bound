def greedyKnapsack(components, max_budget):
    taken = []  # Daftar komponen yang dipilih
    total_harga = 0  # Total harga komponen yang dipilih
    total_priority = 0  # Total priority komponen yang dipili

    for component in components:
        
        name, harga, priority = component
        if total_harga + harga <= max_budget:  # Jika total harga + harga komponen masih tidak melebihi budget maksimum
            taken.append(component)  # Tambahkan komponen ke dalam daftar taken
            total_harga += harga  # Tambahkan harga komponen ke total_harga
            total_priority += priority  # Tambahkan priority komponen ke total_priority

    return taken, total_priority, total_harga


# Contoh penggunaan
components = [
    ("Intel Core I7-13700K", 350, 15),
    ("NZXT N7 Z790 (Motherboard)", 250, 8),
    ("Corsair Vengeance DDR4 32GB (RAM)", 150, 7),
    ("Cooler Master V650 Gold (PSU)", 100, 7),
    ("Gigabyte RTX 3060 Ti Vision (VGA)", 500, 10),
    ("WD Blue NVME 1TB (Storage)", 120, 8),
    ("NZXT H5 Flow (Casing)", 70, 6),
    ("NZXT 240 RGB Elite (Cooler)", 50, 5)
]

componentsbyWeight = sorted(components, key=lambda x: x[1])  # Urutkan komponen berdasarkan harga secara ascending
componentsbyProfit = sorted(components, key=lambda x: x[2], reverse=True)  # Urutkan komponen berdasarkan priority secara descending
componentsbyDensity = sorted(components, key=lambda x: x[2] / x[1], reverse=True)  # Urutkan komponen berdasarkan density secara descending

max_budget = 500

print("========== GREEDY BY WEIGHT ==========")
taken, total_profit, total_harga = greedyKnapsack(componentsbyWeight, max_budget)
print("Barang yang dipilih:")
for component in taken:
    print("- ", component[0])
print("Total Harga:", total_harga)
print("Total profit:", total_profit)
print(" ")

print("========== GREEDY BY PROFIT ==========")
taken, total_profit, total_harga = greedyKnapsack(componentsbyProfit, max_budget)
print("Barang yang dipilih:")
for component in taken:
    print("- ", component[0])
print("Total Harga:", total_harga)
print("Total profit:", total_profit)
print(" ")

print("========== GREEDY BY DENSITY ==========")
taken, total_profit, total_harga = greedyKnapsack(componentsbyDensity, max_budget)
print("Barang yang dipilih:")
for component in taken:
    print("- ", component[0])
print("Total Harga:", total_harga)
print("Total profit:", total_profit)
print("======================================")
