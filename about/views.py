from django.shortcuts import render

# Create your views here.
def index(request):
    contex = {
        'judul' : 'Website Django',
        'penulis' : 'Dikri Fauzan Amrulloh',
        'nav' : [
            ['/', 'HOME'],
            ['/about', 'ABOUT'],
            ['/contact', 'CONTACT'],
        ]
    }
    return render(request, 'about/index.html', contex)