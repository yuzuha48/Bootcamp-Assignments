from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def create_user(request):
    name = request.POST['name']
    location = request.POST["location"]

    if request.POST.get('language1'):
        language1 = request.POST['language1']
    else:
        language1 = None

    if request.POST.get('language2'):
        language2 = request.POST['language2']
    else:
        language2 = None

    if request.POST.get('language3'):
        language3 = request.POST['language3']
    else:
        language3 = None

    language = {
        "language1": language1,
        "language2": language2,
        "language3": language3,
    }
    comment = request.POST["comment"]
    context = {
        "name": name, 
        "location": location,
        "language": language, 
        "comment": comment
    }
    return render(request, "show.html", {'data': context})

# def success(request):
#     return render(request, "success.html")

# def some_function(request):
#     request.session['name'] = request.POST['name']
#     request.session['counter'] = 100