from django.shortcuts import render
from .models import Player, Stat


# Create your views here.

def player_list(request):
    players = Player.objects.all()
    return render(request, 'nba_app/player_list.html', {'players': players})

