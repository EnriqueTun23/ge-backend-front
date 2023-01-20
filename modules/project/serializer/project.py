""" Project serializer """

# Django Rest framework
from rest_framework import serializers

# Models

from ..models import Project
# Serializer
from modules.files.serializers import ImageProjectSerializer


class ProjectSerializer(serializers.ModelSerializer):
    photos = ImageProjectSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'


    def create(self, validated_data):
        users = validated_data.pop('user')
        photos  = validated_data.pop('photos')
        project =  Project.objects.create(**validated_data)

        if users:
            for user in users:
                project.user.add(user)
        
        if photos:
            for photo in photos:
                project.photos.create(**photo)
                        
        return project




