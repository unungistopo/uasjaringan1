# Tugas Mandiri - Load Balancing dalam Komputasi Jaringan

## Deskripsi Repositori

Repositori ini merupakan tugas mandiri dalam mata kuliah **Komputasi Jaringan**, dengan fokus pada implementasi sederhana dari konsep load balancing menggunakan Python socket programming. Proyek ini bertujuan untuk memahami dan menerapkan teknik load balancing dalam mendistribusikan request client ke beberapa server worker melalui server broker.

### Struktur Repositori

- `codes/`
  - Berisi script utama untuk menjalankan simulasi load balancing.
- `documentation/`
  - Menyimpan file dokumentasi, termasuk panduan pengguna, diagram, dan flowchart.

---

### Deskripsi Singkat

Repositori ini ditujukan untuk mata kuliah **Komputasi Jaringan**. Proyek ini mensimulasikan load balancing sederhana yang dapat mendistribusikan request secara merata dan berurutan ke beberapa worker server menggunakan pendekatan counter dan round-robin. Proyek ini akan menyelesaikan masalah distribusi beban kerja pada server sehingga setiap server worker dapat menangani jumlah request yang merata dan berimbang.

---

## Alur Input-Process-Output

```plaintext
          +----------+         +---------+        +-----------+
Client -->|  Broker  | ----> (Load-Balancing) --> |  Worker   |
 Request  |  Server  |         |   Logic |        | Servers   |
          +----------+         +---------+        +-----------+
                 Input             Process              Output
