#Fungsi untuk menghitung UpperBound dengan rumus upperbound
def bound(level, value, weight, components, budget):
    if weight >= budget:
        return 0
    n = len(components)
    bound = value
    total_weight = weight

    while level < n and total_weight + components[level][1] <= budget:
        bound += components[level][2]
        total_weight += components[level][1]
        level += 1

    if level < n:
        bound += (budget - total_weight) * (components[level][2] / components[level][1])

    return bound


def knapsack_bnb_best_first(components, budget):
    # Urutkan komponen berdasarkan density secara descending
    components.sort(key=lambda x: x[2]/x[1], reverse=True)
    n = len(components)

    root = (-1, 0, 0, 0, [])  # Representasi root node
    queue = [root]  # Antrian simpul yang akan dieksplorasi
    max_value = 0  # Nilai maksimum yang ditemukan
    selected = []  # Komponen yang dipilih

    while queue:
        level, value, weight, bound_value, taken = queue.pop(0)

        # Cek bound untuk menentukan apakah simpul harus dieksploras
        if bound(level, value, weight, components, budget) > max_value:
            if level == n - 1:  # Jika sudah mencapai level terakhir
                if value > max_value:
                    max_value = value
                    selected = taken
            else:
                
                # Buat simpul anak kiri yang tidak menyertakan komponen saat ini
                left_child = (level + 1, value, weight, 0, taken[:])
                queue.append(left_child)

                # Buat simpul anak kanan yang menyertakan komponen saat ini
                right_child = (level + 1, value + components[level+1][2], weight + components[level+1][1],
                               bound(level + 1, value + components[level+1][2], weight + components[level+1][1],
                                     components, budget), taken[:] + [components[level+1]])
                queue.append(right_child)

    return selected


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

budget = 500
selected = knapsack_bnb_best_first(components, budget)


print("Knapsack Branch and Bound Best First Search")
print("")

TotalHarga = 0
TotalProfit = 0
print("Barang Terpilih : ")
for name, price, performance in selected:
    print(f"{name}, Harga: ${price}, Kinerja: {performance}")
    TotalProfit += performance
    TotalHarga += price

print("")
print("Total Harga:", TotalHarga)
print("Total profit:", TotalProfit)
