*HARI PERTAMA :
buat folder

install python environment
pyhton -m venv Env

aktivasi environment
Env\Scripts\activate.buat

membuat project
django-admin startproject namaProject

buat apps
python manage.py startapp namaApps

jalankan server
pyhton manage.py runserver

*sampai buat lokal urls di apps

*HARI KEDUA :
Menambah templates dalam apps
- masuk ke settings.py
- tambah pada installed apps 'namaapps'
- pastikan apps_dirs nya = True
- buat templates folder dalam apps

Templates Variable
- membuat variable dict yang bisa di buat dengan banyak index.html
- membuat navigasi dengan for loop dalam index.html

- membuat static img (bisa pakai variable)
- tambah Scripts di bawah dalam settings.py : 
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
- menambah {% load static%} pada atas index.html

*HARI KETIGA :
- menambah css
- menambah bootsrap dan javascript

*sama seperti static image, hanya di bagian src nya saja

*HARI KEEMPAT :
- membuat model pada apps
- menampilkan model pada views (menampilkan database)
- mengatur bahasa sql pada setting.py dengan bahasa databse yg akan di gunakan
- buat class pada models.py untuk di koneksikan dengan data base
- mengatur admin script pada admin.py
from .models import namaClassDB
admin.site.register(namaClassDB);
- membuat superuser agar bisa login ke /admin
pada cmd ketik :
python manage.py createsuperuser

- menambah variable db pada views def index()
views_post = Post.objects.all()
lalu masukan ke context
- masukan variable pada index.html dengan loop
- meloop dari belakang dengan menambah reversed setelah Post
- membuat persiapan imigrasi :
python manage.py makemigrations

- mengimigrasi dari pyhton ke database :
python manage.py migrate

- lalu jalankan server

*HARI KELIMA :
- belajar Models Field :
    CharField(max_length=jumlahHuruf) --> varchar pada databsae
    option :
        - max_length=jumlahHuruf (wajib)
        - null=True/False (defaul itu False), field tidak boleh kosong
        - blank=True/False (defaul itu False), field pada validasi tidak boleh kosong
        - default='isidefault'
    TextField()
    DateTimeField(auto_now_add=True)
    EmailField()

- Object Relational Mapping dengan shelll :
python manage.py shell'
    from contact.models import Data
    Data.objects.create(id="value") --> membuat data
    Data.objects.all()[index] --> membaca data
    Data.objects.all()[index].delete() --> menghapus data
    Data.objects.all()[index].id = "value" --> mengubah data
    Data.objects.all()[index].save() --> jangan lupa save setelah di ubah

- Querysets dengan shell :
    - Data.objects.all()[index] tidak di sarankan
    - Data.objects.get(id=index) lebih baik dengan primary key yaitu id dan hanya satu data
    - Data.objects.filter(category="berita") untuk menampilkan banyak data
    - Data.objects.exclude(category="gosip") untuk menampilkan data kecuali gosip
    - Data.objects.get(judul__iexact="hallo world!") menampilkan data tidak casesensitif
    - Data.objects.order_by(judul) untuk menampilkan sesuai abjad jika ingin reverse maka tambah - depan judul
    - Data.objects.all().values('id')

bisa di lihat di web django querysets