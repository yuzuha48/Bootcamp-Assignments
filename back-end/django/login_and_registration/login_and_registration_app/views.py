import bcrypt, datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import User, Message, Comment

def index(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return render(request, 'index.html')

def register(request):
    if 'first_name' in request.session:
        del request.session['first_name']
    if 'last_name' in request.session:
        del request.session['last_name']
    if 'email' in request.session:
        del request.session['email']
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        return redirect('/')
    else:
        password = request.POST['password']
        pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw)
        request.session['user_id'] = user.id
        return redirect('/wall')
    
def login(request):
    if 'login_email' in request.session:
        del request.session['login_email']
    user = User.objects.filter(email = request.POST['login_email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/wall')
        else: 
            errors = {'login': 'Email and/or password is incorrect.'}
    else:
        errors = {'login': 'Email and/or password is incorrect.'}
    
    messages.error(request, errors['login'], extra_tags='login')
    request.session['login_email'] = request.POST['login_email']
    return redirect('/')
    
def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'posts': Message.objects.all()
    }
    return render(request, 'wall.html', context)

def post_message(request):
    if 'message' in request.session:
        del request.session['message']
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Message.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='post_tag')
        request.session['message'] = request.POST['message']
        return redirect('/wall')
    else:
        Message.objects.create(message=request.POST['message'], user_id=request.session['user_id'])
        return redirect('/wall')
    
def comment(request, message_id):
    if 'comment' in request.session:
        del request.session['comment']
    if 'user_id' not in request.session:
        return redirect('/')
    Comment.objects.create(comment=request.POST['comment'], message_id=message_id, user_id=request.session['user_id'])
    return redirect('/wall')

def delete(request, message_id):
    message = Message.objects.get(id=message_id)

    message_created = message.created_at
    message_date = message_created.strftime("%Y-%m-%d")
    my_timezone = timezone.get_default_timezone()
    message_time = message_created.astimezone(my_timezone)
    message_time = message_time.strftime("%H:%M:%S")
    message_time_str = message_time.split(":")

    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    time_str = time.split(":")

    if message_date == date:
        if message_time_str[0] == time_str[0] and int(time_str[1]) <= int(message_time_str[1]) + 30: 
            message.delete()
        elif int(message_time_str[0]) + 1 == int(time_str[0]) and int(time_str[1]) + 60 - int(message_time_str[1]) <= int(message_time_str[1]):
            message.delete()
    return redirect('/wall')
    

