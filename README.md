# UAS - Komunikasi dan Koordinasi Jaringan

## Deskripsi Repositori

> Repositori ini merupakan UAS dalam mata kuliah **Komputasi Jaringan**, dengan fokus pada implementasi sederhana dari konsep komunikasi dan koordinasi jaringan menggunakan bahasa pemrograman Python, celery Worker, Redis broker dan Postman FastAPI.

> Use Case Diagram

![image](https://github.com/user-attachments/assets/d116fab3-9212-4094-aef4-4040640bbc6d)

## Direktori `codes/`:
> Berisi script utama untuk menjalankan simulasi load balancing.
1. `client.py` - *Script ini digunakan untuk mengirim request ke Broker Server*
2. `broker_server.py` - *Script utama untuk Broker Server. Broker bertanggung jawab untuk menerima request dari Client dan mendistribusikannya ke Worker Servers.*
3. `worker.py` - *Script ini menjalankan Worker Server yang bertugas menerima request dari Broker dan memprosesnya.*

## Direktori `documentation/`:
> Menyimpan file dokumentasi, termasuk panduan pengguna, diagram, dan flowchart.
1. `panduan.pdf` - *File dokumentasi ini memuat panduan pengguna, diagram dan flowchart*
---

## Informasi anggota kelompok
> Nama Mahasiswa - NIM
- Unung Istopo Hartanto - 24051905001
- Suwarno Arieska - 24051905003
