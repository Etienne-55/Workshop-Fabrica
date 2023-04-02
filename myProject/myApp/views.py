from rest_framework import generics

from .models import Carro
from .serializers import CarroSerializer

class CarroLista(generics.ListsCreateAPIView):
    serializer_class = CarroSerializer

    def get_queryset(self):
        queryset = Carro.objetos.all()

class CarroDados(generics.RetreiveUpdateDestroyAPIView):
    serializer_class = CarroSerializer
    queryset = Carro.objects.all()