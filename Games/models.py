from django.db import models
from authentication.models import User
# Create your models here.
class games(models.Model):
    GAME_TYPE=[
    ('FPS GAME','FPS GAME'),
    ('TPS GAME','TPS GAME'),
    ('SPS GAME','SPS GAME'),
    ]

    gametype=models.CharField(choices=GAME_TYPE,max_length=255)
    gamename=models.CharField(max_length=255)
    availableat=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2,max_length=255)
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
