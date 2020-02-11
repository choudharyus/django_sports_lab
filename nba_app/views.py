from django.shortcuts import render, redirect

from django.shortcuts import render
from .models import Player, Stat
from .forms import PlayerForm, StatForm

# Create your views here.

def player_list(request):
    players = Player.objects.all()
    return render(request, 'nba_app/player_list.html', {'players': players})


def player_detail(request, pk):
    player = Player.objects.get(id=pk)
    return render(request, 'nba_app/player_detail.html', {'player': player})



def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save()
            return redirect('player_detail', pk=player.pk)
    else:
        form = PlayerForm()
    return render(request, 'nba_app/player_form.html', {'form': form})


def player_edit(request, pk):
    player = Player.objects.get(pk=pk)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save()
            return redirect('player_detail', pk=player.pk)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'nba_app/player_formƒ.html', {'form': form})



def player_delete(request, pk):
    Player.objects.get(id=pk).delete()
    return redirect('player_list')


def stat_list(request):
    stats = Stat.objects.all()
    return render(request, 'nba_app/stat_list.html', {'stats': stats})


def stat_detail(request, pk):
    stat = Stat.objects.get(id=pk)
    return render(request, 'nba_app/stat_detail.html', {'stat': stat})



def stat_create(request):
    if request.method == 'POST':
        form = StatForm(request.POST)
        if form.is_valid():
            stat = form.save()
            return redirect('stat_detail', pk=stat.pk)
    else:
        form = StatForm()
    return render(request, 'nba_app/stat_form.html', {'form': form})



def stat_edit(request, pk):
    stat = Stat.objects.get(pk=pk)
    if request.method == "POST":
        form = StatForm(request.POST, instance=stat)
        if form.is_valid():
            player = form.save()
            return redirect('stat_detail', pk=stat.pk)
    else:
        form = StatForm(instance=stat)
    return render(request, 'nba_app/stat_form.html', {'form': form})



def stat_delete(request, pk):
    Stat.objects.get(id=pk).delete()
    return redirect('stat_list')
