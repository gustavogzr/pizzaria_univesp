from django.shortcuts import render
from django.shortcuts import get_object_or_404
from pizzaria_app.models import Restaurante, Pizza, Tamanho

# Create your views here.
def index(request):
    return render(request, 'index.html')

def restaurantes(request):
    return render(request, 'restaurantes.html')

def restaurante_pg(request, id):
    restaurante = get_object_or_404(Restaurante, id=id)
    pizzas = Pizza.objects.filter(restaurante=restaurante)
    contexto = {
        'restaurante': restaurante,
        'pizzas': pizzas,
    }
    return render(request, 'restaurante_pg.html', contexto)

def pizza_pg(request, id, id_pizza):
    restaurante = get_object_or_404(Restaurante, id=id)
    pizza = get_object_or_404(Pizza, id=id_pizza)
    tamanhos = Tamanho.objects.filter(pizza=pizza)
    contexto = {
        'restaurante': restaurante,
        'pizza': pizza,
        'tamanhos': tamanhos,
    }
    return render(request, 'pizza_pg.html', contexto)