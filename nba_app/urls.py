from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name= 'player_list'),
    path('stats/', views.stat_list, name= 'stat_list'),
    path('players/<int:pk>/', views.player_detail, name='player_detail'),
    path('stats/<int:pk>/', views.stat_detail, name='stat_detail'),
    path('players/new/', views.player_create, name='player_create'),
    path('stats/new/', views.stat_create, name='stat_create'),
    path('players/<int:pk>/edit/', views.player_edit, name='player_edit'),
    path('stats/<int:pk>/edit/', views.stat_edit, name='stat_edit'),
    path('players/<int:pk>/delete/', views.player_delete, name='player_delete'),
    path('stats/<int:pk>/delete/', views.stat_delete, name='stat_delete')

]