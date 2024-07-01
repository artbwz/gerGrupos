# sources/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Administrador, Grupo, Subgrupo, Tarefa, Avaliacao

# Views existentes
def index(request):
    return render(request, 'pages/index.html')

def integrante(request):
    return render(request, 'pages/integrante.html')

def administrador(request):
    return render(request, 'pages/administrador.html')

# Views para Usuario
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'pages/usuario_list.html', {'usuarios': usuarios})

def usuario_create(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/usuario_form.html')

def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/usuario_form.html', {'usuario': usuario})

def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'pages/usuario_confirm_delete.html', {'usuario': usuario})

# Views para Administrador
def administrador_list(request):
    administradores = Administrador.objects.all()
    return render(request, 'pages/administrador_list.html', {'administradores': administradores})

def administrador_create(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/administrador_form.html')

def administrador_update(request, pk):
    administrador = get_object_or_404(Administrador, pk=pk)
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/administrador_form.html', {'administrador': administrador})

def administrador_delete(request, pk):
    administrador = get_object_or_404(Administrador, pk=pk)
    if request.method == 'POST':
        administrador.delete()
        return redirect('administrador_list')
    return render(request, 'pages/administrador_confirm_delete.html', {'administrador': administrador})

# Similar views for Grupo, Subgrupo, Tarefa, Avaliacao
