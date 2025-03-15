from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Menu, Booking

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    booking_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", input_formats=["%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"])

    class Meta:
        model = Booking
        fields = '__all__'
