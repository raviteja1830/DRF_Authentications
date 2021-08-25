from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import GameSerializer
from .models import games
from rest_framework import permissions
from .permissions import IsOwner
# Create your views here.


class GameListAPIView(ListCreateAPIView):
    serializer_class=GameSerializer
    queryset=games.objects.all()
    permission_classes=(permissions.IsAuthenticated,)



    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)




class GameDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = games.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
