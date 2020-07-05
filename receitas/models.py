from django.db import models

# Create your models here.
class Receita(models.Model):
    nome      = models.CharField(max_length=50)
    descricao = models.TextField()
    valor     = models.DecimalField(max_digits=9, decimal_places=2)
    data      = models.DateTimeField(auto_now_add=True)