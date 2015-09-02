from django.shortcuts import render


def profile(request):
    return render(request, 'profile.html')


def players(request):
    return render(request, 'profile.html')
