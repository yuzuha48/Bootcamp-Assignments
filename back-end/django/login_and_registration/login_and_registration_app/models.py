from django.db import models
import re 

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address.'
        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = 'Passwords do not match.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters.'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class MessageManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['message']) < 15:
            errors['message'] = 'Message should be at least 15 characters.'
        return errors 
    
class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager() 
    
class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
