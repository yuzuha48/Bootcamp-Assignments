from django.shortcuts import render
import random

def index(request):
    if 'count' in request.session:
        del request.session['count']
    request.session['num'] = random.randint(1,100)
    print(request.session['num'])
    return render(request, 'index.html')

def guess(request):
    guess = int(request.POST['guess'])

    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    if request.session['count'] < 5:
        if guess == request.session['num']:
            result = "You win!"
        elif guess > request.session['num']:
            result = "Too high!"
        elif guess < request.session['num']:
            result = "Too low!"
    elif request.session['count'] == 5:
        if guess == request.session['num']:
            result = "You win!"
        if guess != request.session['num']:
            result = "You lose..."
    context = {
        "result": result,
        "count": request.session['count']
    }
    return render(request, "result.html", context)

def leaderboard(request):
    if 'names_and_attempts' not in request.session:
        request.session['names_and_attempts'] = [{"name": request.POST['name'], "attempts": request.session['count']}]
    else:
        request.session['names_and_attempts'].append({"name": request.POST['name'], "attempts": request.session['count']})
        request.session.save()

    context = {
        'names_and_attempts': request.session['names_and_attempts']
    }
    print(request.session['names_and_attempts'])
    return render(request, "leaderboard.html", context)
