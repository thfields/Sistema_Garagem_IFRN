from django.db import models

# Create your models here.
LISTA_VEICULO= [
    ('Motocicleta', 'Motocicleta'),
    ('Carro', 'Carro'),
]
LISTA_ANDAR=[
  ('Andar 1', 'Andar 1'),
    ('Andar 2', 'Andar2'),
]
class Constante(models.Model):
    carro = models.IntegerField()
    moto = models.IntegerField()
      
class Todo(models.Model):
  placa = models.CharField(max_length = 7, primary_key=True, null=False, blank=False)
  andar = models.CharField(choices=LISTA_ANDAR, null=True, max_length = 8, blank=False)
  hora_entrada = models.TimeField(auto_now_add=True, null=False, blank=False)
  hora_saida = models.TimeField(null=True)
  tipo = models.CharField(choices=LISTA_VEICULO, max_length = 11, null=False, blank=False)
  valor = models.IntegerField(null=True)
  