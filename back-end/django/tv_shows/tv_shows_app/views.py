from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from .models import Show

def all(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'all.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):    
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        return JsonResponse({'success': False, 'error_message': errors})
    else:
        show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], date=request.POST['date'], desc=request.POST['desc'])
        return JsonResponse({'success': True, 'show_id': show.id})

def view(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'view.html', context)

def edit(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        return JsonResponse({'success': False, 'error_message': errors})
    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.date = request.POST['date']
        show.desc = request.POST['desc']
        show.save()
        return JsonResponse({'success': True})

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')
