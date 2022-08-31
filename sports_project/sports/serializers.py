from rest_framework import serializers
from .models import Team, Players, Conference


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players= serializers.HyperlinkedRelatedField(
        view_name='players_detail',
        many=True,
        read_only=True
    )
    conference= serializers.HyperlinkedRelatedField(
        view_name='conference_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model=Team
        fields=('id', 'name','location','division','number_of_wins','number_of_losses', 'players', 'conference')


class PlayersSerializer(serializers.HyperlinkedModelSerializer):
    team= serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model=Players
        fields=('id','team','name','age','position','injured_reserved_list')


class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    team= serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model=Conference
        fields=('id','team','conference')





