from django.shortcuts import render, redirect
from .models import Author, Book

def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(request):
    Book.objects.create(title=request.POST["title"], desc=request.POST['desc'])
    return redirect('/')

def view_book(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id), 
        "all_authors": Author.objects.all()
    }
    return render(request, 'view.html', context)

def add_author_to_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author'])
    book.authors.add(author)
    return redirect(f'/view/{book_id}')

def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, 'authors.html', context)

def add_author(request):
    Author.objects.create(first_name=request.POST["first_name"], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')

def view_author(request, author_id):
    context = {
        "author": Author.objects.get(id=author_id), 
        "all_books": Book.objects.all()
    }
    return render(request, 'view_author.html', context)

def add_book_to_author(request, author_id):
    book = Book.objects.get(id=request.POST['book'])
    author = Author.objects.get(id=author_id)
    author.books.add(book)
    return redirect(f'/view_author/{author_id}')
