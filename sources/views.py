from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def integrante(request):
    return render(request, 'pages/integrante.html')

def administrador(request):
    return render(request, 'pages/administrador.html')