from django import forms
from .models import Player, Stat

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('player_name', 'player_position', 'player_photo',)


class StatForm(forms.ModelForm):
    
    class Meta:
        model = Stat
        fields = ('player_team', 'player_point', 'player_rebound', 'player_assist', 'player',)