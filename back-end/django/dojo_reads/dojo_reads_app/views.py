import bcrypt
from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def welcome(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return render(request, 'welcome.html')


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        return JsonResponse({'success': False, 'error_messages': errors})
    else:  
        password = request.POST['password']
        pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=pw)
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

