from django.shortcuts import render, redirect
from dojo_reads_app.models import User
from books_app.models import Book, Review

def user(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')

    books = {}
    review_count = 0
    all_reviews = Review.objects.all()

    for review in all_reviews:
        if review.user.id == user_id:
            books[review.book.title] = review.book.id
            review_count += 1 

    context = {
        'user': User.objects.get(id=user_id),
        "all_books": books,
        "num_of_reviews": review_count
    }

    return render(request, 'user.html', context)

