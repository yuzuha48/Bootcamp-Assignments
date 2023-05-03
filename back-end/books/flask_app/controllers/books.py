from flask_app import app 
from flask import render_template, redirect, request, session
from flask_app.models.author import Author 
from flask_app.models.book import Book

@app.route('/')
def home():
    return redirect('/authors')

@app.route('/authors', methods=['POST'])
def create_author():
    Author.save(request.form)
    return redirect('/authors')

@app.route('/authors')
def get_all_authors():
    all_authors = Author.get_all()
    return render_template('authors.html', all_authors=all_authors)

@app.route('/books', methods=['POST'])
def create_book():
    Book.save(request.form)
    return redirect('/books')

@app.route('/books')
def get_all_books():
    all_books = Book.get_all()
    return render_template('books.html', all_books=all_books)

@app.route('/authors/<int:author_id>')
def view_author_favorites(author_id):
    unfavorited_books = Book.get_unfavorited_books(author_id)
    author = Author.get_favorite_books(author_id)
    author_favorites = author.favorite_books
    return render_template('author_show.html', author_favorites=author_favorites, author=author, unfavorited_books=unfavorited_books)

@app.route('/add_book/<int:author_id>', methods=['POST'])
def add_book_to_favorites(author_id):
    book_id = request.form["book"]
    Author.add_to_favorites(author_id, book_id)
    return redirect(f'/authors/{author_id}')

@app.route('/books/<int:book_id>')
def view_who_favorited_book(book_id):
    unfavorited_authors = Author.get_unfavorited_authors(book_id)
    book = Book.get_favorited_by(book_id)
    return render_template("book_show.html", favorited_by=book.authors, book=book, unfavorited_authors=unfavorited_authors)

@app.route('/add_author/<int:book_id>', methods=['POST'])
def add_author_to_favorited_by(book_id):
    author_id = request.form["author"]
    Book.add_author(book_id, author_id)
    return redirect(f'/books/{book_id}')