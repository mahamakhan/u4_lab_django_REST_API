
from rest_framework import generics
from .models import Team, Players, Conference
# Create your views here.
from .serializers import TeamSerializer, PlayersSerializer, ConferenceSerializer


class TeamList(generics.ListCreateAPIView):
        queryset=Team.objects.all()
        serializer_class=TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Team.objects.all()
    serializer_class=TeamSerializer


class PlayersList(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer

class PlayersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer


class ConferenceList(generics.ListCreateAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class ConferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer