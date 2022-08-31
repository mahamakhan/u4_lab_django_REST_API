from django.urls import path
from . import views

urlpatterns= [
    path('team', views.TeamList.as_view(), name='team_list'),
    path('players', views.PlayersList.as_view(), name='players_list'),
    path('conference', views.ConferenceList.as_view(), name='conference_list'),
    path('team/<int:pk>', views.TeamDetail.as_view(), name='team_detail'),
    path('players/<int:pk>', views.PlayersDetail.as_view(), name='players_detail'),
    path('conference/<int:pk>', views.ConferenceDetail.as_view(), name='conference_detail')
]

