from django.db import models

class Metragem(models.Model):
    largura = models.FloatField()
    comprimento = models.FloatField()
