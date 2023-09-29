from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = 'Title should be at least 2 characters.'
        if Show.objects.filter(title=postData['title']):
            errors['title_exists'] = "There's already a show with that title."
        if len(postData['network']) < 4:
            errors['network'] = 'Network should be at least 3 characters.'
        input_date = datetime.strptime(postData['date'], "%Y-%m-%d")
        if not postData['date'] or input_date.date() > datetime.now().date():
            errors['date'] = 'Please enter a valid date.'
        if len(postData['desc']) > 0 and len(postData['desc']) < 11:
            errors['desc'] = 'Description should be at least 10 characters.'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255, unique=True)
    network = models.CharField(max_length=255)
    date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()