from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=100, unique=True)
    modelo= models.CharField(max_length=100, unique=True)
    ano = models.BigIntegerField()

    def __str__(self):
        return self.marca
    
    def __str__(self):
        return self.modelo
   
    def __str__(self):
        return self.ano