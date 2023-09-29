from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse 
# from django.views.decorators.csrf import csrf_exempt
from .models import Show

def all(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'all.html', context)

def new(request):
    return render(request, 'new.html')

# @csrf_exempt
def create(request):
    # title = request.POST.get('title')
    # if Show.objects.filter(title=title).exists():
    #     return JsonResponse({'error': 'Title already exists'}, status=400)
    
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], date=request.POST['date'], desc=request.POST['desc'])
        return redirect(f'/shows/{show.id}')
        # return JsonResponse({'message': 'Show created successfully'}, status=201)

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

# @csrf_exempt
def update(request, show_id):
    # title = request.POST.get('title')
    # show = Show.objects.filter(title=title).exclude(id=show_id).first()
    # if show:
    #     return JsonResponse({'error': 'Title already exists'}, status=400)
    
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else: 
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.date = request.POST['date']
        show.desc = request.POST['desc']
        show.save()
        # messages.success(request, "Show successfully updated")
        return redirect(f'/shows/{show_id}')
        # return JsonResponse({'message': 'Show updated successfully'})

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')
