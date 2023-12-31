from django.shortcuts import render, get_object_or_404, redirect
from .models import Player, Club, Stats
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, PlayerForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# def player_list(request):
#     players = Player.objects.select_related('club').all()
#     return render(request, 'player_list.html', {'players': players})


# def player_list(request):
#     search_query = request.GET.get('search', '')
#
#     if search_query:
#         players = Player.objects.select_related('club').filter(
#             Q(player_name__icontains=search_query) | Q(club__club_name__icontains=search_query)
#         )
#     else:
#         players = Player.objects.select_related('club').all()
#
#     return render(request, 'player_list.html', {'players': players})

def player_list(request):
    search_query = request.GET.get('search', '')
    players_per_page = 50

    if search_query:
        players = Player.objects.select_related('club').filter(
            Q(player_name__icontains=search_query) | Q(club__club_name__icontains=search_query)
        )
    else:
        players = Player.objects.select_related('club').all()

    paginator = Paginator(players, players_per_page)

    page = request.GET.get('page')
    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(paginator.num_pages)

    return render(request, 'player_list.html', {'players': players})


def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'club_list.html', {'clubs': clubs})


def stats_list(request):
    stats = Stats.objects.all()
    return render(request, 'stats_list.html', {'stats': stats})


def player_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    stats = player.stats
    return render(request, 'player_detail.html', {'player': player, 'stats': stats})


def club_detail(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    return render(request, 'club_detail.html', {'club': club})


def stats_detail(request, stats_id):
    stats = get_object_or_404(Stats, pk=stats_id)
    return render(request, 'stats_detail.html', {'stats': stats})


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


# def login(request, user):
#     return LoginView.as_view(template_name='registration/login.html')(request, user)


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('player_list')
#         else:
#             messages.error(request, 'Nieprawidłowy login lub hasło.')
#
#     return render(request, 'registration/login.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            return redirect('player_list')
    else:
        form = AuthenticationForm(request)

    return render(request, 'registration/login.html', {'form': form})



@login_required
def add_player(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        club_name = request.POST.get('club_name')
        club_country = request.POST.get('club_country')
        club_league = request.POST.get('club_league')

        # Sprawdzenie czy klub już istnieje
        clubs = Club.objects.filter(club_name=club_name)

        if clubs.exists():
            # Jeśli klub istnieje, użyj pierwszego pasującego klubu
            club = clubs.first()
        else:
            # Jeśli klub nie istnieje, stwórz nowy klub
            club = Club.objects.create(
                club_name=club_name,
                country=club_country,
                league=club_league
            )

        # Tworzenie gracza i przypisanie klubu
        player = Player.objects.create(
            player_name=player_name,
            club=club
        )

        # Przekierowanie na stronę z listą graczy
        return redirect('player_list')

    return render(request, 'add_player.html')


def logout_user(request):
    logout(request)
    return redirect('menu')  # Przekieruj użytkownika po wylogowaniu


#
# @login_required
# def add_stats(request):
#     if request.method == 'POST':
#         matches_played = request.POST.get('matches_played')
#         substitution = request.POST.get('substitution')
#         mins = request.POST.get('mins')
#         goals = request.POST.get('goals')
#         xG = request.POST.get('xG')
#         xG_per_avg_match = request.POST.get('xG_per_avg_match')
#         shots = request.POST.get('shots')
#         on_target = request.POST.get('on_target')
#         shots_per_avg_match = request.POST.get('shots_per_avg_match')
#         on_target_per_avg_match = request.POST.get('on_target_per_avg_match')
#         year = request.POST.get('year')
#
#         stats = Stats.objects.create(
#             matches_played=matches_played,
#             substitution=substitution,
#             mins=mins,
#             goals=goals,
#             xG=xG,
#             xG_per_avg_match=xG_per_avg_match,
#             shots=shots,
#             on_target=on_target,
#             shots_per_avg_match=shots_per_avg_match,
#             on_target_per_avg_match=on_target_per_avg_match,
#             year=year,
#         )
#
#
#         return redirect('player_list')
#
#     return render(request, 'add_stats.html')

@login_required
def add_stats(request, player_id):
    if request.method == 'POST':
        matches_played = request.POST.get('matches_played')
        substitution = request.POST.get('substitution')
        mins = request.POST.get('mins')
        goals = request.POST.get('goals')
        xG = request.POST.get('xG')
        xG_per_avg_match = request.POST.get('xG_per_avg_match')
        shots = request.POST.get('shots')
        on_target = request.POST.get('on_target')
        shots_per_avg_match = request.POST.get('shots_per_avg_match')
        on_target_per_avg_match = request.POST.get('on_target_per_avg_match')
        year = request.POST.get('year')

        # Pobierz gracza
        player = get_object_or_404(Player, pk=player_id)

        # Przypisz statystyki do gracza
        stats = Stats.objects.create(
            matches_played=matches_played,
            substitution=substitution,
            mins=mins,
            goals=goals,
            xG=xG,
            xG_per_avg_match=xG_per_avg_match,
            shots=shots,
            on_target=on_target,
            shots_per_avg_match=shots_per_avg_match,
            on_target_per_avg_match=on_target_per_avg_match,
            year=year,
        )

        player.stats = stats
        player.save()

        return redirect('player_list')

    return render(request, 'add_stats.html', {'player_id': player_id})
