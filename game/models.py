# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model

class SpaceObject(models.Model):
    OBJECT_TYPE_CHOICES = [
        ('asteroid', 'Asteroid'),
        ('planet', 'Planet'),
    ]

    object_type = models.CharField(max_length=10, choices=OBJECT_TYPE_CHOICES)
    pos_x = models.FloatField()
    pos_y = models.FloatField()

    def __str__(self):
        return f"{self.object_type.capitalize()} at ({self.pos_x}, {self.pos_y})"


class Player(models.Model):
    username = models.CharField(max_length=50, unique=True)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Rocket(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('destroyed', 'Destroyed'),
    ]

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    speed_x = models.FloatField()
    speed_y = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"Rocket of {self.player.username} ({self.status})"
