#Program Absenesi
import tkinter as tk 

def absen():
    nama = entry_nama.get()
    jam = int (entry_jam.get())

    #Menentukan Hari  
    if jam <= 08.00:
        ket = 'ABSEN ANDA BERHASIL, Kuliah akan dimulai pada pukul 08.00'
    elif jam >= 08.00:
        ket = 'Maaf absensi telah di tutup \nJadi tolong untuk tepat waktu!'
    else:
        ket = 'gagal'
    result_label.config(text=f"Mahasiswa dengan nama {nama} \n {ket}")


# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Kehadiran Siswa")

#label dan entry untuk memasukan nama
label_nama = tk.Label(root, text="Masukan Nama: ")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Label dan entry untuk memasukkan nim
label_nim = tk.Label(root, text="Masukkan NIM:")
label_nim.pack()
entry_nim = tk.Entry(root)
entry_nim.pack()

# Label dan entry untuk memasukkan matkul
label_mataKuliah = tk.Label(root, text="Mata Kuliah:")
label_mataKuliah.pack()
entry_mataKuliah = tk.Entry(root)
entry_mataKuliah.pack()

# Label dan entry untuk memasukkan hari
label_hari = tk.Label(root, text="Masukkan Hari:")
label_hari.pack()
entry_hari = tk.Entry(root)
entry_hari.pack()

# Label dan entry untuk memasukkan jam
label_jam = tk.Label(root, text="Jam Masuk: \n(Menggunakan 1 angka saja)")
label_jam .pack()
entry_jam  = tk.Entry(root)
entry_jam .pack()

# Tombol untuk menghitung grade
hitung_button = tk.Button(root, text="Absen", command=absen)
hitung_button.pack()

# Label untuk menampilkan hasil
result_label = tk.Label(root, text="")
result_label.pack()

# Menampilkan jendela
root.mainloop()