from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect, render
from collection.models import Console,Game

def index(request):
    consoles = Console.objects.all()
    games = Game.objects.all()
    request.session['last_visit'] = str(timezone.now())
    return render(request, 'collection/index.html', {
            'consoles': Console,
            'games': Game,

    })