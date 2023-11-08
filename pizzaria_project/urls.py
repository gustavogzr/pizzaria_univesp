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
    
    path('restaurantes/', pizzaria_app_views.restaurantes, name='restaurantes'),
    path('restaurante/<int:id>/', pizzaria_app_views.restaurante_pg, name='restaurante_pg'),
    path('restaurante/<int:id>/pizza/<int:id_pizza>/', pizzaria_app_views.pizza_pg, name='pizza_pg'),
    #
    path('login/', pizzaria_app_views.login, name='login'),
    path('login/<str:redirect_from>/', pizzaria_app_views.login, name='login'),
    path('logout/', pizzaria_app_views.logout, name='logout'),
    path('cadastrar_pizza/', pizzaria_app_views.cadastrar_pizza, name='cadastrar_pizza'),
    path('listar_pizzas/', pizzaria_app_views.listar_pizzas, name='listar_pizzas'),
    path('cadastrar_pizzaria/', pizzaria_app_views.cadastrar_pizzaria, name='cadastrar_pizzaria'),
    path('listar_pizzarias/', pizzaria_app_views.listar_pizzarias, name='listar_pizzarias'),
    path('cadastrar_pizza_pizzaria/', pizzaria_app_views.cadastrar_pizza_pizzaria, name='cadastrar_pizza_pizzaria'),
    path('listar_pizzas_pizzarias/', pizzaria_app_views.listar_pizzas_pizzarias, name='listar_pizzas_pizzarias'),
]
