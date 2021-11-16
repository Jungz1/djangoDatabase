from django.urls import path, reverse

from . import views

from collection.api import consoles_api, console_api, games_api, game_api

urlpatterns = [
    path('', views.index, name='index'),
    path('/api/consoles', consoles_api, name='consoles api'),
    path('/api/console/<int:id>', console_api, name='console api'),
    path('/api/games', games_api, name='games api'),
    path('/api/game/<int:id>', game_api, name='game api'),
]