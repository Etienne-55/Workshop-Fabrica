from django.urls import path
from .views import CarroLista, CarroDados

urlpatterns = [
    path('Carro/', CarroLista.as_view()),
    path('Carro/', CarroDados.as_view()),
]