from django.contrib import admin
from .models import Restaurante, Pizza, Tamanho

# Register your models here.

# criar modelo para restaurante
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'email', 'cidade')

# criar modelo para pizzas vendidas para cada restaurante
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ingredientes', 'restaurante')

# criar modelo para tamanho das pizzas e seus preços
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'pizza')

admin.site.register(Restaurante, RestauranteAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Tamanho, TamanhoAdmin)