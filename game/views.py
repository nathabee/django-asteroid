
#from rest_framework import viewsets, status
#from rest_framework.response import Response
#from rest_framework.decorators import action, api_view
#from .models import Player, Game
#from .serializers import PlayerSerializer, GameSerializer, InitializeGameSerializer,SubmitScoreSerializer,UpdatePlayerActionSerializer,LeaderboardSerializer
#from django.contrib.auth.models import User 

# Function-based views for more specific custom logic
#from .serializers import InitializeGameSerializer  # Import your serializer
#from drf_yasg.utils import swagger_auto_schema
# Correct imports in views.py
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import PlayerSerializer, GameSerializer, InitializeGameSerializer,SubmitScoreSerializer,UpdatePlayerActionSerializer,LeaderboardSerializer
from .models import Player, Game
from django.contrib.auth.models import User 
from drf_yasg.utils import swagger_auto_schema
# Other imports
 


# PlayerViewSet to handle standard operations and custom actions
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(detail=True, methods=['post'])
    def submit_score(self, request, pk=None):
        player = self.get_object()
        score = request.data.get('score')

        if score is not None:
            player.score = score
            player.save()
            return Response({"status": "success", "message": "Score submitted successfully."}, status=status.HTTP_200_OK)
        return Response({'error': 'Score not provided.'}, status=status.HTTP_400_BAD_REQUEST)


# GameViewSet to handle standard operations and custom actions
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=True, methods=['post'])
    def update_player_action(self, request, pk=None):
        game = self.get_object()
        action = request.data.get('action')

        # Update game state based on action
        if action == 'move_up':
            game.rocket_position_y -= 50
        elif action == 'move_down':
            game.rocket_position_y += 50
        elif action == 'move_left':
            game.rocket_position_x -= 50
        elif action == 'move_right':
            game.rocket_position_x += 50

        # Example asteroid update (move based on direction)
        for asteroid in game.asteroids:
            if asteroid['direction'] == 'left':
                asteroid['x'] -= asteroid['speed']
            elif asteroid['direction'] == 'down':
                asteroid['y'] += asteroid['speed']

        game.save()
        return Response({
            "new_rocket_position": {"x": game.rocket_position_x, "y": game.rocket_position_y},
            "asteroids": game.asteroids
        }, status=status.HTTP_200_OK)



 


@swagger_auto_schema(
    method='post',
    request_body=InitializeGameSerializer,
    responses={
        201: 'Game initialized successfully',
        400: 'Invalid input'
    }
)
@api_view(['POST'])
def initialize_game(request):
    # Extract user ID from request
    user_id = request.data.get('user_id')
    
    # Find or create player using the user field
    user = User.objects.get(id=user_id)
    player, created = Player.objects.get_or_create(user=user)

    # Create initial game state
    initial_rocket_position = {'x': 100, 'y': 200}
    initial_asteroids = [
        {'x': 300, 'y': 100, 'speed': 5, 'direction': 'left'},
        {'x': 500, 'y': 200, 'speed': 3, 'direction': 'down'}
    ]
    
    game = Game.objects.create(
        player=player,
        rocket_position_x=initial_rocket_position['x'],
        rocket_position_y=initial_rocket_position['y'],
        asteroids=initial_asteroids
    )
    
    # Serialize game state
    game_data = {
        "rocket_position": initial_rocket_position,
        "asteroids": initial_asteroids
    }

    return Response(game_data, status=status.HTTP_201_CREATED)



@swagger_auto_schema(
    method='post',
    request_body=SubmitScoreSerializer,
    responses={
        200: 'Score submitted successfully',
        404: 'Player not found'
    }
)
@api_view(['POST'])
def submit_score(request):
    user_id = request.data.get('user_id')
    score = request.data.get('score')

    try:
        player = Player.objects.get(user__id=user_id)
        player.score = score
        player.save()
        return Response({"status": "success", "message": "Score submitted successfully."}, status=status.HTTP_200_OK)
    except Player.DoesNotExist:
        return Response({'error': 'Player not found.'}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='get',
    responses={200: LeaderboardSerializer()},
    operation_description="Retrieve the top 10 players based on their scores."
) 
@api_view(['GET'])
def get_leaderboard(request):
    players = Player.objects.order_by('-score')[:10]  # Top 10 players
    leaderboard = [{"user_id": player.user.id, "username": player.user.username, "score": player.score} for player in players]
    return Response({"leaderboard": leaderboard}, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='post',
    request_body=UpdatePlayerActionSerializer,
    responses={
        200: 'Action updated successfully',
        404: 'Game not found'
    }
)
@api_view(['POST'])
def update_player_action(request):
    user_id = request.data.get('user_id')
    action = request.data.get('action')
    
    try:
        game = Game.objects.get(player__user__id=user_id)
    except Game.DoesNotExist:
        return Response({'error': 'Game not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Update game state based on action
    if action == 'move_up':
        game.rocket_position_y -= 50  # Example action handling
    elif action == 'move_down':
        game.rocket_position_y += 50
    elif action == 'move_left':
        game.rocket_position_x -= 50
    elif action == 'move_right':
        game.rocket_position_x += 50

    # Example asteroid update (move based on direction)
    for asteroid in game.asteroids:
        if asteroid['direction'] == 'left':
            asteroid['x'] -= asteroid['speed']
        elif asteroid['direction'] == 'down':
            asteroid['y'] += asteroid['speed']
    
    # Save updated game state
    game.save()
    
    # Respond with updated game state
    updated_game_state = {
        "new_rocket_position": {"x": game.rocket_position_x, "y": game.rocket_position_y},
        "asteroids": game.asteroids
    }
    return Response(updated_game_state, status=status.HTTP_200_OK)

