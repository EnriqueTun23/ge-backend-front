# Serializer Coigos Postales
from rest_framework import serializers
from .models import CodigoPostales

class CodigosPostalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoPostales
        fields = '__all__'

