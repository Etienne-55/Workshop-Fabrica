from rest_framework import serializers
from .models import Carro

class CarroSerializer(serializers.ModelSerializer):
    class meta:
        model = Carro
        fields = ('__all__')