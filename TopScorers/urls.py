from django.urls import path
from . import views
from .views import add_player, add_stats, menu, register, login

urlpatterns = [
    path('players/', views.player_list, name='player_list'),
    path('players/<int:player_id>/', views.player_detail, name='player_detail'),
    path('clubs/', views.club_list, name='club_list'),
    path('stats/', views.stats_list, name='stats_list'),
    path('player/<int:player_id>/', views.player_detail, name='player_detail'),
    path('club/<int:club_id>/', views.club_detail, name='club_detail'),
    path('stats/<int:stats_id>/', views.stats_detail, name='stats_detail'),
    path('add/player/', add_player, name='add_player'),
    path('add/stats/', add_stats, name='add_stats'),
    path('', menu, name='menu'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
