# Direktori `codes/`

Direktori ini berisi file-file script utama yang diperlukan untuk menjalankan simulasi load balancing sederhana. Berikut adalah deskripsi dari setiap file yang ada di dalam direktori ini:

---

## File Deskripsi

### `client.py`

- **Fungsi**: Script ini digunakan untuk mengirim request ke Broker Server.
- **Cara Kerja**: 
  - Client mengirim request dengan format **"Application ID : Message"** ke Broker Server.
  - Broker Server kemudian akan menentukan worker server mana yang akan menerima request tersebut berdasarkan metode load balancing yang telah ditentukan.
- **Aplikasi ID**: 
  - `Long`: Mensimulasikan perhitungan kompleks.
  - `Short`: Mensimulasikan perhitungan sederhana seperti echo.
  
---

### `broker_server.py`

- **Fungsi**: Script utama untuk Broker Server. Broker bertanggung jawab untuk menerima request dari Client dan mendistribusikannya ke Worker Servers.
- **Metode Load Balancing**:
  - **Pemerataan**: Broker memilih Worker Server yang memiliki jumlah request paling sedikit untuk mendistribusikan beban kerja secara merata.
  - **Berurutan**: Broker memilih Worker Server secara berurutan berdasarkan ID Worker menggunakan counter, sehingga setiap server menangani jumlah request yang seimbang.
- **Cara Kerja**:
  - Setelah menerima request dari Client, Broker akan menggunakan salah satu metode load balancing di atas untuk menentukan Worker Server yang akan menangani request tersebut.
  - Broker kemudian meneruskan request ke Worker Server yang dipilih.

---

### `worker_server.py`

- **Fungsi**: Script ini menjalankan Worker Server yang bertugas menerima request dari Broker dan memprosesnya.
- **Jenis Aplikasi**:
  - **Long**: Mensimulasikan perhitungan yang kompleks dan memerlukan waktu proses yang lebih lama.
  - **Short**: Mensimulasikan tugas sederhana seperti echo atau perhitungan ringan.
- **Cara Kerja**:
  - Worker Server menerima request dari Broker Server dan memproses request tersebut sesuai dengan jenis aplikasi yang diminta oleh Client.
  - Hasil dari proses ini kemudian ditampilkan atau dikirimkan kembali sesuai skenario yang diinginkan.

---

Setiap script dalam direktori `codes/` memiliki peran yang berbeda namun saling terhubung untuk membentuk sistem load balancing sederhana, di mana **Client** mengirim request ke **Broker Server** yang kemudian mendistribusikan beban kerja ke **Worker Servers** secara efisien.

