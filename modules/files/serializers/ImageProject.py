""" image project serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from modules.files.models import  ImageProject


class ImageProjectSerializer(serializers.ModelSerializer):
    """ Image project serializer """
    class Meta:
        model = ImageProject
        fields = '__all__'

