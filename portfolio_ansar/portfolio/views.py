from django.shortcuts import render
from .models import Book, Post

def index(request):
    return render(request, 'about_me.html')

def skills(request):
    return render(request, 'skills.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, 'books.html', context)

def posts(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'posts.html', context)
