from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

def get_default_user():
    try:
        return User.objects.get(id=4)  # Example default user ID
    except ObjectDoesNotExist:
        return None


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=4)  # Ensure each user has only one player instance
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

 


class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    rocket_position_x = models.IntegerField(default=100)
    rocket_position_y = models.IntegerField(default=200)
    asteroids = models.JSONField(default=list)

    def __str__(self):
        return f'Game for {self.player.user.username}'
