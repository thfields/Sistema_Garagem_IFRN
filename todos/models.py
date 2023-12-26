from django.db import models

# Create your models here.

class Todo(models.Model):
  placa = models.CharField(max_length = 7, primary_key=True, null=False, blank=False)
  hora_entrada = models.DateField(auto_now_add=True, null=False, blank=False)
  hora_saida = models.DateField(null=True)
  tipo = models.CharField(max_length = 5, null=False, blank=False)
  #andar = 1 andar 2 andar