from django.shortcuts import render
from .models import Post


def profilehome(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'profilehome.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})