buku = []

print("Perpustakaan Digital")
print("--------------------")

while True:
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Hapus Buku")
    print("3. Cari Buku")
    print("4. Tampilkan Buku")
    print("5. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        judul = input("Judul: ")
        penulis = input("Penulis: ")
        tahun_terbit = input("Tahun Terbit: ")
        buku.append({"judul": judul, "penulis": penulis, "tahun_terbit": tahun_terbit})
        print("Buku berhasil ditambahkan.")

    elif pilihan == "2":
        judul = input("Judul buku untuk dihapus: ")
        for i, buku_item in enumerate(buku):
            if buku_item["judul"] == judul:
                konfirmasi = input("Apakah Anda yakin? (y/n): ")
                if konfirmasi.lower() == 'y':
                    del buku[i]
                    print("Buku berhasil dihapus.")
                break

    elif pilihan == "3":
        kata_kunci = input("Kata kunci: ")
        hasil = [buku_item for buku_item in buku if kata_kunci.lower() in buku_item["judul"].lower()]
        for buku_item in hasil:
            print(f"Judul: {buku_item['judul']}, Penulis: {buku_item['penulis']}, Tahun Terbit: {buku_item['tahun_terbit']}")

    elif pilihan == "4":
        for i, buku_item in enumerate(buku):
            print(f"{i+1}. Judul: {buku_item['judul']}, Penulis: {buku_item['penulis']}, Tahun Terbit: {buku_item['tahun_terbit']}")

    elif pilihan == "5":
        break

    else:
        print("Pilihan tidak valid.")