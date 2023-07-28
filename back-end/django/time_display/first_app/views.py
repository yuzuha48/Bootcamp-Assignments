from django.shortcuts import render, HttpResponse
from time import localtime, strftime

def index(request):
    context = {
        "time": strftime("%B %d, %Y %H:%M %p", localtime())
    }
    return render(request, 'index.html', context)