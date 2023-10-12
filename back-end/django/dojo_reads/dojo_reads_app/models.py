import re
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['name']) < 2:
            errors['name'] = "Name should be at least 2 characters."
        if len(postData['alias']) < 2:
            errors['alias'] = "Alias should be at least 2 characters."

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address.'
        if User.objects.filter(email=postData['email']):
            errors['email_exists'] = "There's already an account with that email."

        if postData['password'] != postData['confirm_pw']:
            print(postData['password'], postData['confirm_pw'])
            errors['confirm_pw'] = 'Passwords do not match.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters.'

        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
        

