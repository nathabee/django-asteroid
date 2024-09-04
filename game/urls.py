from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Define the router and register your viewsets
router = DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'games', views.GameViewSet)

# Define the urlpatterns list
urlpatterns = [
    path('', include(router.urls)),  # No 'api/' prefix here
    path('initialize/', views.initialize_game, name='initialize_game'),  # No 'api/' prefix
    path('submit_score/', views.submit_score, name='submit_score'),
    path('leaderboard/', views.get_leaderboard, name='get_leaderboard'),
    path('update_action/', views.update_player_action, name='update_player_action'),
]
