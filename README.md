# Dreamscape Corner
Dreamscape Corner adalah E-Commerce yang menyediakan produk merchandise dari Honkai: Star Rail. E-Commerce ini terinspirasi dari Honkai Shop yang juga menjual merchandise game yang sama. Nama "Dreamscape Corner" di ambil dari nama toko di dalam game bernama "Dreamscape Sales Store" yang terletak di Penacony.

Dreamscape Corner dijalankan menggunakan Pacil Web Service (PWS) yang dapat diakses diakses melalui [link berikut.](http://stefanus-tan-dreamscapecorner.pbp.cs.ui.ac.id/ "Dreamscape Corner")

Dibuat oleh,<br>
**Nama:** Stefanus Tan Jaya<br>
**NPM:** 2306152456<br>
**Kelas:** PBP D<br>
<br>
<br>
# Tugas
## Tugas Individu 2
### a. Proses Pembuatan Proyek Django
1. Membuat direktori baru bernama `dreamscape-corner` dan inisiasi repositori lokal di direktori tersebut dengan *command prompt* atau Visual Studio Code.
2. Membuat repositori di Github dan hubungkan dengan repositori lokal `dreamscape-corner`.
3. Membuat *virtual environment* baru dan aktifkan env tersebut.
4. Membuat *file* baru bernama `requirements.txt` yang berisi
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    dan *install requirements* tersebut.
5. Membuat proyek Django dengan
    ```
    django-admin startproject dreamscape_corner .
    ```
6. Melakukan penyesuaian di `settings.py` dalam direktori `dreamscape_corner` bersamaan dengan pembuatan file `.gitignore` dan *deployment* proyek Django ke Pacil Web Service (PWS).
7. Membuat aplikasi `main` dengan
    ```
    python manage.py startapp main
    ```
    lalu daftar `main` pada variabel `INSTALLED_APPS` di `settings.py` dalam direktori `dreamscape_corner`.
8. Membuat model `Product` di  `models.py` dalam direktori `main` dengan atribut
    ```
    name: CharField,
    price: IntegerField,
    description: TextField,
    category: CharField,
    ```
9. Membuat dan menjalankan migrasi model untuk menerapkannya ke dalam basis data lokal.
10. Membuat fungsi *view* `show_main` dalam `views.py` untuk menampilkan HTML bernama `main.html` yang telah dibuat di dalam direktori `templates` pada direktori `main`. 
11. Di dalam `main.html`, nantinya akan ditampilkan nama aplikasi, data dari `show_main`. serta identitas pembuat.
12. Membuat *file* `urls.py` di dalam direktori `main` untuk *routing* URL aplikasi `main`.
13. Melakukan penyesuaian di `urls.py` pada direktori `dreamscape_corner` untuk *routing* URL proyek.
14. Melakukan *push* kode ke GitHub dan menunggu PWS selesai *build* proyek.

### b. Bagan Request Client ke Django


### c. Fungsi `git` pada Pengembangan Proyek Lunak
1. Riwayat Perubahan Lengkap<br>

2. *Branching* dan *Merging*
3. *Open Source* dan Fleksibilitas

### d. Mengapa Django menjadi pondasi dasar pengembangan perangkat lunak?
### e. Mengapa model pada Django disebut sebagai ORM?