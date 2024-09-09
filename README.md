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
    Sistem kontrol `git` dapat melacak setiap perubahan yang dilakukan pada setiap *file* seiring waktu, termasuk mencatat siapa yang membuat perubahan, kapan perubahan itu dilakukan, dan mengapa. Hal ini mencakup membuat dan menghapus file, serta mengedit kontennya. Dengan riwayat lengkap ini memungkinkan developer untuk kembali ke versi *file* sebelumnya, yang berguna untuk menemukan penyebab *bug*.

    <br>
2. *Branching* dan *Merging*<br>
    Dalam sistem kontrol `git`, tim developer dapat mengerjakan berbagai bagian proyek secara bersamaan. Meskipun dalam komputer sendiri-sendiri, developer dapat mengerjakan bagian yang berbeda secara terpisah dengan cara membuat *branch*. Nantinya, developer dapat menggabungkan kembali bagian-bagian yang terpisah ini dengan fitur *merge*. Hal ini membantu memastikan bahwa perubahan yang dilakukan di setiap bagian tidak bertentangan satu sama lain.

    <br>
3. *Open Source* dan Fleksibilitas<br>
    Sistem kontrol `git` dapat digunakan secara terbuka oleh siapa pun yang ingin mengembangkan proyeknya. Selain itu, `git` menjadi layanan *hosting* yang komprehensif dengan *platform* yang fleksibel, seperti Gitlab, GitHub, Bitbucket, dan SourceForge. *Platform* tersebut dapat digunakan sebagai solusi untuk *hosting* berbagai proyek.

### d. Mengapa Django menjadi pondasi dasar pengembangan perangkat lunak?
1. *Simple*<br>
    *Framework* Django telah dibuat untuk mudah digunakan dan mempercepat proses implementasi *software*. Django menyediakan *tools*, *components*, dan *liraries* yang membantu dalam pengembangan perangkat lunak yang sederhana.

    <br>
2. Komunitas<br>
    Komunitas Django dipenuhi developer-developer informatif yang mendukung pengembangan *framework* ini. Mereka seringkali berbagi pengalaman, *best practices*, dan tutorial yang dapat membantu developer baru untuk belajar, mengembangkan *skill*, dan membangun aplikasi yang lebih baik.

    <br>
3. Keamanan<br>
    Django menyediakan fitur yang dapat melindungi developer baru yang masih awam terhadap ancaman siber. Django dapat mengatasi serangan maupun ancaman web, seperti Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), and SQL Injection.

    <br>
4. Dukungan Autentikasi<br>
    Django menyediakan fitur autentikasi dan autorisasi yang mendukung pembangunan perangkat lunak yang aman. Fitur ini termasuk kata sandi, pengaturan akses *user*, dan mendukung autentikasi dari pihak ketiga, seperti Google Sign-In.

    <br>
5. Performa<br>
    Django memiliki kinerja performa yang bagus, sehingga cocok untuk *software* yang membutuhkan respon cepat. *Framework* ini memiliki struktur kode yang optimal dan fitur *caching* untuk mendukung performa.
### e. Mengapa model pada Django disebut sebagai ORM?
Model Django yang ORM (Object-Relational Mapper) memungkinkan deveoper untuk berinteraksi dengan *database*. ORM Django berfungsi untuk membuat SQL secara *pythonic* dengan mengambil dan memanipulasi data dari *database* developer. Kemudian, didapatkan hasil dengan gaya pemrograman Python yang mudah dipahami. Alhasil, kita tidak perlu menulis *query* SQL lagi jika ingin berinteraksi dengan database yang dikelola Django.