from rest_framework import serializers
from .models import Player, Game  # Ensure Rocket is not mistakenly included


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


# for swagger :
class InitializeGameSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
 

class SubmitScoreSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    score = serializers.IntegerField()

class UpdatePlayerActionSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    action = serializers.CharField()


class LeaderboardSerializer(serializers.Serializer):
    leaderboard = serializers.ListSerializer(child=PlayerSerializer())