HARI PERTAMA :
buat folder

install python environment
pyhton -m venv Env

aktivasi environment
Env\Scripts\activate.buat

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