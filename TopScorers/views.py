from django.shortcuts import render, get_object_or_404, redirect
from .models import Player, Club, Stats
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import RegistrationForm, PlayerForm
from django.contrib.auth.views import LoginView


def player_list(request):
    players = Player.objects.select_related('club').all()
    return render(request, 'player_list.html', {'players': players})


def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'club_list.html', {'clubs': clubs})


def stats_list(request):
    stats = Stats.objects.all()
    return render(request, 'stats_list.html', {'stats': stats})


def player_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'player_detail.html', {'player': player, 'stats': player.stats})


def club_detail(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    return render(request, 'club_detail.html', {'club': club_id})


def stats_detail(request, stats_id):
    stats = get_object_or_404(Stats, pk=stats_id)
    return render(request, 'stats_detail.html', {'stats': stats})


# def add_player(request):
#     # Tworzenie piłkarza...
#     return render(request, 'add_player.html')


def add_stats(request):
    # Dodawanie statystyk...
    return render(request, 'add_stats.html')


def menu(request):
    return render(request, 'includes/menu.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('player_list')  # Przekieruj użytkownika po udanej rejestracji
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login(request):
    return LoginView.as_view(template_name='registration/login.html')(request)


@login_required
def add_player(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        club_name = request.POST.get('club_name')
        club_country = request.POST.get('club_country')  # Dodane pole 'Kraj'
        club_league = request.POST.get('club_league')    # Dodane pole 'Liga'

        # Tworzenie klubu (jeśli nie istnieje)
        club, created = Club.objects.get_or_create(
            club_name=club_name,
            defaults={
                'country': club_country,
                'league': club_league
            }
        )

        # Tworzenie gracza i przypisanie klubu
        player = Player.objects.create(
            player_name=player_name,
            club=club
            # Dodaj tutaj inne pola gracza, jeśli istnieją
        )

        # Przekierowanie na stronę z listą graczy
        return redirect('player_list')

    return render(request, 'add_player.html')



def logout_user(request):
    logout(request)
    return redirect('menu')  # Przekieruj użytkownika po wylogowaniu
