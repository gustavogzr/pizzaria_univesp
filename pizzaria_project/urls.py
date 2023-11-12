"""pizzaria_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pizzaria_app import views as pizzaria_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pizzaria_app_views.index, name='index'),
    #
    path('login/', pizzaria_app_views.login, name='login'),
    path('login/<str:redirect_from>/', pizzaria_app_views.login, name='login_redirect'),
    path('logout/', pizzaria_app_views.logout, name='logout'),

    path('cadastrar_pizza/', pizzaria_app_views.cadastrar_pizza, name='cadastrar_pizza'),
    path('listar_pizzas/', pizzaria_app_views.listar_pizzas, name='listar_pizzas'),
    path('listar_pizzas/<str:redirect_from>/', pizzaria_app_views.listar_pizzas, name='listar_pizzas_redirect'),
    path('editar_pizza/<str:id>/', pizzaria_app_views.editar_pizza, name='editar_pizza_id'),
    path('excluir_pizza/<str:id>/', pizzaria_app_views.excluir_pizza, name='excluir_pizza_id'),
    path('pizza/<str:id>/', pizzaria_app_views.pizza, name='pizza'),

    path('cadastrar_pizzaria/', pizzaria_app_views.cadastrar_pizzaria, name='cadastrar_pizzaria'),
    path('listar_pizzarias/', pizzaria_app_views.listar_pizzarias, name='listar_pizzarias'),
    path('listar_pizzarias/<str:redirect_from>/', pizzaria_app_views.listar_pizzarias, name='listar_pizzarias_redirect'),
    path('editar_pizzaria/<str:id>/', pizzaria_app_views.editar_pizzaria, name='editar_pizzaria_id'),
    path('excluir_pizzaria/<str:id>/', pizzaria_app_views.excluir_pizzaria, name='excluir_pizzaria_id'),
    path('pizzaria/<str:id>/', pizzaria_app_views.pizzaria, name='pizzaria'),

    path('cadastrar_pizza_pizzaria/', pizzaria_app_views.cadastrar_pizza_pizzaria, name='cadastrar_pizza_pizzaria'),
    path('cadastrar_pizza_pizzaria/<str:redirect_from>/', pizzaria_app_views.cadastrar_pizza_pizzaria, name='cadastrar_pizza_pizzaria_redirect'),
    path('listar_pizzas_pizzarias/', pizzaria_app_views.listar_pizzas_pizzarias, name='listar_pizzas_pizzarias'),
    path('listar_pizzas_pizzarias/<str:redirect_from>/', pizzaria_app_views.listar_pizzas_pizzarias, name='listar_pizzas_pizzarias_redirect'),
    path('editar_pizza_pizzaria/<str:id>/', pizzaria_app_views.editar_pizza_pizzaria, name='editar_pizza_pizzaria_id'),
    path('excluir_pizza_pizzaria/<str:id>/', pizzaria_app_views.excluir_pizza_pizzaria, name='excluir_pizza_pizzaria_id'),
]
