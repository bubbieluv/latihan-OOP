class Mahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self):
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        self.data.append({'nama': nama, 'nim': nim})
        print("Data mahasiswa berhasil ditambahkan.")

    def tampilkan_data(self):
        if not self.data:
            print("Tidak ada data mahasiswa.")
            return
        print("\nData Mahasiswa:")
        for index, mahasiswa in enumerate(self.data, start=1):
            print(f"{index}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}")

    def ubah_data(self):
        self.tampilkan_data()
        index = int(input("Pilih nomor mahasiswa yang ingin diubah: ")) - 1
        if 0 <= index < len(self.data):
            nama = input("Masukkan nama baru: ")
            nim = input("Masukkan NIM baru: ")
            self.data[index] = {'nama': nama, 'nim': nim}
            print("Data mahasiswa berhasil diubah.")
        else:
            print("Nomor tidak valid.")

    def hapus_data(self):
        self.tampilkan_data()
        index = int(input("Pilih nomor mahasiswa yang ingin dihapus: ")) - 1
        if 0 <= index < len(self.data):
            self.data.pop(index)
            print("Data mahasiswa berhasil dihapus.")
        else:
            print("Nomor tidak valid.")


def main():
    mahasiswa_manager = Mahasiswa()

    while True:
        print("\nMenu Utama:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            mahasiswa_manager.tambah_data()
        elif pilihan == "2":
            mahasiswa_manager.tampilkan_data()
        elif pilihan == "3":
            mahasiswa_manager.ubah_data()
        elif pilihan == "4":
            mahasiswa_manager.hapus_data()
        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()