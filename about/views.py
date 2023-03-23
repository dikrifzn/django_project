from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    views_post = Post.objects.all()
    print(views_post)
    context = {
        'judul' : 'Website Django',
        'penulis' : 'Dikri Fauzan Amrulloh',
        'Posts':views_post,
        'nav' : [
            ['/', 'HOME'],
            ['/about', 'ABOUT'],
            ['/contact', 'CONTACT'],
        ]
    }
    return render(request, 'about/index.html', context)