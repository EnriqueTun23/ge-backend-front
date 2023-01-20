""" User person serializer """

# Django Rest Framework
from rest_framework import serializers

# Model
from ..models import UserPerson


class UserPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPerson
        fields = '__all__'