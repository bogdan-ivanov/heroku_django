from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def authors(request):
    authors = User.objects.all()
    return render(request, 'authors.html', {'authors': authors})