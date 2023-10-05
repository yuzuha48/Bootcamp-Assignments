from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = 'Course name should be more than 5 characters.'
        if len(postData['desc']) < 16:
            errors['desc'] = 'The description should be more than 15 characters.'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Desc(models.Model):
    desc = models.TextField()
    course = models.OneToOneField(Course, related_name="desc", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 6:
            errors['comment'] = 'Comment should be at least 5 characters.'
        return errors
    
class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()