from rest_framework import serializers
from .models import Articulo

#class serializadora

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'
