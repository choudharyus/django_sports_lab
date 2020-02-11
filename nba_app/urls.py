from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, player= 'player_list')

]