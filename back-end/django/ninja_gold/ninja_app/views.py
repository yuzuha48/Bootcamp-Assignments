from django.shortcuts import render, redirect
import random, json
from datetime import datetime

def form(request):
    if 'total_moves' in request.session:
        del request.session['total_moves']
    if 'gold' in request.session:
        del request.session['gold']
    if 'activities' in request.session:
        del request.session['activities']
    return render(request, "form.html")

def index(request):
    if 'activities' in request.session:
        context = {
            "total_gold": request.session['gold'],
            'activities': request.session['activities']
        }
    else:
        context = {"total_gold": 0}

    if 'goal' in request.POST:
        request.session['goal'] = request.POST['goal']
    if 'moves' in request.POST:
        request.session['moves'] = request.POST['moves']

    return render(request, "index.html", context)

def process_money(request, location):
    if 'total_moves' in request.session:
        request.session['total_moves'] += 1
    else:
        request.session['total_moves'] = 1

    # if request.POST['location'] == "farm":
    if location == "farm":
        gold = random.randint(10,20)
        if 'gold' in request.session:
            request.session['gold'] += gold 
        else:
            request.session['gold'] = gold
    # if request.POST['location'] == "cave":
    if location == "cave":
        gold = random.randint(5,10)
        if 'gold' in request.session:
            request.session['gold'] += gold 
        else:
            request.session['gold'] = gold
    # if request.POST['location'] == "house":
    if location == "house":
        gold = random.randint(2,5)
        if 'gold' in request.session:
            request.session['gold'] += gold 
        else:
            request.session['gold'] = gold
    # if request.POST['location'] == "casino":
    if location == "casino":
        gold = random.randint(-50,50)
        if 'gold' in request.session:
            request.session['gold'] += gold 
        else:
            request.session['gold'] = gold

    if 'activities' in request.session:
        request.session['activities'].append({
            'delta_gold': gold, 
            # 'location': request.POST['location'], 
            'location': location, 
            "date_time": datetime.now().strftime("%m/%d/%Y, %H:%I")
        })
        request.session.save()
    else:
        request.session['activities'] = [{
            'delta_gold': gold, 
            # 'location': request.POST['location'], 
            'location': location, 
            "date_time": datetime.now().strftime("%m/%d/%Y, %H:%I")
        }]
    
    if int(request.session['total_moves']) == int(request.session['moves']) and int(request.session['gold']) < int(request.session['goal']):
        context = {
            "result": "lost", 
            "total_moves": request.session['total_moves'],
            "moves": request.session['moves'], 
            "total_gold": request.session['gold'], 
            "goal": request.session["goal"]
        }
        return render(request, "result.html", context)
    
    elif int(request.session['total_moves']) <= int(request.session['moves']) and int(request.session['gold']) >= int(request.session['goal']):
        context = {
            "result": "won", 
            "total_moves": request.session['total_moves'],
            "moves": request.session['moves'], 
            "total_gold": request.session['gold'], 
            "goal": request.session["goal"]
        }
        return render(request, "result.html", context)

    elif int(request.session['total_moves']) < int(request.session['moves']) and int(request.session['gold']) < int(request.session['goal']):
        return redirect("/ninja_gold")
    
