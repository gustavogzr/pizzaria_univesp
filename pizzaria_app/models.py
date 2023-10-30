from django.db import models

# Create your models here.

# criar modelo para restaurante
class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    
# criar modelo para pizzas vendidas para cada restaurante
class Pizza(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

# criar modelo para tamanho das pizzas e seus preços
class Tamanho(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nome