""" Client serializer """

# Django REST FRAMEWORK 
from rest_framework import serializers

# Models
from ..models import Cliente


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    
    def create(self, validated_data):
        users = validated_data.pop('users')
        projects = validated_data.pop('projects')
        client = Cliente.objects.create(**validated_data)

        if users:
            for user in users:
                client.users.add(user)
        
        if projects:
            for project in projects:
                client.projects.add(project)


        return client