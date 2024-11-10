from rest_framework import serializers
from tickets.models import Movie,Geust,Resevation


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
        
        
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Geust
        fields=['pk','reservation','name','phone']
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resevation
        fields='__all__'
        
        