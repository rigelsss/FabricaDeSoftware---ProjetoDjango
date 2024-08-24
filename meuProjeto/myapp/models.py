from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    ies = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nome}, {self.email}, {self.ies}'
    

class Detalhe(models.Model):
    cidade = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data = models.DateField()
    cep = models.IntegerField()

    def __str__(self):
        return f'{self.cidade}, {self.cep}, {self.data}'