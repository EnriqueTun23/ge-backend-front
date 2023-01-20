""" User Serializer """
# Django Rest Framework
from rest_framework import serializers
# Model
from ..models import User, UserPerson, UserRol

# Serializer
from .userPerson import UserPersonSerializer
from .userRol import UserRolSerializer



class UserSerializer(serializers.ModelSerializer):
    userRol = UserRolSerializer()
    userPerson = UserPersonSerializer()

    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'ext', 'mobile_number', 'is_verified', 'userRol', 'userPerson')

    def create(self, validated_data):
        rol =  validated_data.pop('userRol')
        person = validated_data.pop('userPerson')
        rol_post = UserRol.objects.create(**rol)
        person_post =  UserPerson.objects.create(**person)
        if rol_post:
            if person_post:
                user_post = User.objects.create_user(userRol=rol_post, userPerson=person_post, **validated_data)
            else:
                user_post = User.objects.create_user(userRol=rol_post, **validated_data)
        else:
            user_post = User.objects.create_user(**validated_data)
        
        return user_post   
    
    def update(self, instance, validated_data):
        user = instance
        rol_data =  validated_data.pop('userRol')
        person_data = validated_data.pop('userPerson')

        if(rol_data):
            rol = UserRolSerializer(instance.userRol, data=rol_data, partial=True)
            rol.is_valid()
            rol.save()
        
        if(person_data):
            person = UserPersonSerializer(instance.userPerson, data=person_data, partial=True)
            person.is_valid()
            person.save()
        
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.phone_number =  validated_data.get('phone_number', user.phone_number)
        user.ext = validated_data.get('ext', user.ext)
        user.mobile_number = validated_data.get('mobile_number', user.mobile_number)

        user.save()

        return instance