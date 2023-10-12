from django.db import models
from dojo_reads_app.models import User

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Title should be at least 2 characters.'
        if len(postData['author']) < 2:
            errors['author'] = "Author's name should be at least 2 characters."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class ReviewManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['review']) < 15:
            errors['review'] = 'Review should be at least 15 characters.'
        if not postData['rating']:
            errors['rating'] = 'Please select a rating.'
        return errors

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()