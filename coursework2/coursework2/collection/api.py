from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
import json
from datetime import datetime

from .models import Console, Game


def console_api(request, id):
    '''
        API entry point for each country
    '''

    if request.method == "DELETE":
        console = get_object_or_404(Console, id=id)
        console.delete()
        return JsonResponse({})

    return HttpResponseBadRequest("Invalid method")



def consoles_api(request):
    '''
        API entry point for list of countries
        On POST: Create a new countries

    '''
    if request.method == "GET":
        return JsonResponse({
                'consoles': [
                    console.to_dict()
                    for console in Console.objects.all()
                ]
            })

    if request.method == "POST":
                body = json.loads(request.body.decode('utf-8'))
                date_time_str = body['release_date']
                date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
                newConsole = Console(console_name = body['console_name'],release_date = date_time_obj,price = body['price'],developer = body['developer'])
                newConsole.save()
                return JsonResponse({})

    return HttpResponseBadRequest("Invalid method")



def game_api(request, id):
    '''
        API entry point for each country
    '''

    if request.method == "DELETE":
        game = get_object_or_404(Game, id=id)
        game.delete()
        return JsonResponse({})

    return HttpResponseBadRequest("Invalid method")

def games_api(request):
    '''
        API entry point for list of countries
        On POST: Create a new countries
    '''
    return JsonResponse({
        'games': [
            game.to_dict()
            for game in Game.objects.all()
        ]
    })