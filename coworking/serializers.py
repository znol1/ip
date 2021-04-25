from rest_framework import serializers
from .models import Reservation, Place, BookedTime
from django.contrib.auth.models import User


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        # depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        depth = 1


class BookedTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedTime
        fields = '__all__'
        # depth = 1