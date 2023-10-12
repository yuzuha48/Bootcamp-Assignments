from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import Book, Review
from dojo_reads_app.models import User

def view_all(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_reviews': Review.objects.all(),
        'all_books': Book.objects.all()
    }

    return render(request, 'view_all.html', context)


def add(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    return render(request, 'add.html')


def create(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    errors = Book.objects.basic_validator(request.POST)
    review_errors = Review.objects.basic_validator(request.POST)
    errors.update(review_errors)

    if len(errors) > 0:
        return JsonResponse({'success': False, 'error_messages': errors})
    else:
        book = Book.objects.create(title=request.POST['title'], author=request.POST['author'])
        Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], user_id=request.session['user_id'], book_id=book.id)
        return JsonResponse({'success': True, 'book_id': book.id})


def create_review(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    errors = Review.objects.basic_validator(request.POST)
    book_id = request.POST['book_id']

    if len(errors) > 0:
        return JsonResponse({'success': False, 'error_messages': errors})
    else:
        review = Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], user_id=request.session['user_id'], book_id=book_id)

    created_at = review.created_at 
    my_timezone = timezone.get_default_timezone()
    review_date = created_at.astimezone(my_timezone)
    review_date = review_date.strftime('%B %-d, %Y')

    return JsonResponse({'success': True, 'book_id': review.book.id, 'user_id': request.session['user_id'], 'user': review.user.alias, 'review_id': review.id, 'review': review.review, 'rating': review.rating, 'created_at': review_date})
    

def view(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    book = Book.objects.get(id=book_id)

    context = {
        'book': book, 
        'reviews': book.reviews.all()
    }

    return render(request, 'view.html', context)


def delete(request, review_id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    review = Review.objects.get(id=review_id)
    review.delete()
    return JsonResponse({'success': True})

