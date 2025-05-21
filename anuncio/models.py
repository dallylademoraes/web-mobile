# anuncio/models.py

from django.db import models

class Veiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=50)
    combustivel = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano})'
