from rest_framework import serializers
from .models import games


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = games
        fields = ['id', 'gametype', 'gamename', 'availableat', 'price']
AWS_SECRET_KEY = '5sVuvbO367NZYBXL7lDEs1HX3Qkz33ks0qpaiGd/'
