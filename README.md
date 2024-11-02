# Tugas Mandiri - Load Balancing dalam Komputasi Jaringan

## Deskripsi Repositori

> Repositori ini merupakan tugas mandiri dalam mata kuliah **Komputasi Jaringan**, dengan fokus pada implementasi sederhana dari konsep load balancing menggunakan Python socket programming. Proyek ini bertujuan untuk memahami dan menerapkan teknik load balancing dalam mendistribusikan request client ke beberapa server worker melalui server broker.

> Alur Input-Process-Output

```plaintext
          +----------+         +---------+        +-----------+
Client -->|  Broker  | ----> (Load-Balancing) --> |  Worker   |
 Request  |  Server  |         |   Logic |        | Servers   |
          +----------+         +---------+        +-----------+
                 Input             Process              Output
```
## Direktori `codes/`:
> Berisi script utama untuk menjalankan simulasi load balancing.
1. `client.py` - *Script ini digunakan untuk mengirim request ke Broker Server*
2. `broker_server.py` - *Script utama untuk Broker Server. Broker bertanggung jawab untuk menerima request dari Client dan mendistribusikannya ke Worker Servers.*
3. `worker.py` - *Script ini menjalankan Worker Server yang bertugas menerima request dari Broker dan memprosesnya.*

## Direktori `documentation/`:
> Menyimpan file dokumentasi, termasuk panduan pengguna, diagram, dan flowchart.
1. `panduan.pdf` - *File dokumentasi ini memuat panduan pengguna, diagram dan flowchart*
---

# Informasi anggota kelompok*
> Tugas ini adalah tugas mandiri, dikerjakan sendiri tanpa kelompok

Nama mahasiswa: Unung Istopo Hartanto
NIM: 24051905001
