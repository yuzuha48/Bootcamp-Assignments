from django.shortcuts import render, redirect

def index(request):
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1
    if 'count' not in request.session:
        request.session['count'] = 1
    return render(request, "index.html")

def destroy(request):
    del request.session['count']
    return redirect("/")

def double(request):
    request.session['count'] += 2
    return redirect("/")

def add_num(request):
    num = request.POST["num"]
    request.session['count'] += int(num)
    return redirect("/")
