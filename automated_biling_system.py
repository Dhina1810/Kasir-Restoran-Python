harga_makanan = 400000
ambang_diskon = 500000
diskon = 0.10
pajak = 0.05

if harga_makanan > ambang_diskon:
    harga_setelah_diskon = harga_makanan - (harga_makanan * diskon)

else:
    harga_setelah_diskon = harga_makanan

# harga setelah diskon + pajak

total_harga = harga_setelah_diskon + (harga_setelah_diskon * pajak)
print(f"harga makanan: {harga_makanan}")
print(f"harga setelah diskon: {harga_setelah_diskon}")
print(f"total harga: {total_harga}")