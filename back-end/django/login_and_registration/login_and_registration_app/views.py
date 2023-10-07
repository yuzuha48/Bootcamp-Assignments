import bcrypt, datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .models import User, Message, Comment

def index(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return render(request, 'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        return JsonResponse({'success': False, 'error_messages': errors})
    else:  
        password = request.POST['password']
        pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw)
        request.session['user_id'] = user.id
        return JsonResponse({'success': True})
    
def login(request):
    user = User.objects.filter(email = request.POST['login_email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return JsonResponse({'success': True})
        else: 
            errors = {'login': 'Email and/or password is incorrect.'}
            return JsonResponse({'success': False, 'error_messages': errors})
    else:
        errors = {'login': 'Email and/or password is incorrect.'}
        return JsonResponse({'success': False, 'error_messages': errors})
    
def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'posts': Message.objects.all()
    }
    return render(request, 'wall.html', context)

def post_message(request):
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Message.objects.basic_validator(request.POST)
    if len(errors) > 0:
        return JsonResponse({'success': False, 'error_messages': errors})
    else:
        Message.objects.create(message=request.POST['message'], user_id=request.session['user_id'])
        return JsonResponse({'success': True})
    
def comment(request, message_id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    comment = Comment.objects.create(comment=request.POST['comment'], message_id=message_id, user_id=request.session['user_id'])

    return JsonResponse({'success': True, 'id': comment.id, 'first_name': comment.user.first_name, 'last_name': comment.user.last_name, 'created_at': comment.created_at, 'comment': comment.comment})

def delete(request, message_id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    message = Message.objects.get(id=message_id)

    message_created = message.created_at
    my_timezone = timezone.get_default_timezone()
    message_date_time = message_created.astimezone(my_timezone)
    message_date_time = message_date_time.strftime("%Y-%m-%d %H:%M:%S")

    message_date_time_str = message_date_time.split(" ")
    message_date = message_date_time_str[0]
    message_time_str = message_date_time_str[1].split(":")

    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    time_str = time.split(":")

    if message_date == date:
        if message_time_str[0] == time_str[0] and int(time_str[1]) <= int(message_time_str[1]) + 30: 
            message.delete()
            return JsonResponse({'success': True})
        elif int(message_time_str[0]) + 1 == int(time_str[0]) and int(time_str[1]) + 60 - int(message_time_str[1]) <= int(message_time_str[1]):
            message.delete()
            return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error_messages': {'delete': "Can't delete messages posted over 30 minutes ago."}})
    

def delete_comment(request, comment_id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({'success': True})