from rest_framework import serializers
from .models import games


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = games
        fields = ['id', 'gametype', 'gamename', 'availableat', 'price']
