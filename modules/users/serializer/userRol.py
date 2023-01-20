""" User Rol serializer """

# Django Rest Framework
from rest_framework import serializers
# Model
from ..models import UserRol



class UserRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRol
        fields = '__all__'

