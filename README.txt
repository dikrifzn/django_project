HARI PERTAMA :
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

HARI KEDUA :
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

HARI KETIGA :
- menambah css
- menambah bootsrap dan javascript

*sama seperti static image, hanya di bagian src nya saja

HARI KEEMPAT :
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
