from django.shortcuts import render

from .models import Data
# Create your views here.
def index(request):
    data = Data.objects.all()
    context = {
        'judul' : 'Website Django',
        'penulis' : 'Dikri Fauzan Amrulloh',
        'data' : data,
        'nav' : [
            ['/', 'HOME'],
            ['/about', 'ABOUT'],
            ['/contact', 'CONTACT'],
        ]
    }
    return render(request, 'contact/index.html', context)