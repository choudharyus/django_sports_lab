from django.db import models

# Create your models here.

class Player(models.Model):
    player_name = models.CharField(max_length=100)
    player_position = models.CharField(max_length=100)
    player_photo = models.TextField()

    def __str__(self):
        return self.player_name

class Stat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='stats')
    player_team = models.CharField(max_length=100, default='Enter team')
    player_point = models.CharField(max_length=100, default='Enter points')
    player_rebound = models.CharField(max_length=100, default='Enter rebounds')
    player_assist = models.CharField(max_length=100, default='Enter assists')

    def __str__(self):
        return self.player_team