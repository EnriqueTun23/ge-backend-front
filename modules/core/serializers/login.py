""" Login Serializer """

# Django 
from django.contrib.auth import authenticate


# Django REST FRAMEWORK 
from rest_framework import serializers
from rest_framework.authtoken.models import Token



class LoginSerializer(serializers.Serializer):
    """ responsible for validating the login and creating your authenfication token """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=7)

    def validate(self, data):
        """ validatin the login"""
        login = authenticate(username=data['email'], password=data['password'])
        if not login:
            raise serializers.ValidationError('Credenciales invalidas')
        self.context['login'] = login
        return data
    
    def create(self, data):
        """ retorna el token que debe ir """
        return self.context['login']