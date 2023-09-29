from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Desc, Comment

def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    if 'name' in request.session:
        del request.session['name']
    if 'desc' in request.session:
        del request.session['desc']
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        request.session['name'] = request.POST['name']
        request.session['desc'] = request.POST['desc']
        return redirect('/')
    else:
        course = Course.objects.create(name=request.POST['name'])
        course_id = course.id
        Desc.objects.create(desc=request.POST['desc'], course_id=course_id)
        return redirect('/')
    
def view_comments(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'comments.html', context)

def add_comment(request, course_id):
    if 'comment' in request.session:
        del request.session['comment']
    errors = Comment.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        request.session['comment'] = request.POST['comment']
        return redirect(f'/courses/view_comments/{course_id}')
    else:
        Comment.objects.create(comment=request.POST['comment'], course_id=course_id)
        return redirect(f'/courses/view_comments/{course_id}')
    
def delete(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'delete.html', context)

def destroy(request, course_id):
    answer = request.POST['answer']
    if answer == "No":
        return redirect('/')
    if answer == "Yes! I want to delete this":
        course = Course.objects.get(id=course_id)
        course.delete()
        return redirect('/')
    
