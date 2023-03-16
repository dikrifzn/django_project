from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'Website Django',
        'penulis' : 'Dikri Fauzan Amrulloh',
        'nav' : [
            ['/', 'HOME'],
            ['/about', 'ABOUT'],
            ['/contact', 'CONTACT'],
        ]
    }
    return render(request, 'index.html', context)