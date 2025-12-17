# 1.
nama = input("Masukkan nama Anda: ") 
umur_str = input("Masukkan umur Anda: ")
nim= input("masukkan nim anda: ")
prodi = input("prodi apa kamu: ")
warna= input("warna favoritmu: ")

# 2. Proses (Mengolah data

umur = int(umur_str)
tahun_lahir = 2025 - umur # Contoh proses: menghitung tahun lahir
pesan = f"Halo, {nama}! prodi {prodi} dengan nim {nim} yang mempunyai warna favorit {warna} Anda lahir sekitar tahun {tahun_lahir}." # Menggabungkan teks dan variabel

# 3. Output (Menampilkan hasil ke pengguna)
print(pesan) # Menampilkan pesan yang sudah diproses
