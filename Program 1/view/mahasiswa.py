from input_form import InputForm

class MahasiswaView:
    def __init__(self):
        self.data_mahasiswa: list[Mahasiswa] = []

    def tambah_data(self) -> None:
        nim, nama = InputForm.input_data()  # Removed jurusan
        mahasiswa = Mahasiswa(nim, nama)  # Removed jurusan
        self.data_mahasiswa.append(mahasiswa)
        print("Data berhasil ditambahkan.")

    def tampilkan_data(self) -> None:
        if not self.data_mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            for idx, mahasiswa in enumerate(self.data_mahasiswa, start=1):
                print(f"{idx}. {mahasiswa}")

    def hapus_data(self) -> None:
        self.tampilkan_data()
        try:
            idx = int(input("Pilih nomor data yang akan dihapus: ")) - 1
            if 0 <= idx < len(self.data_mahasiswa):
                del self.data_mahasiswa[idx]
                print("Data berhasil dihapus.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

    def ubah_data(self) -> None:
        self.tampilkan_data()
        try:
            idx = int(input("Pilih nomor data yang akan diubah: ")) - 1
            if 0 <= idx < len(self.data_mahasiswa):
                nim, nama = InputForm.input_data()  # Removed jurusan
                self.data_mahasiswa[idx].nim = nim
                self.data_mahasiswa[idx].nama = nama
                print("Data berhasil diubah.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")