"""
URL configuration for source project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('integrante', views.integrante, name='integrante'),
    path('administrador', views.administrador, name='administrador'),

    path('', views.index, name='index'),
    path('integrante', views.integrante, name='integrante'),
    path('administrador', views.administrador, name='administrador'),

    # Rotas para Usuario
    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/create/', views.usuario_create, name='usuario_create'),
    path('usuarios/<int:pk>/update/', views.usuario_update, name='usuario_update'),
    path('usuarios/<int:pk>/delete/', views.usuario_delete, name='usuario_delete'),

    # Rotas para Administrador
    path('administradores/', views.administrador_list, name='administrador_list'),
    path('administradores/create/', views.administrador_create, name='administrador_create'),
    path('administradores/<int:pk>/update/', views.administrador_update, name='administrador_update'),
    path('administradores/<int:pk>/delete/', views.administrador_delete, name='administrador_delete'),

    # Rotas para Grupo
    path('grupos/', views.grupo_list, name='grupo_list'),
    path('grupos/create/', views.grupo_create, name='grupo_create'),
    path('grupos/<int:pk>/update/', views.grupo_update, name='grupo_update'),
    path('grupos/<int:pk>/delete/', views.grupo_delete, name='grupo_delete'),

    # Rotas para Subgrupo
    path('subgrupos/', views.subgrupo_list, name='subgrupo_list'),
    path('subgrupos/create/', views.subgrupo_create, name='subgrupo_create'),
    path('subgrupos/<int:pk>/update/', views.subgrupo_update, name='subgrupo_update'),
    path('subgrupos/<int:pk>/delete/', views.subgrupo_delete, name='subgrupo_delete'),

    # Rotas para Tarefa
    path('tarefas/', views.tarefa_list, name='tarefa_list'),
    path('tarefas/create/', views.tarefa_create, name='tarefa_create'),
    path('tarefas/<int:pk>/update/', views.tarefa_update, name='tarefa_update'),
    path('tarefas/<int:pk>/delete/', views.tarefa_delete, name='tarefa_delete'),

    # Rotas para Avaliacao
    path('avaliacoes/', views.avaliacao_list, name='avaliacao_list'),
    path('avaliacoes/create/', views.avaliacao_create, name='avaliacao_create'),
    path('avaliacoes/<int:pk>/update/', views.avaliacao_update, name='avaliacao_update'),
    path('avaliacoes/<int:pk>/delete/', views.avaliacao_delete, name='avaliacao_delete'),
]
