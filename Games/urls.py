from django.urls import path
from . import views


urlpatterns=[
    path('',views.GameListAPIView.as_view(),name="GameList"),
    path('<int:id>',views.GameDetailAPIView.as_view(),name="GameList"),
    ]
