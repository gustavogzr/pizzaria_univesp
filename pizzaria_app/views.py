from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from pizzaria_app.models import Restaurante, Pizza, Tamanho
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(request):
    contexto = {
        'nome_usuario': request.session['nome_usuario'],
    }
    return render(request, 'index.html', contexto)

def login(request, redirect_from=None):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Dados para enviar ao back-end Java
        data = {
            'email': username,
            'senha': password
        }

        # URL do endpoint no back-end Java
        java_backend_url = 'http://localhost:8080/v1/api/usuario/login'

        # Enviando os dados para o back-end Java usando Curl
        response = requests.post(java_backend_url, json=data, headers={'Content-Type': 'application/json'})

        # Verificando a resposta
        if response.status_code == 200:
            # Lidar com a resposta do back-end Java
            # (por exemplo, exibir uma mensagem de sucesso)
#<<<<<<< HEAD
                dados_usuario = json.loads(response.text)
                request.session['nome_usuario'] = dados_usuario['nome']
                request.session['token'] = dados_usuario['token']
                request.session['usuarioId'] = dados_usuario['usuarioId']
                request.session['list_roles_usuario'] = dados_usuario['listaRoles']
#=======
 #           request.session['token'] = response.text
#>>>>>>> 49c79cb558ca709dae0a1edae7c962f75cf6896a
                return redirect('/login/login')
        else:
            # Lidar com possíveis erros de solicitação
            return HttpResponse("Erro ao enviar solicitação para o back-end Java.")
    
    contexto = {
        'mensagem_logout': False,      
    }
    if redirect_from == 'login':
        contexto['mensagem_login'] = 'Login realizado com sucesso!'
    if redirect_from == 'logout':
        contexto['mensagem_logout'] = 'Logout realizado com sucesso!'
    if 'nome_usuario' in request.session:
        contexto['nome_usuario'] = request.session['nome_usuario']

    return render(request, 'login.html', contexto)

def logout(request):
    request.session.flush()
    return redirect('/login/logout')
    # return render(request, 'login.html', {'mensagem_logout': 'Logout realizado com sucesso!'})
    

def cadastrar_pizza(request):
    if request.method == 'POST':
        # Dados para enviar ao back-end Java
        data = {
            'categoria': request.POST.get('categoria'),
            'descricao': request.POST.get('descricao'),
            'nome': request.POST.get('nome'),
            'urlimagem': request.POST.get('urlimagem')
        }
        token = request.session['token']
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        # URL do endpoint no back-end Java
        java_backend_url = 'http://localhost:8080/v1/api/pizza'

        # Enviando os dados para o back-end Java usando Curl
        response = requests.post(java_backend_url, json=data, headers=headers)

        # Verificando a resposta
        if response.status_code == 201:
            # Lidar com a resposta do back-end Java
            # (por exemplo, exibir uma mensagem de sucesso)
            return render(request, 'cadastrar_pizza.html', {'mensagem_sucesso': 'Solicitação enviada com sucesso!'})
        else:
            # Lidar com possíveis erros de solicitação
            return HttpResponse("Erro ao enviar solicitação para o back-end Java.")
    
    return render(request, 'cadastrar_pizza.html')

def cadastrar_pizzaria(request):
    if request.method == 'POST':
        # Dados para enviar ao back-end Java
        data = {
            'avaliacao': 0,
            'cep': request.POST.get('cep'),
            'cidade': request.POST.get('cidade'),
            'endereco': request.POST.get('endereco'),
            'nome': request.POST.get('nome'),
            'site': request.POST.get('site'),
            'telefone': request.POST.get('telefone')
        }
        token = request.session['token']
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        # URL do endpoint no back-end Java
        java_backend_url = 'http://localhost:8080/v1/api/pizzaria'

        # Enviando os dados para o back-end Java usando Curl
        response = requests.post(java_backend_url, json=data, headers=headers)

        # Verificando a resposta
        if response.status_code == 201:
            # Lidar com a resposta do back-end Java
            # (por exemplo, exibir uma mensagem de sucesso)
            return render(request, 'cadastrar_pizzaria.html', {'mensagem_sucesso': 'Solicitação enviada com sucesso!'})
        else:
            # Lidar com possíveis erros de solicitação
            return HttpResponse("Erro ao enviar solicitação para o back-end Java.")
        
    return render(request, 'cadastrar_pizzaria.html')

def cadastrar_pizza_pizzaria(request, redirect_from=None):
    if request.method == 'POST':
        # Dados para enviar ao back-end Java
        data = {
            "pizza": [{
                    "id": request.POST.get('pizza'),
                    "preco": request.POST.get('preco')
                }],
            "pizzaria": {
                "id": request.POST.get('pizzaria')
                }
                }
        token = request.session['token']
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        # URL do endpoint no back-end Java
        java_backend_url = 'http://localhost:8080/v1/api/pizzaPizzaria'

        # Enviando os dados para o back-end Java usando Curl
        response = requests.post(java_backend_url, json=data, headers=headers)

        # Verificando a resposta
        if response.status_code == 201:
            # Lidar com a resposta do back-end Java
            # (por exemplo, exibir uma mensagem de sucesso)
            return redirect('/cadastrar_pizza_pizzaria/cadastro_efetuado')
        else:
            # Lidar com possíveis erros de solicitação
            return HttpResponse("Erro ao enviar solicitação para o back-end Java.")

    token = request.session['token']
    headers = {
        'Authorization': f'Bearer {token}',
    }
    # Obter lista de pizzas cadastradas
    java_backend_url = 'http://localhost:8080/v1/api/pizza'
    response = requests.get(java_backend_url, headers=headers)
    lista_pizzas = json.loads(response.text)
    lista_pizzas.sort(key=lambda pizza: pizza['nome'].lower())

    # Obter lista de pizzarias cadastradas
    java_backend_url = 'http://localhost:8080/v1/api/pizzaria'
    response = requests.get(java_backend_url, headers=headers)
    lista_pizzarias = json.loads(response.text)
    lista_pizzarias.sort(key=lambda pizzaria: pizzaria['nome'].lower())

    contexto = {
        'pizzas': lista_pizzas,
        'pizzarias': lista_pizzarias,
    }
    if redirect_from == 'cadastro_efetuado':
        contexto['mensagem_sucesso'] = 'Cadastro realizado com sucesso!'
    if 'nome_usuario' in request.session:
        contexto['nome_usuario'] = request.session['nome_usuario']
    return render(request, 'cadastrar_pizza_pizzaria.html', contexto)

def listar_pizzas(request, redirect_from=None):
    token = request.session['token']
    headers = {
        'Authorization': f'Bearer {token}',
    }
    # Obter lista de pizzas cadastradas
    java_backend_url = 'http://localhost:8080/v1/api/pizza'
    response = requests.get(java_backend_url, headers=headers)
    lista_pizzas = json.loads(response.text)
    lista_pizzas.sort(key=lambda pizza: pizza['nome'].lower())

    contexto = {
        'lista_pizzas': lista_pizzas,
    }
    if redirect_from == 'dados_atualizados':
        contexto['mensagem_cadastro_atualizado'] = 'Dados atualizados com sucesso!'
    if redirect_from == 'dados_excluidos':
        contexto['mensagem_exclusao'] = 'Dados excluídos com sucesso!'
    if redirect_from == 'erro_exclusao':
        contexto['mensagem_erro_exclusao'] = 'Erro ao excluir dados!'
    if 'nome_usuario' in request.session:
        contexto['nome_usuario'] = request.session['nome_usuario']
    return render(request, 'listar_pizzas.html', contexto)

def listar_pizzarias(request, redirect_from=None):
    token = request.session['token']
    headers = {
        'Authorization': f'Bearer {token}',
    }
    # Obter lista de pizzas cadastradas
    java_backend_url = 'http://localhost:8080/v1/api/pizzaria'
    response = requests.get(java_backend_url, headers=headers)
    lista_pizzarias = json.loads(response.text)
    lista_pizzarias.sort(key=lambda pizzaria: pizzaria['nome'].lower())

    contexto = {
        'lista_pizzarias': lista_pizzarias,
    }
    if redirect_from == 'dados_atualizados':
        contexto['mensagem_cadastro_atualizado'] = 'Dados atualizados com sucesso!'
    if redirect_from == 'dados_excluidos':
        contexto['mensagem_exclusao'] = 'Dados excluídos com sucesso!'
    if redirect_from == 'erro_exclusao':
        contexto['mensagem_erro_exclusao'] = 'Erro ao excluir dados!'
    if 'nome_usuario' in request.session:
        contexto['nome_usuario'] = request.session['nome_usuario']
    return render(request, 'listar_pizzarias.html', contexto)

def listar_pizzas_pizzarias(request, redirect_from=None):
    token = request.session['token']
    headers = {
        'Authorization': f'Bearer {token}',
    }
    # Obter lista de pizzas cadastradas
    java_backend_url = 'http://localhost:8080/v1/api/pizzaPizzaria'
    response = requests.get(java_backend_url, headers=headers)
    lista_pizzaPizzarias = json.loads(response.text)
    
    #lista_pizzarias.sort(key=lambda pizzaria: pizzaria['nome'].lower())
    contexto = {
        'lista_pizzaPizzarias': lista_pizzaPizzarias,
    }
    if redirect_from == 'dados_atualizados':
        contexto['mensagem_cadastro_atualizado'] = 'Dados atualizados com sucesso!'
    if redirect_from == 'dados_excluidos':
        contexto['mensagem_exclusao'] = 'Dados excluídos com sucesso!'
    if redirect_from == 'erro_exclusao':
        contexto['mensagem_erro_exclusao'] = 'Erro ao excluir dados!'
    if 'nome_usuario' in request.session:
        contexto['nome_usuario'] = request.session['nome_usuario']
    return render(request, 'listar_pizzas_pizzarias.html', contexto)

def editar_pizza(request, id):
    if request.method == 'POST':
        data = {
            'categoria': request.POST.get('categoria'),
            'descricao': request.POST.get('descricao'),
            'nome': request.POST.get('nome'),
            'urlimagem': request.POST.get('urlimagem')
        }
        token = request.session['token']
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        # URL do endpoint no back-end Java
        java_backend_url = 'http://localhost:8080/v1/api/pizza/' + id
        print(data)
        print(headers)
        print(java_backend_url)
        # Enviando os dados para o back-end Java usando Curl
        response = requests.put(java_backend_url, json=data, headers=headers)
        print(response)
        print(response.text)

        # Verificando a resposta
        if response.status_code == 200:
            # Lidar com a resposta do back-end Java
            # (por exemplo, exibir uma mensagem de sucesso)
            return redirect('/listar_pizzas/dados_atualizados')
        else:
            # Lidar com possíveis erros de solicitação
            return HttpResponse("Erro ao enviar solicitação para o back-end Java.")
    
    # buscar dados da pizza no banco de dados
    token = request.session['token']
    headers = {
        'Authorization': f'Bearer {token}',
    }
    # Obter dados da pizza com id informado
    java_backend_url = 'http://localhost:8080/v1/api/pizza/' + id
    response = requests.get(java_backend_url, headers=headers)
    dados_pizza = json.loads(response.text)
    contexto = {
        'dados_pizza': dados_pizza,
    }
    if 'nome_usuario' in request.session:
        contexto['nome_usuario'] = request.session['nome_usuario']
    return render(request, 'editar_pizza.html', contexto)

def editar_pizzaria(request, id):
    return render(request, 'editar_pizzaria.html')

def editar_pizza_pizzaria(request, id):
    return render(request, 'editar_pizza_pizzaria.html')

def excluir_pizza(request, id):
    token = request.session['token']
    headers = {
        'Authorization': f'Bearer {token}',
    }
    # URL do endpoint no back-end Java
    java_backend_url = 'http://localhost:8080/v1/api/pizza/' + id
    # Enviando os dados para o back-end Java usando Curl
    response = requests.delete(java_backend_url, headers=headers)
    if response.status_code == 200:
            # Lidar com a resposta do back-end Java
            # (por exemplo, exibir uma mensagem de sucesso)
        return redirect('/listar_pizzas/dados_excluidos')
    if response.status_code == 400:
        return redirect('/listar_pizzas/erro_exclusao')
    else:
        # Lidar com possíveis erros de solicitação
        return HttpResponse("Erro ao enviar solicitação para o back-end Java.") 
    

def excluir_pizzaria(request, id):
    return render(request, 'excluir_pizzaria.html')

def excluir_pizza_pizzaria(request, id):
    return render(request, 'excluir_pizza_pizzaria.html')

def restaurantes(request):
    restaurantes = Restaurante.objects.all()
    contexto = {
        'restaurantes': restaurantes,
    }
    return render(request, 'restaurantes.html', contexto)

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