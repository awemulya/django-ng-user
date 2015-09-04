from django.shortcuts import render
from .models import Players


def home(request):
    return render(request, 'home.html')


def players(request):
    objlist = Players.objects.all()
    return render(request, 'players.html',{'players':objlist})
